+++
title = "Generics"
weight = 21
+++

# Generics

Generic structs, generic functions, and type constraints for
type-safe reusable code.

## Zen C

```zc
import "std/io.zc"

fn swap(a: int*, b: int*) {
    let temp = *a;
    *a = *b;
    *b = temp;
}

fn main() {
    let x = 1;
    let y = 2;
    swap(&x, &y);
    println "swapped: x={x}, y={y}";
}
```

## C

```c
#include <stdio.h>

void swap_int(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 1, y = 2;
    swap_int(&x, &y);
    printf("swapped: x=%d, y=%d\n", x, y);
    return 0;
}
```

## Key Differences

- Generic functions via type parameters: `fn swap<T>(a: T*, b: T*)`
- Zen C generics are type-safe; C uses `void*` or duplicate functions per type
- `struct Pair<T, U>` for multi-parameter generic types
- C alternatives: `void*` + casting, `_Generic`, or code duplication

## Output

swapped: x=2, y=1
