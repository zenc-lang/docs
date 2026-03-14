# std/slice

`Slice<T>` is a lightweight, non-owning "view" into a contiguous sequence of elements. It is primarily used to provide a safe and convenient interface for working with fixed-size arrays.

## Overview

- **Non-owning**: Slices do not copy or own the underlying data; they merely point to it.
- **Iteration Support**: Implements the `iterator()` method, allowing slices to be used directly in `for-in` loops.
- **Automatic Conversion**: The Zen-C compiler automatically converts fixed-size arrays to slices when performing iteration or passing to slice-expecting functions.
- **Safe Access**: Provides bounds-checked `get()` and `at()` methods returning `Option<T>`.

## Usage

```zc
import "std/slice.zc"

fn main() {
    let arr: int[5] = [10, 20, 30, 40, 50];
    
    // Explicit slice creation
    let s = Slice<int>::from_array(arr, 5);
    
    // Direct iteration over the slice
    for val in s {
        println "{val}";
    }
    
    // Directly iterating over the array (auto-imports std/slice.zc)
    for val in arr {
        println "{val}";
    }
}
```

## Struct Definition

```zc
struct Slice<T> {
    data: T*;
    len: usize;
}
```

## Methods

### Construction

| Method | Signature | Description |
| :--- | :--- | :--- |
| **from_array** | `Slice<T>::from_array(ptr: T*, len: usize) -> Slice<T>` | Creates a slice view over an array pointer. |
| **new** | `Slice<T>::new(data: T*, len: usize) -> Slice<T>` | Alias for `from_array`. |

### Iteration

| Method | Signature | Description |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> SliceIter<T>` | Returns an iterator for use in `for-in` loops. |

### Access & Query

| Method | Signature | Description |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Returns the number of elements in the slice. |
| **is_empty** | `is_empty(self) -> bool` | Returns `true` if the slice contains no elements. |
| **get** | `get(self, idx: usize) -> Option<T>` | Returns the element at `idx`, or `None` if out of bounds. |
| **at** | `at(self, idx: usize) -> Option<T>` | Alias for `get`. |

## Notes

- **Auto-import**: `std/slice.zc` is automatically imported by the compiler when performing `for-in` iteration on fixed-size arrays.
- **Safety**: While `data` is a raw pointer, the `Slice` struct encourages using the length-aware `get()` method for safe access.
