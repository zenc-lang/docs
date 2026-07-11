+++
title = "Stack & Queue vs Custom LIFO/FIFO"
weight = 48
+++

# Stack & Queue vs Custom LIFO/FIFO

Stack (LIFO) and Queue (FIFO) vs C custom implementations.

## Zen C

```zc
import "std/stack.zc"
import "std/io.zc"

fn main() {
    let s: Stack<int> = Stack::new();
    s.push(1);
    s.push(2);
    s.push(3);

    println "stack size: {s.len}";
}
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct { int* data; size_t len; size_t cap; } Stack;

void stack_push(Stack* s, int v) {
    if (s->len >= s->cap) { s->cap = s->cap ? s->cap * 2 : 4; s->data = realloc(s->data, s->cap * sizeof(int)); }
    s->data[s->len++] = v;
}

int main(void) {
    Stack s = {NULL, 0, 0};
    stack_push(&s, 1); stack_push(&s, 2); stack_push(&s, 3);
    printf("stack size: %zu\n", s.len);
    free(s.data);
    return 0;
}
```

## Key Differences

- `Stack<T>` with `push(val)`, `pop()`, `peek()` -> `Option<T>`
- `Queue<T>` with `enqueue(val)`, `dequeue()` -> `Option<T>`
- Generic: works with any type
- C: manual array-based implementations

## Output

stack size: 3
