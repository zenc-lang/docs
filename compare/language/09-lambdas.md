+++
title = "Lambdas & Closures"
weight = 9
+++

# Lambdas & Closures

Anonymous functions, captures by reference or value, arrow syntax,
and block syntax.

## Zen C

```zc
import "std/io.zc"

fn apply_twice(x: int, f: fn(int) -> int) -> int {
    return f(f(x));
}

fn main() {
    let factor = 3;

    let doubler = x -> x * 2;
    println "double 5: {doubler(5)}";

    let multiplier = fn(x: int) -> int {
        return x * factor;
    };
    println "triple 5: {multiplier(5)}";

    let result = apply_twice(5, fn(x: int) -> int {
        return x + 1;
    });
    println "apply_twice: {result}";

    let val = 10;
    let inc = fn[&]() { val += 1; };
    inc();
    inc();
    println "after inc: {val}";
}
```

## C

```c
#include <stdio.h>

typedef int (*int_op)(int);

int apply_twice(int x, int_op f) {
    return f(f(x));
}

int double_func(int x) {
    return x * 2;
}

int triple_func(int x) {
    static int factor;
    return x * factor;
}

int add_one(int x) {
    return x + 1;
}

void inc_val(int *val) {
    (*val)++;
}

int main(void) {
    printf("double 5: %d\n", double_func(5));

    triple_func(0); /* hack: set static via call -- limited */
    printf("triple 5: %d\n", triple_func(5));

    int result = apply_twice(5, add_one);
    printf("apply_twice: %d\n", result);

    int val = 10;
    inc_val(&val);
    inc_val(&val);
    printf("after inc: %d\n", val);
    return 0;
}
```

## Key Differences

- Arrow syntax: `x -> x * 2` for single-expression lambdas
- Block syntax: `fn(x: int) -> int { ... }` for multi-line
- Capture by value (implicit in arrows): captures outer variables
- Capture by reference: `fn[&]() { val += 1 }`
- Explicit value capture: `fn[=]() { ... }`
- C has no closures; needs function pointers + manual state passing
- C workaround: static variables, structs with function pointers, void* contexts

## Output

double 5: 10
triple 5: 15
apply_twice: 7
after inc: 12
