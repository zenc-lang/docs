+++
title = "12. Avanzate e Metaprogrammazione"
weight = 12
+++

# 12. Avanzate e Metaprogrammazione


### Metaprogramming

#### Comptime
Esegui codice al momento della compilazione per generare sorgente o stampare messaggi.
```zc
comptime {
    // Genera codice al momento della compilazione (scritto su stdout)
    println "let data_compilazione = \"2024-01-01\";";
}

println "Data compilazione: {data_compilazione}";
```

<details>
<summary><b>Funzioni Helper</b></summary>

Funzioni speciali disponibili all'interno dei blocchi `comptime`:

<table>
<tr>
<th>Funzione</th>
<th>Descrizione</th>
</tr>
<tr>
<td><code>yield(str)</code></td>
<td>Emette esplicitamente codice generato (alternativa a <code>printf</code>)</td>
</tr>
<tr>
<td><code>code(str)</code></td>
<td>Alias di <code>yield()</code> - intento più chiaro per generazione codice</td>
</tr>
<tr>
<td><code>compile_error(msg)</code></td>
<td>Interrompe la compilazione con un messaggio di errore fatale</td>
</tr>
<tr>
<td><code>compile_warn(msg)</code></td>
<td>Emette un avviso al momento della compilazione (consente di continuare)</td>
</tr>
</table>

**Esempio:**
```zc
comptime {
    compile_warn("Generazione codice ottimizzato...");
    
    let ENABLE_FEATURE = 1;
    if (ENABLE_FEATURE == 0) {
        compile_error("La funzionalità deve essere abilitata!");
    }
    
    // Usa code() con raw strings per generazione pulita
    code(r"let FEATURE_ENABLED = 1;");
}
```
</details>

<details>
<summary><b>Metadati di Build</b></summary>

Accedi alle informazioni di build del compilatore al momento della compilazione:

<table>
<tr>
<th>Costante</th>
<th>Tipo</th>
<th>Descrizione</th>
</tr>
<tr>
<td><code>__COMPTIME_TARGET__</code></td>
<td>string</td>
<td>Piattaforma: <code>"linux"</code>, <code>"windows"</code> o <code>"macos"</code></td>
</tr>
<tr>
<td><code>__COMPTIME_FILE__</code></td>
<td>string</td>
<td>Nome del file sorgente corrente in compilazione</td>
</tr>
</table>

**Esempio:**
```zc
comptime {
    // Generazione codice specifico per piattaforma
    println "let PLATFORM = \"{__COMPTIME_TARGET__}\";";
}

println "In esecuzione su: {PLATFORM}";
```
</details>

{% alert(type="tip") %}
Usa raw strings (`r"..."`) in comptime per evitare di eseguire l'escape delle parentesi graffe: `code(r"fn test() { return 42; }")`. Altrimenti, usa `{{` e `}}` per l'escape nelle stringhe normali.
{% end %}


#### Incorporati
Incorpora file come tipi specificati.
```zc
// Default (Slice_char)
let data = embed "assets/logo.png";

// Incorporazioni tipizzate
let testo = embed "shader.glsl" as string;    // Incorpora come una stringa C
let rom   = embed "bios.bin" as u8[1024];     // Incorpora come un array a dimensione fissa
let wav   = embed "sound.wav" as u8[];        // Incorpora come Slice_u8
```

#### Plugin
Importa plugin del compilatore per estendere la sintassi.
```zc
import plugin "regex"
let re = regex! { ^[a-z]+$ };
```

#### Macro C Generiche
Passa delle macro del preprocessore C.

{% alert(type="tip") %}
Per delle semplici costanti, utilizza `def`. Usa `#define` solo quanto ti servono macro del preprocessore C o flag di compilazione condizionale.
{% end %}

```zc
#define BUFFER_MASSIMO 1024
```

#### Compilazione Condizionale
Usa `@cfg()` per includere o escludere condizionalmente qualsiasi dichiarazione di livello superiore in base ai flag `-D`.

```zc
// Compila con: zc build app.zc -DUSE_OPENGL

@cfg(USE_OPENGL)
import "opengl_backend.zc";

@cfg(USE_VULKAN)
import "vulkan_backend.zc";

@cfg(not(USE_OPENGL))
@cfg(not(USE_VULKAN))
fn fallback_init() { println "Nessun backend selezionato"; }
```

| Forma | Significato |
|:---|:---|
| `@cfg(NAME)` | Includi se `-DNAME` è definito |
| `@cfg(not(NAME))` | Includi se `-DNAME` NON è definito |
| `@cfg(any(A, B, ...))` | Includi se QUALSIASI condizione è vera (OR) |
| `@cfg(all(A, B, ...))` | Includi se TUTTE le condizioni sono vere (AND) |

