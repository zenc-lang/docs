+++
title = "13. C Interoperability"
weight = 13
+++

# 13. C Interoperability


Zen C offers two ways to interact with C code: **Trusted Imports** (Convenient) and **Explicit FFI** (Safe/Precise).

#### Method 1: Trusted Imports (Convenient)

You can import a C header directly using the `import` keyword with the `.h` extension. This treats the header as a module and assumes all symbols accessed through it exist.

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // Compiler trusts correctness; emits 'cos(...)' directly
    let x = c_math::cos(3.14159);
}
```

> **Pros**: Zero boilerplate. Access everything in the header immediately.
> **Cons**: No type safety from Zen C (errors caught by C compiler later).

#### Method 2: Explicit FFI (Safe)

For strict type checking or when you don't want to include the text of a header, use `extern fn`.

```zc
include <stdio.h> // Emits #include <stdio.h> in generated C

// Define strict signature
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Hello FFI: %d\n", 42); // Type checked by Zen C
}
```

> **Pros**: Zen C ensures types match.
> **Cons**: Requires manual declaration of functions.

#### `import` vs `include`

- **`import "file.h"`**: Registers the header as a named module. Enables implicit access to symbols (for example, `file::function()`).
- **`include <file.h>`**: Purely emits `#include <file.h>` in the generated C code. Does not introduce any symbols to the Zen C compiler; you must use `extern fn` to access them.

#### Diagnostics & Friction

By default, Zen C suppresses "Undefined function" warnings for standard C library functions to provide a frictionless interop experience. You can control this behavior using the `-Winterop` and `-Wno-interop` flags.

[Read more about the Diagnostic System](15-diagnostics.md)

---

## Standard Library

Zen C includes a standard library (`std`) covering essential functionality.

[Browse the Standard Library Documentation](docs/std/README.md)

### Key Modules

<details>
<summary>Click to see all Standard Library modules</summary>

| Module | Description | Docs |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | Arbitrary-precision floating-point arithmetic. | [Docs](docs/std/bigfloat.md) |
| **`std/bigint.zc`** | Arbitrary-precision integer `BigInt`. | [Docs](docs/std/bigint.md) |
| **`std/bits.zc`** | Low-level bitwise operations (`rotl`, `rotr`). | [Docs](docs/std/bits.md) |
| **`std/complex.zc`** | Complex Number Arithmetic `Complex`. | [Docs](docs/std/complex.md) |
| **`std/vec.zc`** | Growable dynamic array `Vec<T>`. | [Docs](docs/std/vec.md) |
| **`std/string.zc`** | Heap-allocated `String` type with UTF-8 support. | [Docs](docs/std/string.md) |
| **`std/queue.zc`** | FIFO queue (Ring Buffer). | [Docs](docs/std/queue.md) |
| **`std/map.zc`** | Generic Hash Map `Map<V>`. | [Docs](docs/std/map.md) |
| **`std/fs.zc`** | File system operations. | [Docs](docs/std/fs.md) |
| **`std/io.zc`** | Standard Input/Output (`print`/`println`). | [Docs](docs/std/io.md) |
| **`std/option.zc`** | Optional values (`Some`/`None`). | [Docs](docs/std/option.md) |
| **`std/result.zc`** | Error handling (`Ok`/`Err`). | [Docs](docs/std/result.md) |
| **`std/path.zc`** | Cross-platform path manipulation. | [Docs](docs/std/path.md) |
| **`std/env.zc`** | Process environment variables. | [Docs](docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [Docs](docs/std/net.md) |
| **`std/thread.zc`** | Threads and Synchronization. | [Docs](docs/std/thread.md) |
| **`std/time.zc`** | Time measurement and sleep. | [Docs](docs/std/time.md) |
| **`std/json.zc`** | JSON parsing and serialization. | [Docs](docs/std/json.md) |
| **`std/stack.zc`** | LIFO Stack `Stack<T>`. | [Docs](docs/std/stack.md) |
| **`std/set.zc`** | Generic Hash Set `Set<T>`. | [Docs](docs/std/set.md) |
| **`std/process.zc`** | Process execution and management. | [Docs](docs/std/process.md) |
| **`std/regex.zc`** | Regular Expressions (TRE based). | [Docs](docs/std/regex.md) |
| **`std/simd.zc`** | Native SIMD vector types. | [Docs](docs/std/simd.md) |

</details>
