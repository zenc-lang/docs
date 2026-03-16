# Zen C Documentation

Welcome to the official documentation repository for the **Zen C** programming language. This repository contains the technical specifications, language reference, and standard library documentation.

## Documentation Index

### Standard Library
The core of Zen C's power lies in its standard library. Detailed documentation for each module can be found in the [std/](std/) directory.

| Module | Description |
| :--- | :--- |
| **[vec](std/vec.md)** | Dynamic array implementation. |
| **[string](std/string.md)** | Modern, safe string handling. |
| **[net](std/net.md)** | High-level networking (TCP, HTTP). |
| **[cuda](std/cuda.md)** | First-class GPU programming support. |
| **[thread](std/thread.md)** | Concurrency and parallelism. |
| **[json](std/json.md)** | Built-in JSON serialization/deserialization. |

> [!NOTE]
> For a high-level overview of the library, see the **[Standard Library README](std/README.md)**.

### Technical Specifications
Deep dives into the compiler's internals and tooling protocols.

- **[Lexer Specification](lex.md)**: Detailed breakdown of Zen C's tokens and grammar rules.
- **[LSP Protocol](LSP.md)**: Documentation for the Zen C Language Server integration.
- **[Plugin System](PLUGINS.md)**: How to extend the compiler with custom plugins.

## Related Resources

- **[zenc](https://github.com/zenc-lang/zenc)**: The core compiler source code.
- **[awesome-zenc](https://github.com/zenc-lang/awesome-zenc)**: A collection of examples and Rosetta Code implementations.

## Contributing to Docs

Documentation is a community effort. If you find a typo, outdated information, or want to contribute a new guide, please open a documentation issue or pull request.
