+++
title = "Tuples"
weight = 5
+++

# Tuples, Multiple Returns & Destructuring

Group multiple values into a single compound value, return
multiple values from functions, and destructure into variables.

## Zen C

```zc
import "std/io.zc"

fn divide(a: int, b: int) -> (int, int) {
    return (a / b, a % b);
}

fn compute(a: int, b: int) -> (int, int, int) {
    return (a + b, a - b, a * b);
}

fn main() {
    let pair: (int, string) = (42, "Zen");
    println "pair: {pair.0}, {pair.1}";

    let (q, r) = divide(10, 3);
    println "quotient: {q}, remainder: {r}";

    let (sum: int, diff, prod) = compute(10, 3);
    println "sum: {sum}, diff: {diff}, prod: {prod}";
}
```

## C

```c
#include <stdio.h>

typedef struct {
    int quotient;
    int remainder;
} DivResult;

typedef struct {
    int sum;
    int diff;
    int prod;
} ComputeResult;

DivResult divide(int a, int b) {
    DivResult r = {a / b, a % b};
    return r;
}

ComputeResult compute(int a, int b) {
    ComputeResult r = {a + b, a - b, a * b};
    return r;
}

int main(void) {
    int pair_val = 42;
    const char* pair_str = "C";
    printf("pair: %d, %s\n", pair_val, pair_str);

    DivResult dr = divide(10, 3);
    printf("quotient: %d, remainder: %d\n", dr.quotient, dr.remainder);

    ComputeResult cr = compute(10, 3);
    printf("sum: %d, diff: %d, prod: %d\n", cr.sum, cr.diff, cr.prod);
    return 0;
}
```

## Key Differences

- Zen C tuples are anonymous: `(int, string)` vs C structs requiring names
- Multiple return values via tuples: `fn f() -> (int, int)`
- C needs named structs or output parameters for multiple returns
- Tuple destructuring: `let (q, r) = divide(10, 3)`
- Typed destructuring: `let (sum: int, diff, prod) = ...`
- Indexed access: `pair.0`, `pair.1` (zero-based)

## Output

pair: 42, Zen
quotient: 3, remainder: 1
sum: 13, diff: 7, prod: 30
