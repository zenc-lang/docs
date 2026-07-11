+++
title = "Operators & Overloading"
weight = 13
+++

# Operators & Overloading

Built-in operators and custom operator implementations via trait methods.

## Zen C

```zc
import "std/io.zc"

struct Point {
    x: int;
    y: int;
}

impl Point {
    fn add(self, other: Point) -> Point {
        return Point { x: self.x + other.x, y: self.y + other.y };
    }

    fn eq(self, other: Point) -> bool {
        return self.x == other.x && self.y == other.y;
    }
}

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = Point { x: 3, y: 4 };
    let p3 = p1 + p2;

    println "p3: ({p3.x}, {p3.y})";
    println "p1 == p2: {p1 == p2}";
    let expected = Point { x: 4, y: 6 };
    println "p3 == expected: {p3 == expected}";
}
```

## C

```c
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int x;
    int y;
} Point;

Point point_add(Point a, Point b) {
    Point r = {a.x + b.x, a.y + b.y};
    return r;
}

bool point_eq(Point a, Point b) {
    return a.x == b.x && a.y == b.y;
}

int main(void) {
    Point p1 = {1, 2};
    Point p2 = {3, 4};
    Point p3 = point_add(p1, p2);

    printf("p3: (%d, %d)\n", p3.x, p3.y);
    printf("p1 == p2: %s\n", point_eq(p1, p2) ? "true" : "false");
    Point p4 = {4, 6};
    printf("p3 == Point { x: 4, y: 6 }: %s\n", point_eq(p3, p4) ? "true" : "false");
    return 0;
}
```

## Key Differences

- Operator overloading via trait methods: `add`, `sub`, `mul`, `div`, `eq`, `lt`, etc.
- Natural syntax: `p1 + p2` calls `p1.add(p2)`
- Index overloading: `a[i]` via `get`/`set`, `a[i, j]` for multi-dim
- C requires explicit function calls: `point_add(p1, p2)`
- Overloadable: arithmetic (`+ - * / % **`), comparison (`== != < > <= >=`), bitwise (`& | ^ << >>`), unary (`- ! ~`), index (`[]`)

## Output

p3: (4, 6)
p1 == p2: false
p3 == expected: true
