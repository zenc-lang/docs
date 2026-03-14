# std/arena

The `std/arena` module provides a fast "bump" allocator for bulk memory allocations. All memory allocated within an arena is freed at once when the arena itself is destroyed or reset.

## Overview

- **Performance**: Allocations are extremely fast, involving only a single pointer increment.
- **Bulk Freeing**: Ideal for task-local or request-local allocations where everything can be freed at the same time.
- **Save/Restore**: Support for "checkpoints" to partially free memory within the arena.
- **RAII**: Implements the `Drop` trait to ensure the underlying buffer is freed automatically.

## Usage

```zc
import "std/arena.zc"

struct Node {
    val: int;
}

fn main() {
    // Create arena with 1KB capacity
    let a = Arena::new(1024);
    
    // Fast allocations
    let n1 = a.alloc<Node>();
    let n2 = a.alloc<Node>();
    
    // Duplicate string into arena memory
    let s = a.dup_str("Hello World");
    
    println "Arena used: {a.bytes_used()} bytes";
    
    // Everything is freed automatically when 'a' goes out of scope
}
```

## Struct Definition

```zc
struct Arena {
    data: void*;
    capacity: usize;
    used: usize;
}
```

## Methods

### Construction

| Method | Signature | Description |
| :--- | :--- | :--- |
| **new** | `Arena::new(cap: usize) -> Arena` | Creates a new arena with the specified capacity. |

### Allocation

| Method | Signature | Description |
| :--- | :--- | :--- |
| **alloc\<T>** | `alloc<T>(self) -> T*` | Allocates and zero-initializes memory for a type `T`. |
| **alloc_n\<T>**| `alloc_n<T>(self, count: usize) -> T*` | Allocates memory for an array of `count` elements of type `T`. |
| **alloc_bytes**| `alloc_bytes(self, size: usize) -> void*` | Raw byte allocation (aligned to 8 bytes). |
| **dup_str** | `dup_str(self, src: char*) -> char*` | Duplicates a C string into the arena. |

### Query & Control

| Method | Signature | Description |
| :--- | :--- | :--- |
| **bytes_used** | `bytes_used(self) -> usize` | Returns the total bytes currently allocated. |
| **bytes_free** | `bytes_free(self) -> usize` | Returns the remaining capacity. |
| **save** | `save(self) -> usize` | Returns a "checkpoint" representating current usage. |
| **restore** | `restore(self, mark: usize)` | Partially frees back to a previous checkpoint. |
| **reset** | `reset(self)` | Frees all allocations by resetting usage to zero (buffer is kept). |

## Memory Management

| Method | Signature | Description |
| :--- | :--- | :--- |
| **free** | `free(self)` | Explicitly frees the underlying arena buffer. |
| **Trait** | `impl Drop for Arena` | Automatically calls `free()` when the arena goes out of scope. |
