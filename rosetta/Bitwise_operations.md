+++
title = "Bitwise operations"
+++

# Bitwise operations

Zen C inherits standard C bitwise operators but clarifies shift semantics through its strong type system. Furthermore, it provides a dedicated <code>std/bits.zc</code> standard library module to handle bit manipulations like rotations and population counts.

```zc
import "std/bits.zc"

fn main() {
    let a: u32 = 255;
    let b: u32 = 3;

    println "a AND b: {a & b}";
    println "a OR b: {a | b}";
    println "a XOR b: {a ^ b}";
    println "NOT a: {~a}";
    
    // Shifts
    println "Left shift (a << b): {a << b}";
    
    // Logical right shift comes natively when using unsigned types ('u32')
    println "Logical right shift (a >> b): {a >> b}";
    
    // Arithmetic right shift requires casting to a signed type to retain the sign bit
    let arithmetic_rs = ((i32)a) >> b;
    println "Arithmetic right shift: {arithmetic_rs}";
    
    let left_rot = Bits::rotl32(a, b);
    let right_rot = Bits::rotr32(a, b);
    println "Left rotate: {left_rot}";
    println "Right rotate: {right_rot}";
    
    // A little bonus.
    println "Population Count: {Bits::popcount32(a)}";
    println "Leading Zeros: {Bits::clz32(a)}";
    println "Trailing Zeros: {Bits::ctz32(a)}";
}
```

**Output:**

```
a AND b: 3
a OR b: 255
a XOR b: 252
NOT a: 4294967040
Left shift (a << b): 2040
Logical right shift (a >> b): 31
Arithmetic right shift: 31
Left rotate: 2040
Right rotate: 3758096415
Population Count: 8
Leading Zeros: 24
Trailing Zeros: 0
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Bitwise operations**](https://rosettacode.org/wiki/Bitwise_operations) in Zen C.

*This article uses material from the Rosetta Code article **Bitwise operations**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Bitwise_operations?action=history).*
