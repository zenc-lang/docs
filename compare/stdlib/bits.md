+++
title = "Bits vs Manual Bit Ops"
weight = 51
+++

# Bits vs Manual Bit Operations

Built-in rotate and bit manipulation functions vs C manual
shift-and-mask patterns.

## Zen C

```zc
import "std/bits.zc"
import "std/io.zc"

fn main() {
    let x: u32 = 0x80000001;

    let left = bits::rotl32(x, 1);
    println "rotl(0x{x:08x}, 1) = 0x{left:08x}";

    let right = bits::rotr32(x, 1);
    println "rotr(0x{x:08x}, 1) = 0x{right:08x}";
}
```

## C

```c
#include <stdio.h>
#include <stdint.h>

uint32_t rotl32(uint32_t x, int n) {
    return (x << n) | (x >> (32 - n));
}

uint32_t rotr32(uint32_t x, int n) {
    return (x >> n) | (x << (32 - n));
}

int main(void) {
    uint32_t x = 0x80000001;

    uint32_t left = rotl32(x, 1);
    printf("rotl(0x%08x, 1) = 0x%08x\n", x, left);

    uint32_t right = rotr32(x, 1);
    printf("rotr(0x%08x, 1) = 0x%08x\n", x, right);
    return 0;
}
```

## Key Differences

- `bits::rotl32`, `bits::rotr32` etc. for type-specific bit rotation
- `bits::rotl8`, `bits::rotl16`, `bits::rotl64` for different widths
- C: manual `(x << n) | (x >> (32 - n))` pattern

## Output

rotl(0x80000001, 1) = 0x00000003
rotr(0x80000001, 1) = 0xc0000000
