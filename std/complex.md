# std/complex

The `std/complex` library provides the `Complex` struct and essential mathematical operations for working with complex numbers in Zen-C.

## Overview

- **Value Type**: Simple struct with `real` and `imag` components.
- **Operator support**: Supports `+`, `-`, `*`, `/`, `==`, and `!=` via operator overloading.
- **Properties**: Provides methods for calculating magnitude and phase.
- **Interpolation**: Can be directly used in f-strings and print statements.

## Usage

```zc
import "std/complex.zc"

fn main() {
    let c1 = Complex::new(3.0, 4.0);
    let c2 = Complex::new(1.0, 2.0);
    
    let sum = c1 + c2;
    let prod = c1 * c2;
    
    println "Sum: {sum}";       // Sum: 4.000000 + 6.000000i
    println "Magnitude: {c1.magnitude()}";
}
```

## Struct Definition

```zc
struct Complex {
    real: double;
    imag: double;
}
```

## Methods

### Construction

| Method | Signature | Description |
| :--- | :--- | :--- |
| **new** | `Complex::new(r: double, i: double) -> Complex` | Creates a new complex number with real component `r` and imaginary component `i`. |

### Access & Query

| Method | Signature | Description |
| :--- | :--- | :--- |
| **magnitude** | `magnitude(self) -> double` | Returns the magnitude (absolute value) of the complex number. |
| **phase** | `phase(self) -> double` | Returns the phase (angle) in radians. |

## Operators

| Operator | Method | Description |
| :--- | :--- | :--- |
| `+` | **add** | Adds two complex numbers. |
| `-` | **sub** | Subtracts one complex number from another. |
| `*` | **mul** | Multiplies two complex numbers. |
| `/` | **div** | Divides one complex number by another. |
| `==` | **eq** | Checks if two complex numbers are strictly equal. |
| `!=` | **neq** | Checks if two complex numbers are not equal. |
| `{}` | **to_string** | Enables direct string interpolation. |