Più `@cfg` su una dichiarazione vengono combinati con AND. `not()` può essere usato dentro `any()` e `all()`. Funziona con qualsiasi dichiarazione di livello superiore: `fn`, `struct`, `import`, `impl`, `raw`, `def`, `test`, ecc.

### Attributi

Decora le funzioni e gli struct per modificare il comportamento del compilatore.

| Attributo | Ambito | Descrizione |
|:---|:---|:---|
| `@required` | Fn | Avvereti se il valore di ritorno viene ignorato. |
| `@deprecated("msg")` | Fn/Struct | Avverti all'uso con 'msg' |
| `@inline` | Fn | Suggerisci al compilatore di rendere il codice inline |
| `@noinline` | Fn | Previeni l'inline automatico |
| `@packed` | Struct | Rimuovi il padding (lett. _imbottitura_) automatico in mezzo ai campi. |
| `@align(N)` | Struct | Forza l'allineamento a N byte. |
| `@constructor` | Fn | Esegui prima di `main`. |
| `@destructor` | Fn | Esegue dopo la terminazione di `main`. |
| `@unused` | Fn/Var | Sopprimi gli errori di 'variabile inutilizzata' |
| `@weak` | Fn | Linking dei simboli _weak_ (lett. _debole_). |
| `@section("name")` | Fn | Inserisci il codice in una specifica sezione. |
| `@noreturn` | Fn | La funzione non restituisce valori. (e.g. `exit`). |
| `@pure` | Fn | La funzione non ha effetti collaterali (indizio per l'ottimizzazione). |
| `@cold` | Fn | La funzione è usata poco spesso (indizio per la branch prediction). |
| `@hot` | Fn | La funzione è usata molto spesso (indizio per l'ottimizzazione). |
| `@export` | Fn/Struct | Esporta simbolo (visibilità default). |
| `@global` | Fn | CUDA: Entry point del Kernel (`__global__`). |
| `@device` | Fn | CUDA: Funzione del Device (`__device__`). |
| `@host` | Fn | CUDA: Funzione dell'Host (`__host__`). |
| `@comptime` | Fn | Funzione di supporto disponibile per l'esecuzione al tempo di compilazione. |
| `@cfg(NAME)` | Qualsiasi | Compilazione condizionale: includi solo se viene passato `-DNAME`. Supporta `not()`, `any()`, `all()`. |
| `@derive(...)` | Struct | Implementa automaticamente i tratti. Supporta `Debug`, `Eq` (Derivazione Intelligente), `Copy`, `Clone`. |
| `@<custom>` | Any | Passa gli attributi generici direttamente al C (e.g. `@flatten`, `@alias("nome")`) |

#### Attributi Personalizzati

Zen C supporta un potente sistema di **Attributi Personalizzati** che ti permettono di utilizzare ogni `__attributo__` GCC/Clang direttamente nel tuo codice Zen C. Qualsiasi attributo non riconosciuto dal compilatore Zen C viene trattato come un attributo generico e passato direttamente nel codice C generato.

Ciò fornisce accesso a delle avanzate funzionalità, ottimizzazioni e direttive del linker senza necessitare di un supporto esplicito nel cuore del linguaggio.

#### Mappatura della Sintassi
Zen C attributes are mapped directly to C attributes:
- `@name` → `__attribute__((name))`
- `@name(args)` → `__attribute__((name(args)))`
- `@name("string")` → `__attribute__((name("string")))`

#### Derivazioni Intelligenti

Zen C fornisce delle "derivazioni intelligenti" che rispettano le Semantiche di Movimento:

- **`@derive(Eq)`**: Genera un metodo di uguaglianza che prende argomenti per referenza (`fn eq(self, other: T*)`).
    - Quando si confrontano due struct non-Copy (`a == b`), il compilatore passa automaticamente `b` per referenza (`&b`) per non doverlo spostare.
    - I controlli di uguaglianza ricorsivi preferiscono l'accesso da puntatore per prevenire il trasferimento del proprietario.

### Assembly Inline

Zen C fornisce supporto di prima-classe per l'assembly _inline_, traspilando direttamente ad `asm` con estensioni in stile GCC.

#### Utilizzo Base
Scrivi assembly grezzo all'interno di blocchi `asm`. Le stringhe vengono concatenate automaticamente.
```zc
asm {
    "nop"
    "mfence"
}
```

#### Volatile
Impedisci al compilatore di eliminare automaticamente istruzioni assembly (e.g. ottimizzazione) se ciò potrebbe avere ripercussioni.
```zc
asm volatile {
    "rdtsc"
}
```

#### Vincoli Nominati
Zen C semplifica la sintassi complessa dei vincoli di GCC con dei binding nominati.

**Nota per i lettori italiani**: Con 'clobber' si intende la *sovrascrizione*.

```zc
// Sintassi: : out(variable) : in(variable) : clobber(reg)
// Usa una sintassi placeholder (`{variabile}`) per la leggibilità

fn aggiungi_cinque(x: int) -> int {
    let risultato: int;
    asm {
        "mov {x}, {risultato}"
        "add $5, {risultato}"
        : out(risultato)
        : in(x)
        : clobber("cc")
    }
    return risultato;
}
```

| Tipo | Sintassi | Equivalente GCC |
|:---|:---|:---|
| **Output** | `: out(variabile)` | `"=r"(variabile)` |
| **Input** | `: in(variabile)` | `"r"(variabile)` |
| **Clobber** | `: clobber("rax")` | `"rax"` |
| **Memory** | `: clobber("memoria")` | `"memoria"` |

{% alert(type="note") %}
Quando si usa la sintassi Intel (via `-masm=intel`), dovrai assicurarti che la tua build sia configurata correttamente (per esempio, `//> cflags: -masm=intel`). TCC non supporta la sintassi assembly Intel.
{% end %}


### Direttive della Build

Zen C supporta dei commenti speciali all'inizio del tuo file sorgente che ti permettono di configurare il processo di build senza necessitare di un sistema di build complesso o di un *Makefile*.

| Direttiva | Argomenti | Descrizione |
|:---|:---|:---|
| `//> link:` | `-lfoo` oppure `path/to/lib.a` | Linka con una libreria o un file object. |
| `//> lib:` | `path/to/libs` | Aggiunge una directory dove cercare le librerie (`-L`). |
| `//> include:` | `path/to/headers` | Aggiunge una directory dove cercare i file include (`-I`). |
| `//> framework:` | `Cocoa` | Linka con un framework macOS. |
| `//> cflags:` | `-Wall -O3` | Passa flag arbitrare al compilatore C. |
| `//> define:` | `MACRO` or `KEY=VAL` | Definisci una macro del preprocessore (`-D`). |
| `//> pkg-config:` | `gtk+-3.0` | Esegui `pkg-config` e aggiungi `--cflags` e `--libs`. |
| `//> shell:` | `command` | Esegui un comando sulla shell durante il processo di build. |
| `//> get:` | `http://url/file` | Scarica un file se un file specifico non esiste. |

#### Feature

**1. OS Guarding** (lett. _Protezione OS_)
Prefissa delle direttive con il nome di un OS per applicarle solo su piattaforme specifiche.
Prefissi supportati: `linux:`, `windows:`, `macos:` (or `darwin:`).

```zc
//> linux: link: -lm
//> windows: link: -lws2_32
//> macos: framework: Cocoa
```

**2. Environment Variable Expansion**
Utilizza la sintassi `${VAR}` per espandare variabili d'ambiente nelle tue direttive.

```zc
//> include: ${HOME}/MiaLibreria/include
//> lib: ${ZC_ROOT}/std
```

#### Esempi

```zc
//> include: ./include
//> lib: ./librerie
//> link: -lraylib -lm
//> cflags: -Ofast
//> pkg-config: gtk+-3.0

import "raylib.h"

fn main() { ... }
```

### Keyword

Le keyword che seguono sono riservate in Zen C.

#### Dichiarazioni
`alias`, `def`, `enum`, `fn`, `impl`, `import`, `let`, `module`, `opaque`, `struct`, `trait`, `union`, `use`

#### Controllo del Flusso
`async`, `await`, `break`, `catch`, `continue`, `defer`, `do`, `else`, `for`, `goto`, `guard`, `if`, `loop`, `match`, `return`, `try`, `unless`, `while`

#### Speciali
`asm`, `assert`, `autofree`, `comptime`, `const`, `embed`, `launch`, `ref`, `sizeof`, `static`, `test`, `volatile`

#### Costanti
`true`, `false`, `null`

#### Riservate del C
Gli identifiers seguenti sono riservati poiché sono keyword nello standard C11:
`auto`, `case`, `char`, `default`, `double`, `extern`, `float`, `inline`, `int`, `long`, `register`, `restrict`, `short`, `signed`, `switch`, `typedef`, `unsigned`, `void`, `_Atomic`, `_Bool`, `_Complex`, `_Generic`, `_Imaginary`, `_Noreturn`, `_Static_assert`, `_Thread_local`

#### Operatori
`and`, `or`
