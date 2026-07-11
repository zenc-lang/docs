+++
title = "Guard & Unless"
weight = 12
+++

# Guard & Unless

Guard for early return on failed conditions, and `unless` as
inverted-if sugar.

## Zen C

```zc
import "std/io.zc"

fn process(ptr: int*) -> int {
    guard ptr != null else {
        println "null pointer, aborting";
        return -1;
    }
    return *ptr * 2;
}

fn validate(age: int) -> bool {
    guard age > 0 else { return false; }
    guard age < 150 else { return false; }
    return true;
}

fn show_status(active: bool) {
    unless active {
        println "inactive";
        return;
    }
    println "active and running";
}

fn main() {
    let x = 21;
    println "2x: {process(&x)}";

    println "age 25 valid: {validate(25)}";
    println "age -5 valid: {validate(-5)}";

    show_status(true);
    show_status(false);
}
```

## C

```c
#include <stdio.h>

int process(int* ptr) {
    if (ptr == NULL) {
        printf("null pointer, aborting\n");
        return -1;
    }
    return (*ptr) * 2;
}

int validate(int age) {
    if (age <= 0) return 0;
    if (age >= 150) return 0;
    return 1;
}

void show_status(int active) {
    if (!active) {
        printf("inactive\n");
        return;
    }
    printf("active and running\n");
}

int main(void) {
    int x = 21;
    printf("2x: %d\n", process(&x));

    printf("age 25 valid: %d\n", validate(25));
    printf("age -5 valid: %d\n", validate(-5));

    show_status(1);
    show_status(0);
    return 0;
}
```

## Key Differences

- `guard condition else { block }` runs block and must exit (return/break/continue)
- `guard` enforces early exit, preventing fallthrough bugs
- `unless condition { ... }` is syntactic sugar for `if !condition { ... }`
- C uses `if (!cond)` or `if (cond == NULL)` with manual returns
- Zen C `guard` ensures you cannot forget the exit statement
- Combined with `defer`, creates clean early-return-unwrap patterns

## Output

2x: 42
age 25 valid: true
age -5 valid: false
active and running
inactive
