# Zen C vs C Comparison Guide

Internal documentation comparing Zen C language features and standard library
to their C equivalents. Each file shows Zen C code alongside equivalent C code
with explanations of the key differences.

This directory is **not synced** to the public docs website.

## Language Features

| # | File | Topic |
|---|------|-------|
| 1 | [Variables & Constants](language/01-variables.md) | `let`, `def`, type inference, `const`, `static` |
| 2 | [Primitive Types](language/02-primitive-types.md) | Integer, float, bool, char, void, rune, sized types |
| 3 | [Literals](language/03-literals.md) | Numeric, float, rune, string, binary, hex, octal |
| 4 | [Arrays](language/04-arrays.md) | Fixed-size arrays, value semantics, initialization |
| 5 | [Tuples](language/05-tuples.md) | Tuple construction, destructuring, multiple returns |
| 6 | [Structs](language/06-structs.md) | Structs, bitfields, opaque structs, type aliases |
| 7 | [Enums & Unions](language/07-enums-unions.md) | Tagged unions, pattern variants, C unions |
| 8 | [Functions](language/08-functions.md) | fn syntax, named args, defaults, variadic, fn* |
| 9 | [Lambdas](language/09-lambdas.md) | Closures, captures by ref/value, arrow syntax |
| 10 | [Control Flow](language/10-control-flow.md) | if/else, while, for ranges, loop, do-while |
| 11 | [Pattern Matching](language/11-pattern-matching.md) | match on literals, ranges, enums, ref binding |
| 12 | [Guard & Unless](language/12-guard-unless.md) | Guard early return, unless (inverted if) |
| 13 | [Operators](language/13-operators.md) | Operator overloading (arithmetic, index, comparison) |
| 14 | [Syntactic Sugar](language/14-sugar.md) | Pipe, null-coalescing, safe nav, try, auto-deref |
| 15 | [Printing & Interpolation](language/15-printing.md) | print/println, f-strings, raw strings, input |
| 16 | [Defer & Autofree](language/16-defer-autofree.md) | Deferred cleanup, automatic free |
| 17 | [Memory Management](language/17-memory.md) | Move semantics, Copy, Clone, Drop, RAII |
| 18 | [Methods](language/18-methods.md) | impl blocks, static/instance, primitive methods |
| 19 | [Traits](language/19-traits.md) | Trait definition, impl, trait objects, standard traits |
| 20 | [Composition](language/20-composition.md) | use keyword for mixin and named composition |
| 21 | [Generics](language/21-generics.md) | Generic structs, functions, constraints |
| 22 | [Concurrency](language/22-concurrency.md) | async/await, channels, launch |
| 23 | [Comptime](language/23-comptime.md) | Compile-time code generation, metadata |
| 24 | [Embed & Plugins](language/24-embed-plugins.md) | File embedding, compiler plugins |
| 25 | [Conditional Compilation](language/25-conditional.md) | cfg, defines, custom attributes, derive |
| 26 | [Attributes](language/26-attributes.md) | Inline, packed, align, section, noreturn, etc. |
| 27 | [Inline Assembly](language/27-assembly.md) | asm blocks, named constraints, volatile |
| 28 | [Build Directives](language/28-build.md) | link, lib, include, pkg-config, OS guards |
| 29 | [C Interop](language/29-ffi.md) | Trusted imports, explicit FFI, C/C++/CUDA |

## Standard Library

| # | File | C equivalent |
|---|------|-------------|
| 1 | [Vec](stdlib/vec.md) | Dynamic arrays (malloc/realloc) |
| 2 | [String](stdlib/string.md) | C strings (char*, strcpy/strcat) |
| 3 | [Option](stdlib/option.md) | Null checks, sentinel values |
| 4 | [Result](stdlib/result.md) | errno, return codes, goto error |
| 5 | [Map](stdlib/map.md) | Hash tables (uthash, hsearch) |
| 6 | [Set](stdlib/set.md) | Custom set implementations |
| 7 | [Iter](stdlib/iter.md) | Manual loops with indices |
| 8 | [Sort](stdlib/sort.md) | qsort() with comparators |
| 9 | [IO](stdlib/io.md) | printf/scanf, file I/O |
| 10 | [FS](stdlib/fs.md) | fopen/fread/fwrite/stat |
| 11 | [Path](stdlib/path.md) | Manual path manipulation |
| 12 | [Net](stdlib/net.md) | BSD sockets |
| 13 | [Thread](stdlib/thread.md) | pthread_create/join |
| 14 | [Sync](stdlib/sync.md) | pthread_mutex/semaphore |
| 15 | [Time](stdlib/time.md) | time.h, clock_gettime |
| 16 | [JSON](stdlib/json.md) | Manual parsing (cJSON pattern) |
| 17 | [Regex](stdlib/regex.md) | regex.h (POSIX) |
| 18 | [Stack & Queue](stdlib/stack-queue.md) | Array/linked-list based LIFO/FIFO |
| 19 | [BigInt & BigFloat](stdlib/bigint-bigfloat.md) | GMP / custom big number |
| 20 | [Complex](stdlib/complex.md) | complex.h (C99) |
| 21 | [Bits](stdlib/bits.md) | Manual bit shifts and masks |
| 22 | [CUDA](stdlib/cuda.md) | Raw CUDA C API |
| 23 | [SIMD](stdlib/simd.md) | Intrinsics (_mm_add_ps, etc.) |
| 24 | [Arena & Mman](stdlib/arena-mman.md) | Custom arena allocators, mmap |
| 25 | [Process & Env](stdlib/process-env.md) | system(), popen(), getenv() |

## Testing

Run `python3 compare/scripts/check_comparisons.py` to compile and run all code
blocks, verifying that Zen C and C output match.
