# Zen C Language Server Protocol (LSP)

Zen C ships a Language Server (LSP) binary, `zc-lsp`, that provides editor features like autocompletion, go-to-definition, and error diagnostics.

## Starting the Server

`zc-lsp` is a standalone binary installed alongside `zc`. (The legacy `zc lsp` subcommand still works as a deprecated alias.) You can start it manually (though your editor usually handles this) with:

```bash
zc-lsp
```

It communicates over standard input/output (stdio).

## Editor Configuration

### VS Code

For Visual Studio Code, use the official Zen C extension:

- **Repository**: [zenc-lang/vscode-zenc](https://github.com/zenc-lang/vscode-zenc)

Install the extension directly from the **[Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=zenc-lang.zenc)**.

Alternatively, you can build the `.vsix` from source.

### Vim / Neovim

Support for Vim and Neovim is provided via the `Zen-C.vim` plugin, which includes syntax highlighting and LSP configuration helpers.

- **Repository**: [davidscholberg/Zen-C.vim](https://github.com/davidscholberg/Zen-C.vim)

#### Neovim (`lazy.nvim` example)

If you are using `nvim-lspconfig`, you can register `zc` as a custom server:

```lua
local lspconfig = require('lspconfig')
local configs = require('lspconfig.configs')

if not configs.zenc then
  configs.zenc = {
    default_config = {
      cmd = { 'zc-lsp' },
      filetypes = { 'zenc', 'zc' },
      root_dir = lspconfig.util.root_pattern('.git', 'build.bat', 'Makefile'),
      settings = {},
    },
  }
end

lspconfig.zenc.setup {}
```

### Zed

To configure Zen C in Zed, add the following to your `settings.json` or language configuration:

```json
{
  "lsp": {
    "zenc": {
      "binary": {
        "path": "zc-lsp"
      }
    }
  },
  "languages": {
    "Zen C": {
      "language_servers": ["zenc"]
    }
  }
}
```

### Generic Editors (Sublime, Emacs, etc.)

For any editor that supports generic LSP clients:

1.  **Command**: `zc-lsp`
2.  **Transport**: `stdio`
3.  **File Extensions**: `.zc`

## Project Configuration

When the server starts, it indexes every `.zc` file under the workspace root, skipping what the root `.gitignore` ignores.

To configure the server per project, place a `zenc.server.json` file in the workspace root:

```json
{
  "include_paths": ["../libs", "third_party/include"],
  "exclude": ["generated/", "*.tmp.zc"],
  "use_gitignore": true
}
```

*   `include_paths`: extra directories used to resolve imports, like `zc -I`. Relative paths are resolved against the directory containing `zenc.server.json`.
*   `exclude`: patterns in `.gitignore` syntax, relative to the workspace root, that the workspace indexing skips (names at any depth, `/anchored` paths, a trailing `/` for directories only, `*`, `?`, a leading `**/`), on top of the `.gitignore` rules.
*   `use_gitignore`: `true` by default. When `false`, the root `.gitignore` is not read and `exclude` alone decides what is skipped.

All keys are optional. Invalid JSON ignores the whole file; an unknown key or a value of the wrong type is ignored. Either case is reported in the editor with a warning.

## Features

- **Diagnostics**: Real-time syntax and type errors.
- **Go to Definition**: Jump to struct, function, and variable definitions.
- **Autocompletion**: Context-aware suggestions for fields and methods.
- **Hover**: Type information and documentation on hover (including custom DSL plugins).
