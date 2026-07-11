+++
title = "Syntactic Sugar"
weight = 14
+++

# Syntactic Sugar

Pipe forward, null coalescing, safe navigation, try operator,
and auto-dereference.

## Zen C

```zc
import "std/io.zc"

fn square(x: int) -> int { return x * x; }
fn add_one(x: int) -> int { return x + 1; }

fn main() {
    let result = 5 |> square |> add_one;
    println "5 |> square |> add_one: {result}";
}
```

## C

```c
#include <stdio.h>

int square(int x) { return x * x; }
int add_one(int x) { return x + 1; }

int main(void) {
    int result = add_one(square(5));
    printf("5 |> square |> add_one: %d\n", result);

    int* maybe = NULL;
    int val = maybe ? *maybe : 42;
    printf("null ?? 42: %d\n", val);

    int r = 42;
    int* p = &r;
    printf("auto-deref: %d\n", *p);
    return 0;
}
```

## Key Differences

- Pipe `|>`: `x |> f(y)` becomes `f(x, y)`, readable left-to-right
- Null coalescing `??`: `val ?? default` for pointers
- Null assign `??=`: `val ??= init` sets only if null
- Safe navigation `?.`: `ptr?.field` returns null if ptr is null
- Try operator `?`: `res?` unwraps Result or returns error
- Auto-dereference: `ptr.field` works on pointers (no `->` needed)
- C needs nested function calls, ternary operators, explicit `*`/`->`

## Output

5 |> square |> add_one: 26
