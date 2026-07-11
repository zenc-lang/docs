+++
title = "Iter vs Manual Iteration"
weight = 37
+++

# Iter vs Manual Iteration

Iterator-based traversal with `for-in` loops vs C manual loops
with indices or pointer arithmetic.

## Zen C

```zc
import "std/vec.zc"
import "std/io.zc"

fn main() {
    let v: Vec<int> = Vec::new();
    v.push(1);
    v.push(2);
    v.push(3);

    for val in v {
        println "value: {val}";
    }

    for i, val in v {
        println "[{i}]: {val}";
    }
}
```

## C

```c
#include <stdio.h>

int main(void) {
    int arr[] = {1, 2, 3};
    size_t len = sizeof(arr) / sizeof(arr[0]);

    for (size_t i = 0; i < len; i++)
        printf("value: %d\n", arr[i]);

    for (size_t i = 0; i < len; i++)
        printf("[%zu]: %d\n", i, arr[i]);
    return 0;
}
```

## Key Differences

- `for val in iterable` works on any type implementing `Iterable`
- `for i, val in iterable` gives index + value (enumerated iteration)
- Custom iterators via `impl Iterable<T>` with `next() -> Option<T>`
- `map`, `filter`, `fold` patterns via iterator combinators
- C: manual loops with `i < len` bounds checking
- C: no standard iterator protocol
- C: `qsort`, `bsearch` use function pointers for custom iteration

## Output

value: 1
value: 2
value: 3
[0]: 1
[1]: 2
[2]: 3
