+++
title = "Pattern Matching"
weight = 11
+++

# Pattern Matching

Exhaustive match on literals, ranges, enums, and destructuring with
reference binding.

## Zen C

```zc
import "std/io.zc"

enum Color { Red, Green, Blue }

fn color_name(c: Color) -> string {
    match c {
        Color::Red => { return "red"; },
        Color::Green => { return "green"; },
        Color::Blue => { return "blue"; },
    }
}

fn describe(n: int) -> string {
    match n {
        0 => { return "zero"; },
        1 || 2 || 3 => { return "small"; },
        4..10 => { return "medium"; },
        11..=100 => { return "large"; },
        _ => { return "out of range"; },
    }
}

fn main() {
    println "color: {color_name(Color::Red)}";
    println "color: {color_name(Color::Green)}";

    println "1: {describe(1)}";
    println "5: {describe(5)}";
    println "50: {describe(50)}";
    println "200: {describe(200)}";
}
```

## C

```c
#include <stdio.h>

typedef enum { COLOR_RED, COLOR_GREEN, COLOR_BLUE } Color;

const char* color_name(Color c) {
    switch (c) {
        case COLOR_RED:   return "red";
        case COLOR_GREEN: return "green";
        case COLOR_BLUE:  return "blue";
        default:          return "unknown";
    }
}

const char* describe(int n) {
    if (n == 0) return "zero";
    else if (n >= 1 && n <= 3) return "small";
    else if (n >= 4 && n <= 10) return "medium";
    else if (n >= 11 && n <= 100) return "large";
    else return "out of range";
}

int main(void) {
    printf("color: %s\n", color_name(COLOR_RED));
    printf("color: %s\n", color_name(COLOR_GREEN));

    printf("1: %s\n", describe(1));
    printf("5: %s\n", describe(5));
    printf("50: %s\n", describe(50));
    printf("200: %s\n", describe(200));
    return 0;
}
```

## Key Differences

- `match` is exhaustive: all enum variants or a `_` wildcard required
- Multiple patterns: `1 || 2 || 3` or `1, 2, 3`
- Range patterns: `4..10` (exclusive), `11..=100` (inclusive)
- Enum destructuring with data: `Circle(r) => ...`
- Reference binding: `Some(ref x) => ...` to inspect without moving
- C `switch` only works on integers; no range support, no destructuring
- C pattern matching uses `if`/`else` chains or `switch` with fallthrough

## Output

color: red
color: green
1: small
5: medium
50: large
200: out of range
