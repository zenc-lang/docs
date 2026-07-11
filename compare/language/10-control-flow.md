+++
title = "Control Flow"
weight = 10
+++

# Control Flow

Conditionals, loops, if-expressions, and range-based iteration.

## Zen C

```zc
import "std/io.zc"

fn classify(x: int) -> string {
    if x > 100 {
        return "huge";
    } else if x > 10 {
        return "medium";
    } else {
        return "small";
    }
}

fn main() {
    println "--- while loop ---";
    let i = 0;
    while i < 3 {
        println "i: {i}";
        i += 1;
    }

    println "--- for range ---";
    for n in 0..5 {
        println "n: {n}";
    }

    println "--- inclusive range ---";
    for n in 0..=3 {
        println "n: {n}";
    }

    println "--- step ---";
    for n in 0..10 step 2 {
        println "n: {n}";
    }

    println "--- do-while ---";
    let j = 0;
    do {
        println "j: {j}";
        j += 1;
    } while j < 2;

    println "--- classify ---";
    println "50: {classify(50)}";
    println "200: {classify(200)}";
}
```

## C

```c
#include <stdio.h>

const char* classify(int x) {
    if (x > 100) return "huge";
    else if (x > 10) return "medium";
    else return "small";
}

int main(void) {
    printf("--- while loop ---\n");
    int i = 0;
    while (i < 3) {
        printf("i: %d\n", i);
        i++;
    }

    printf("--- for range ---\n");
    for (int n = 0; n < 5; n++) {
        printf("n: %d\n", n);
    }

    printf("--- inclusive range ---\n");
    for (int n = 0; n <= 3; n++) {
        printf("n: %d\n", n);
    }

    printf("--- step ---\n");
    for (int n = 0; n < 10; n += 2) {
        printf("n: %d\n", n);
    }

    printf("--- do-while ---\n");
    int j = 0;
    do {
        printf("j: %d\n", j);
        j++;
    } while (j < 2);

    printf("--- classify ---\n");
    printf("50: %s\n", classify(50));
    printf("200: %s\n", classify(200));
    return 0;
}
```

## Key Differences

- `if` expression returns a value: `let x = if (...) { ... } else { ... }`
- Ranges: `0..5` (exclusive), `0..=5` (inclusive), `0..<5` (explicit exclusive)
- Range step: `0..10 step 2`
- Iterator loops: `for item in vec` on any Iterable type
- Enumerated: `for i, val in arr`
- C needs manual bounds with `i = 0; i < N; i++`

## Output

--- while loop ---
i: 0
i: 1
i: 2
--- for range ---
n: 0
n: 1
n: 2
n: 3
n: 4
--- inclusive range ---
n: 0
n: 1
n: 2
n: 3
--- step ---
n: 0
n: 2
n: 4
n: 6
n: 8
--- do-while ---
j: 0
j: 1
--- classify ---
50: medium
200: huge
