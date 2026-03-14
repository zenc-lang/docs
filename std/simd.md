# std/simd

Zen-C provides native SIMD (Single Instruction, Multiple Data) vector types that compile directly to hardware-optimized vector instructions (SSE, AVX, NEON, etc.) supported by the target backend.

## Overview

- **Native Performance**: Leverages LLVM/GCC vector extensions for maximum efficiency.
- **Implicitly Portable**: Types like `f32x4` map to the best available 128-bit hardware specific to the architecture.
- **Element-wise arithmetic**: Standard operators (`+`, `-`, `*`, `/`) apply to all lanes simultaneously.
- **Broadcasting**: Initializing with a single value broadcasts it to all lanes.

## Usage

```zc
import "std/simd.zc"

fn main() {
    // Initialization (Explicit lanes)
    let a = f32x4 { 1.0, 2.0, 3.0, 4.0 };
    
    // Broadcasting (Single value to all lanes)
    let b = f32x4 { v: 2.0 };
    
    // Element-wise addition
    let c = a + b;   // Result: { 3.0, 4.0, 5.0, 6.0 }
    
    // Lane Access
    let first = c[0];
}
```

## Vector Types

The standard library defines several 128-bit and 256-bit vector types. You can also define custom ones using the `@vector(N)` attribute.

### 128-bit Vectors (SSE / NEON)

| Type | Element Type | Lanes | Byte Size |
| :--- | :--- | :--- | :--- |
| `f32x4` | `f32` | 4 | 16 |
| `f64x2` | `f64` | 2 | 16 |
| `i32x4` | `i32` | 4 | 16 |
| `u32x4` | `u32` | 4 | 16 |
| `i64x2` | `i64` | 2 | 16 |
| `u64x2` | `u64` | 2 | 16 |
| `i16x8` | `i16` | 8 | 16 |
| `u16x8` | `u16` | 8 | 16 |
| `i8x16` | `i8` | 16 | 16 |
| `u8x16` | `u8` | 16 | 16 |

### 256-bit Vectors (AVX / AVX2)

| Type | Element Type | Lanes | Byte Size |
| :--- | :--- | :--- | :--- |
| `f32x8` | `f32` | 8 | 32 |
| `f64x4` | `f64` | 4 | 32 |
| `i32x8` | `i32` | 8 | 32 |
| `u32x8` | `u32` | 8 | 32 |
| `i64x4` | `i64` | 4 | 32 |
| `u64x4` | `u64` | 4 | 32 |
| `i16x16` | `i16` | 16 | 32 |
| `u16x16` | `u16` | 16 | 32 |
| `i8x32` | `i8` | 32 | 32 |
| `u8x32` | `u8` | 32 | 32 |

## Operations

| Category | Operator | Description |
| :--- | :--- | :--- |
| **Arithmetic** | `+`, `-`, `*`, `/` | Standard element-wise addition, subtraction, multiplication, and division. |
| **Bitwise** | `&`, `\|`, `^`, `~` | Bitwise AND, OR, XOR, and NOT across all lanes. |
| **Indexing** | `[i]` | Access or modify individual lanes by index. |
| **Comparison** | `==`, `!=`, `<`, `>` | Returns a boolean mask vector (results vary by backend). |
