import { translate } from '@vitalets/google-translate-api';
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from 'fs';
import { join } from 'path';
import { setTimeout } from 'timers/promises';

const LANGUAGES = ['es', 'pt', 'it', 'de', 'ru', 'zh-cn', 'zh-tw'];
const DIRS = ['std', 'rosetta'];

// Technical terms that should NEVER be translated
const PROTECTED_TERMS = [
    'Zen C', 'CUDA', 'SIMD', 'UTF-8', 'UTF8', 'UTF-16', 'UTF16', 'UTF-32', 'UTF32',
    'IO', 'API', 'GPGPU', 'LSP', 'REPL', 'ABI', 'RAII', 'FFI', 'LLD', 'LLVM', 'GCC', 'Clang',
    'JSON', 'HTTP', 'TCP', 'UDP', 'DNS', 'URL', 'SHA1', 'SHA256', 'Base64', 'DOM',
    'Vec', 'BigInt', 'BigFloat', 'Map', 'Set', 'Stack', 'Queue', 'Result', 'Option', 'Some', 'None', 'Ok', 'Err',
    'zc', 'zprep', 'zenc', 'cosmocc', 'APE'
];

const sleep = async (ms) => await setTimeout(ms);

async function safeTranslate(text, lang) {
    if (!text.trim() || text.length < 2) return text;
    if (text.match(/^[a-zA-Z0-9_/.-]+$/)) return text;

    console.log(`    -> Translating chunk... (${text.length} chars)`);

    // Protect terms with placeholders
    let termStore = [];
    let sanitizedText = text;

    // Sort terms by length descending to avoid partial matches (e.g. 'Zen C' before 'Zen')
    const sortedTerms = [...PROTECTED_TERMS].sort((a, b) => b.length - a.length);

    for (const term of sortedTerms) {
        const regex = new RegExp(`\\b${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'g');
        sanitizedText = sanitizedText.replace(regex, (m) => {
            termStore.push(m);
            return `__TERM${termStore.length - 1}__`;
        });
    }

    const timeout = ms => new Promise((_, reject) => globalThis.setTimeout(() => reject(new Error('TIMEOUT')), ms));

    try {
        const res = await Promise.race([translate(sanitizedText, { to: lang }), timeout(15000)]);
        let trans = res.text;

        // Restore terms
        trans = trans.replace(/__TERM(\d+)__/g, (m, id) => termStore[parseInt(id)]);
        return trans;
    } catch (e) {
        console.error(`    -> [ERROR: ${e.message}] Sleeping 10s before retrying...`);
        await sleep(10000);
        try {
            const retryRes = await Promise.race([translate(sanitizedText, { to: lang }), timeout(20000)]);
            let trans = retryRes.text;
            trans = trans.replace(/__TERM(\d+)__/g, (m, id) => termStore[parseInt(id)]);
            return trans;
        } catch (e2) {
            console.error(`    -> [FATAL: ${e2.message}] Skipping chunk.`);
            return text;
        }
    }
}

async function translateMarkdown(content, lang) {
    const lines = content.split('\n');
    let inFrontmatter = false;
    let inCodeBlock = false;
    let translatedLines = [];
    let textBuffer = [];

    const processParagraph = async (rawParagraph) => {
        if (!rawParagraph.trim()) return rawParagraph;

        // 1. Protect inline code
        let codeStore = [];
        let p1 = rawParagraph.replace(/`([^`]+)`/g, (m, code) => {
            codeStore.push(code);
            return `__CODE${codeStore.length - 1}__`;
        });

        // 2. Protect link URLs and optionally the titles
        let linkStore = [];
        let p2 = p1.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, text, url) => {
            linkStore.push(url);
            // If text is short or looks like a module name, protect it too
            if (text.length < 5 || text.match(/^[a-z0-9_]+$/)) {
                linkStore.push(text);
                return `[__LTEXT${linkStore.length - 1}__](__URL${linkStore.length - 2}__)`;
            }
            return `[${text}](__URL${linkStore.length - 1}__)`;
        });

        // 3. Translate
        let trans = await safeTranslate(p2, lang);

        // 4. Restore
        trans = trans.replace(/__URL(\d+)__/g, (m, id) => linkStore[parseInt(id)]);
        trans = trans.replace(/__LTEXT(\d+)__/g, (m, id) => linkStore[parseInt(id)]);
        trans = trans.replace(/\]\s+\(/g, '](');
        trans = trans.replace(/__CODE(\d+)__/g, (m, id) => `\`${codeStore[parseInt(id)]}\``);

        return trans;
    };

    const flushTextBuffer = async () => {
        if (textBuffer.length > 0) {
            const rawText = textBuffer.join('\n');
            const transText = await processParagraph(rawText);
            translatedLines.push(transText);
            textBuffer = [];
            await sleep(5000); // 5s between paragraphs
        }
    };

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        if (line.trim() === '+++') {
            await flushTextBuffer();
            inFrontmatter = !inFrontmatter;
            translatedLines.push(line);
            continue;
        }

        if (inFrontmatter) {
            if (line.startsWith('title = ')) {
                const titleMatch = line.match(/^title\s*=\s*"([^"]+)"/);
                if (titleMatch) {
                    const titleStr = titleMatch[1];
                    const tTitle = await processParagraph(titleStr);
                    translatedLines.push(`title = "${tTitle.replace(/"/g, '\\"')}"`);
                } else {
                    translatedLines.push(line);
                }
            } else {
                translatedLines.push(line);
            }
            continue;
        }

        if (line.trim().startsWith('\`\`\`')) {
            await flushTextBuffer();
            inCodeBlock = !inCodeBlock;
            translatedLines.push(line);
            continue;
        }

        if (inCodeBlock) {
            translatedLines.push(line);
            continue;
        }

        if (line.trim().startsWith('|')) {
            await flushTextBuffer();
            if (line.includes('---')) {
                translatedLines.push(line);
            } else {
                const cells = line.split('|');
                let translatedCells = [];
                for (let cell of cells) {
                    if (!cell.trim() || cell.trim().match(/^[*\-]+$/)) {
                        translatedCells.push(cell);
                    } else {
                        translatedCells.push(` ${await processParagraph(cell.trim())} `);
                    }
                }
                translatedLines.push(translatedCells.join('|'));
            }
            continue;
        }

        if (line.trim().startsWith('> [!')) {
            await flushTextBuffer();
            const alertMatch = line.match(/^(>\s*\[!(\w+)\]\s*)(.*)/);
            if (alertMatch) {
                translatedLines.push(`${alertMatch[1]}${await processParagraph(alertMatch[3])}`);
            } else {
                translatedLines.push(line);
            }
            continue;
        }

        if (line.trim().startsWith('>')) {
            await flushTextBuffer();
            translatedLines.push(`> ${await processParagraph(line.replace(/^>\s?/, ''))}`);
            continue;
        }

        if (line.startsWith('#')) {
            await flushTextBuffer();
            const headerMatch = line.match(/^(#+)\s*(.*)/);
            if (headerMatch) {
                translatedLines.push(`${headerMatch[1]} ${await processParagraph(headerMatch[2])}`);
            } else {
                translatedLines.push(line);
            }
            continue;
        }

        if (!line.trim()) {
            await flushTextBuffer();
            translatedLines.push(line);
            continue;
        }

        textBuffer.push(line);
    }
    await flushTextBuffer();
    return translatedLines.join('\n');
}

async function walkAndTranslate() {
    for (const dir of DIRS) {
        if (!existsSync(dir)) continue;
        const files = readdirSync(dir);

        for (const file of files) {
            if (file.match(/\.(es|pt|it|de|ru|zh-cn|zh-tw)\.md$/)) continue;
            if (!statSync(join(dir, file)).isFile()) continue;

            const baseName = file.substring(0, file.length - 3);
            const content = readFileSync(join(dir, file), 'utf8');

            console.log(`\nTranslating: ${join(dir, file)}`);

            for (const lang of LANGUAGES) {
                const outPath = join(dir, `${baseName}.${lang}.md`);
                if (existsSync(outPath)) {
                    const stats = statSync(outPath);
                    if (stats.size > 100) {
                        console.log(`  [SKIP] ${lang} already exists (${stats.size} bytes)`);
                        continue;
                    }
                }

                console.log(`  [=> ${lang}] Creating...`);
                const translated = await translateMarkdown(content, lang);
                writeFileSync(outPath, translated);
                console.log(`  [OK] Saved ${outPath}`);
                await sleep(15000); // 15s between languages
            }
            await sleep(30000); // 30s between files
        }
    }
}

walkAndTranslate().then(() => console.log('Done!'));
