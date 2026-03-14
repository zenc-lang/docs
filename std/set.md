# std/set

`Set<T>` is a generic hash set implementation for storing unique values of type `T`. It uses an open-addressing hash table with linear probing.

## Overview

- **Generic**: Stores any type `T`.
- **Unique**: Automatically handles duplicates; adding an existing element returns `false`.
- **Fast**: O(1) average time complexity for additions, removals, and lookups.
- **RAII**: Implements the `Drop` trait for automatic memory management.

## Usage

```zc
import "std/set.zc"

fn main() {
    let s = Set<int>::new();
    
    s.add(10);
    s.add(20);
    s.add(10); // Duplicate, returns false
    
    if (s.contains(10)) {
        println "Set contains 10";
    }
    
    s.remove(20);
    println "Length: {s.length()}";
} // s is freed automatically here
```

## Struct Definition

```zc
struct Set<T> {
    data: T*;
    len: usize;
    cap: usize;
    // ... internal fields
}
```

## Methods

### Construction

| Method | Signature | Description |
| :--- | :--- | :--- |
| **new** | `Set<T>::new() -> Set<T>` | Creates a new, empty set. |

### Modification

| Method | Signature | Description |
| :--- | :--- | :--- |
| **add** | `add(self, val: T) -> bool` | Adds a value to the set. Returns `true` if added, `false` if already present. |
| **remove** | `remove(self, val: T) -> bool` | Removes a value from the set. Returns `true` if present and removed. |
| **clear** | `clear(self)` | Removes all elements from the set without freeing allocated memory. |

### Access & Query

| Method | Signature | Description |
| :--- | :--- | :--- |
| **contains** | `contains(self, val: T) -> bool` | Returns `true` if the value exists in the set. |
| **length** | `length(self) -> usize` | Returns the number of unique elements. |
| **is_empty** | `is_empty(self) -> bool` | Returns `true` if the set has no elements. |
| **capacity** | `capacity(self) -> usize` | Returns the current internal capacity. |

### Utility

| Method | Signature | Description |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Checks if a specific internal hash slot is occupied. |
| **val_at** | `val_at(self, idx: usize) -> Option<T>` | Returns the value at a specific internal slot, if any. |

## Memory Management

| Method | Signature | Description |
| :--- | :--- | :--- |
| **free** | `free(self)` | Manually frees the set's internal buffers. |
| **Trait** | `impl Drop for Set` | Automatically calls `free()` when the set goes out of scope. |
