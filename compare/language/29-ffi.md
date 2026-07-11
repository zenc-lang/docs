+++
title = "C Interop (FFI)"
weight = 29
+++

# C Interop (FFI)

Call C functions via trusted imports or explicit FFI declarations.
Include C headers and bridge C/C++/CUDA/Objective-C code.

## Zen C

```zc
import "std/io.zc"

import "math.h" as c_math;

extern fn printf(fmt: char*, ...) -> c_int;

include <stdlib.h>

fn main() {
    let pi = c_math::cos(3.14159);
    println "cos(pi): {pi}";

    printf("via C printf: %d, %s\n", 42, "Zen");

    let ptr = malloc(64);
    defer free(ptr);
    println "malloc'd 64 bytes via C stdlib";
}
```

## C

```c
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    double pi = cos(3.14159);
    printf("cos(pi): %f\n", pi);

    printf("via C printf: %d, %s\n", 42, "C");

    void* ptr = malloc(64);
    printf("malloc'd 64 bytes via C stdlib\n");
    free(ptr);
    return 0;
}
```

## Key Differences

- Trusted imports: `import "math.h" as c_math` gives zero-boilerplate access
- Access via namespace: `c_math::cos(...)`
- Explicit FFI: `extern fn printf(fmt: char*, ...) -> c_int` for type safety
- `include <header.h>` emits `#include` without introducing symbols to compiler
- `import` registers module; `include` is pure emission
- C interop types: `c_int`, `c_char`, `c_long` etc. map directly to C types
- Method 1 (Trusted Imports): fast, loose type checking
- Method 2 (Explicit FFI): strict, explicit, type-safe declarations
- C/Safe: just writes C code directly

## Output

cos(pi): -1.000000
via C printf: 42, Zen
malloc'd 64 bytes via C stdlib
