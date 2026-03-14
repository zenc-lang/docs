# std/bits

The `std/bits` module provides low-level bitwise operations, including rotations, population counts, and bit reversals.

## Overview

- **Cross-platform**: Correctly implements bitwise operations across different architectures.
- **Efficient**: Uses optimized bit manipulation algorithms.
- **Comprehensive**: Supports 8, 16, 32, 64, and 128-bit unsigned integers.
- **Endianness Utilities**: Includes functions for reversing byte order (endianness swapping).

## Usage

```zc
import "std/bits.zc"

fn main() {
    let a: u32 = 0x80000001;
    
    // Rotate 32-bit integer left by 1
    let rotated = Bits::rotl32(a, 1); // 0x00000003
    
    // Count set bits (population count)
    let count = Bits::popcount32(0b1011); // 3
    
    // Reverse byte order (bswap)
    let swapped = Bits::bswap32(0x12345678); // 0x78563412
}
```

## Methods

### Bitwise Rotation

| Method | Signature | Description |
| :--- | :--- | :--- |
| **rotl[N]** | `Bits::rotl[N](n: u[N], c: u[N]) -> u[N]` | Rotates `n` left by `c` bits (N=8, 16, 32, 64, 128). |
| **rotr[N]** | `Bits::rotr[N](n: u[N], c: u[N]) -> u[N]` | Rotates `n` right by `c` bits (N=8, 16, 32, 64, 128). |

### Population Count

| Method | Signature | Description |
| :--- | :--- | :--- |
| **popcount[N]** | `Bits::popcount[N](n: u[N]) -> u[N]` | Returns the number of set bits (1s) in `n` (N=8, 16, 32, 64, 128). |

### Count Leading/Trailing Zeros

| Method | Signature | Description |
| :--- | :--- | :--- |
| **clz[N]** | `Bits::clz[N](n: u[N]) -> u[N]` | Returns the number of leading zero bits (N=8, 16, 32, 64, 128). |
| **ctz[N]** | `Bits::ctz[N](n: u[N]) -> u[N]` | Returns the number of trailing zero bits (N=8, 16, 32, 64, 128). |

### Byte Swap & Bit Reversal

| Method | Signature | Description |
| :--- | :--- | :--- |
| **bswap[N]** | `Bits::bswap[N](n: u[N]) -> u[N]` | Reverses the byte order of `n` (N=16, 32, 64, 128). |
| **reverse_bits[N]** | `Bits::reverse_bits[N](n: u[N]) -> u[N]` | Reverses the bit order of `n` (N=8, 16, 32, 64, 128). |
