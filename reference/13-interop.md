+++
title = "13. Interoperability"
weight = 13
+++

# 13. Interoperability


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

---

## Standard Library

Zen C includes a standard library (`std`) covering essential functionality.

[Browse the Standard Library Documentation](docs/std/README.md)

### C++ Interop

Zen C can generate C++-compatible code with the `--cpp` flag, allowing seamless
integration with C++ libraries.

```bash
# Direct compilation with g++
zc app.zc --cpp

# Or transpile for manual build
zc transpile app.zc --cpp
g++ out.c my_cpp_lib.o -o app
```

#### Using C++ in Zen C

Include C++ headers and use raw blocks for C++ code:

```zc
include <vector>
include <iostream>

raw {
    std::vector<int> make_vec(int a, int b) {
        return {a, b};
    }
}

fn main() {
    let v = make_vec(1, 2);
    raw { std::cout << "Size: " << v.size() << std::endl; }
}
```

> **Note:** The `--cpp` flag switches the backend to `g++` and emits C++-compatible
> code (uses `auto` instead of `__auto_type`, function overloads instead of `_Generic`,
> and explicit casts for `void*`).

---

### CUDA Interop

Zen C supports GPU programming by transpiling to **CUDA C++**.

```bash
# Direct compilation with nvcc
zc run app.zc --cuda

# Or transpile for manual build
zc transpile app.zc --cuda -o app.cu
nvcc app.cu -o app
```

#### CUDA Attributes

| Attribute | CUDA Equivalent | Description |
|:---|:---|:---|
| `@global` | `__global__` | Kernel function (runs on GPU, called from host) |
| `@device` | `__device__` | Device function (runs on GPU, called from GPU) |
| `@host` | `__host__` | Host function (explicit CPU-only) |

#### Kernel Launch Syntax

```zc
launch kernel_name(args) with {
    grid: num_blocks,
    block: threads_per_block,
    shared_mem: 1024,  // Optional
    stream: my_stream   // Optional
};
```

Transpiles to: `kernel_name<<<grid, block, shared, stream>>>(args);`

#### Writing CUDA Kernels

```zc
import "std/cuda.zc"

@global
fn add_kernel(a: float*, b: float*, c: float*, n: int) {
    let i = thread_id();
    if i < n { c[i] = a[i] + b[i]; }
}

fn main() {
    def N = 1024;
    let d_a = cuda_alloc<float>(N);
    let d_b = cuda_alloc<float>(N);
    let d_c = cuda_alloc<float>(N);
    defer cuda_free(d_a);
    defer cuda_free(d_b);
    defer cuda_free(d_c);

    launch add_kernel(d_a, d_b, d_c, N) with {
        grid: (N + 255) / 256,
        block: 256
    };
    cuda_sync();
}
```

> **Note:** The `--cuda` flag sets `nvcc` as the compiler and implies `--cpp` mode.
> Requires the NVIDIA CUDA Toolkit.

---

### Objective-C Interop

Zen C can compile to Objective-C (`.m`) using the `--objc` flag.

```bash
zc app.zc --objc --cc clang
```

```zc
include <Foundation/Foundation.h>

fn main() {
    raw {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        NSLog(@"Hello from Objective-C!");
        [pool drain];
    }
    println "Zen C works too!";
}
```

> **Note:** Zen C string interpolation works with Objective-C objects (`id`)
> by calling `debugDescription` or `description`.

---

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
