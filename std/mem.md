# std/mem

The `std/mem` module provides core memory management utilities, including manual allocation functions, standard lifecycle traits, and smart pointer implementations.

## Overview

- **Manual Allocation**: Wrappers around `malloc`, `calloc`, and `free` with type-safe signatures.
- **Traits**: Defines the primary lifecycle traits: `Drop` (destructors), `Clone` (deep copies), and `Copy` (implicit copies).
- **Smart Pointers**: Includes `Box<T>` for heap-allocated data with automatic cleanup (RAII).
- **Buffer Utilities**: High-level functions for swapping, zeroing, and copying memory.

## Usage

```zc
import "std/mem.zc"

fn main() {
    // Manual allocation
    let ptr = alloc<int>();
    *ptr = 42;
    free(ptr);
    
    // Automatic cleanup with Box (RAII)
    {
        let b = Box<int>::new();
        *b.get() = 100;
        // memory is freed automatically here
    }
}
```

## Methods

### Allocation

| Method | Signature | Description |
| :--- | :--- | :--- |
| **alloc\<T>**| `alloc<T>() -> T*` | Allocates memory for a single instance of `T`. |
| **zalloc\<T>**| `zalloc<T>() -> T*` | Allocates zero-initialized memory for a single instance of `T`. |
| **alloc_n\<T>**| `alloc_n<T>(n: usize) -> T*` | Allocates memory for an array of `n` instances of `T`. |

### Operations

| Method | Signature | Description |
| :--- | :--- | :--- |
| **mem_zero\<T>**| `mem_zero<T>(ptr: T*, count: usize)` | Sets memory for `count` instances of `T` to zero. |
| **mem_copy\<T>**| `mem_copy<T>(dst: T*, src: T*, count: usize)`| Copies `count` instances of `T` from `src` to `dst`. |
| **swap\<T>** | `swap<T>(a: T*, b: T*)` | Swaps the values between two memory locations. |

## Traits

| Trait | Method | Signature | Description |
| :--- | :--- | :--- | :--- |
| **Drop** | **drop** | `drop(self)` | Destructor called when object goes out of scope. |
| **Clone** | **clone** | `clone(self) -> Self` | Creates a deep copy of the object. |
| **Copy** | *(Marker)* | N/A | Indicates the type should use implicit copies instead of moves. |

## Struct Definition: `Box<T>`

A simple RAII smart pointer for managing heap memory.

```zc
struct Box<T> {
    ptr: T*;
}
```

### `Box` Methods

| Method | Signature | Description |
| :--- | :--- | :--- |
| **new** | `Box::new() -> Box<T>` | Allocates a new heap-managed instance. |
| **from_ptr** | `Box::from_ptr(p: T*) -> Box<T>` | Creates a `Box` that takes ownership of an existing pointer. |
| **get** | `get(self) -> T*` | Returns the raw internal pointer. |
| **free** | `free(self)` | Manually frees the underlying memory. |
| **Trait** | `impl Drop for Box<T>` | Automatically calls `free()` when the box exists scope. |
