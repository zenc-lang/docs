+++
title = "Arena & Mman vs Custom Allocators"
weight = 54
+++

# Arena & Mman vs Custom Allocators

Arena allocators and memory mapping vs C custom arena implementations
and mmap.

## Zen C

```zc
import "std/io.zc"

fn main() {
    let a = malloc(4096);
    defer free(a);

    let x: int* = a;
    *x = 42;

    let buf: char* = a + 8;
    strcpy(buf, "Hello from arena");

    println "x: {*x}";
    println "buf: {buf}";
}
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* memory;
    size_t cap;
    size_t offset;
} Arena;

Arena arena_new(size_t size) {
    Arena a = {malloc(size), size, 0};
    return a;
}

void* arena_alloc(Arena* a, size_t size) {
    if (a->offset + size > a->cap) return NULL;
    void* ptr = a->memory + a->offset;
    a->offset += size;
    return ptr;
}

void arena_free_all(Arena* a) {
    free(a->memory);
    a->memory = NULL;
    a->cap = a->offset = 0;
}

int main(void) {
    Arena a = arena_new(4096);

    int* x = arena_alloc(&a, sizeof(int));
    *x = 42;

    char* buf = arena_alloc(&a, 256);
    strcpy(buf, "Hello from arena");

    printf("x: %d\n", *x);
    printf("buf: %s\n", buf);

    arena_free_all(&a);
    return 0;
}
```

## Key Differences

- Arena allocation: bump pointer allocation within a pre-allocated block
- `defer free(a)` for automatic cleanup at scope exit
- `arena::new(size)` / `arena::alloc(a, size)` / `arena::free_all(a)` in stdlib
- `mman::map` for memory-mapped files and anonymous regions
- C: manual bump allocator, `mmap`/`munmap` with manual flags

## Output

x: 42
buf: Hello from arena
