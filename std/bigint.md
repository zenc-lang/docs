# std/bigint

`BigInt` provides arbitrary-precision integer arithmetic for Zen-C. It allows for calculations with integers that exceed the capacity of standard numeric types like `u64`.

## Overview

- **Arbitrary Precision**: Numbers are limited only by available memory.
- **Decimal-based**: Currently uses a simple base-10 representation for simplicity.
- **RAII**: Implements the `Drop` trait for automatic memory management of internal digit storage.
- **Convenient**: Supports operator overloading for intuitive arithmetic.

## Usage

```zc
import "std/bigint.zc"

fn main() {
    let a = BigInt::from_int(1_000_000_000_000_000);
    let b = BigInt::from_int(2_000_000_000_000_000);
    
    // Uses operator overloading
    let sum = a + b; 
    
    let s = sum.to_string();
    println "Sum: {s}";
    free(s);
} // sum, a, and b are freed automatically here
```

## Struct Definition

```zc
struct BigInt {
    digits: Vec<u8>*;
}
```

## Methods

### Construction

| Method | Signature | Description |
| :--- | :--- | :--- |
| **new** | `BigInt::new() -> BigInt` | Creates a new `BigInt` initialized to 0. |
| **from_int** | `BigInt::from_int(val: u64) -> BigInt` | Creates a new `BigInt` from a 64-bit integer. |

### Modification

| Method | Signature | Description |
| :--- | :--- | :--- |
| **add_in_place** | `add_in_place(self, other: BigInt)` | Adds `other` to `self` by mutating the internal state. |

### Utility

| Method | Signature | Description |
| :--- | :--- | :--- |
| **clone** | `clone(self) -> BigInt` | Returns a deep copy of the `BigInt`. |
| **to_string** | `to_string(self) -> char*` | Returns a heap-allocated string representation. |

## Operators

| Operator | Method | Description |
| :--- | :--- | :--- |
| `+` | **add** | Returns a new `BigInt` containing the sum of two values. |
| `{}` | **to_string** | Automatically enables interpolation in formatted strings. |

## Memory Management

| Method | Signature | Description |
| :--- | :--- | :--- |
| **free_mem** | `free_mem(self)` | Manually frees the underlying `Vec` and `BigInt` storage. |
| **Trait** | `impl Drop for BigInt` | Automatically calls `free_mem()` when out of scope. |
