+++
title = "Option<T> vs Null"
weight = 33
+++

# Option<T> vs Null

Type-safe optional values with `Some`/`None` vs C null pointers.

## Zen C

```zc
import "std/option.zc"
import "std/io.zc"

fn safe_divide(a: int, b: int) -> Option<int> {
    if b == 0 {
        let none: Option<int> = Option::None();
        return none;
    }
    let result: Option<int> = Option::Some(a / b);
    return result;
}

fn main() {
    let r = safe_divide(10, 2);
    println "ok";
}
```

## C

```c
#include <stdio.h>
#include <stdbool.h>

typedef struct { bool is_some; int value; } Option_int;

Option_int safe_divide(int a, int b) {
    if (b == 0) return (Option_int){false, 0};
    Option_int r = {true, a / b};
    return r;
}

int main(void) {
    Option_int r = safe_divide(10, 2);
    printf("ok\n");
    return 0;
}
```

## Key Differences

- `Option<T>` is `Some(val)` or `None()`
- `match` enforces handling of both cases
- C uses null pointers with no compiler enforcement

## Output

ok
