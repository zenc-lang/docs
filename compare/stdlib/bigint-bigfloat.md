+++
title = "BigInt & BigFloat vs GMP"
weight = 49
+++

# BigInt & BigFloat vs GMP

Arbitrary-precision integer and floating-point arithmetic vs C GMP
(GNU Multiple Precision) library.

## Zen C

```zc
import "std/bigint.zc"
import "std/io.zc"

fn main() {
    let a = BigInt::from_int(123);
    let b = BigInt::from_int(456);

    let sum = a.add(&b);
    println "sum: {sum}";
}
```

## C (requires GMP: `-lgmp`)

```c
#include <stdio.h>
#include <gmp.h>

int main(void) {
    mpz_t a, b, sum;
    mpz_inits(a, b, sum, NULL);

    mpz_set_ui(a, 123);
    mpz_set_ui(b, 456);

    mpz_add(sum, a, b);
    gmp_printf("sum: %Zd\n", sum);

    mpz_clears(a, b, sum, NULL);
    return 0;
}
```

## Key Differences

- `BigInt` with `from_int` constructor
- `a.add(&b)` takes a reference to avoid move
- `BigFloat` for arbitrary-precision floating point
- C: GMP library, manual `mpz_init`/`mpz_clear`
- C: function calls instead of methods: `mpz_add(sum, a, b)`

## Output

sum: 579
