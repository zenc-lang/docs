+++
title = "Memory Management"
weight = 17
+++

# Memory Management

Resource semantics with move-by-default, Copy, Clone, and Drop
(RAII) traits.

## Zen C

```zc
import "std/io.zc"

struct Buffer {
    data: char*;
    size: usize;
}

impl Drop for Buffer {
    fn drop(self) {
        free(self.data);
    }
}

impl Clone for Buffer {
    fn clone(self) -> Buffer {
        let new_data = malloc(self.size);
        memcpy(new_data, self.data, self.size);
        return Buffer { data: new_data, size: self.size };
    }
}

fn process_buf(b: Buffer) {
    println "processing buffer of size {b.size}";
}

fn main() {
    let buf1 = Buffer { data: malloc(64), size: 64 };
    println "buf1 size: {buf1.size}";

    let buf2 = buf1.clone();
    println "cloned size: {buf2.size}";

    process_buf(buf2);
    println "buf2 moved into process_buf";
}
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* data;
    size_t size;
} Buffer;

Buffer buffer_clone(Buffer b) {
    char* new_data = malloc(b.size);
    memcpy(new_data, b.data, b.size);
    Buffer r = {new_data, b.size};
    return r;
}

void buffer_free(Buffer* b) {
    free(b->data);
}

void process_buf(Buffer b) {
    printf("processing buffer of size %zu\n", b.size);
    buffer_free(&b);
}

int main(void) {
    Buffer buf1 = {malloc(64), 64};
    printf("buf1 size: %zu\n", buf1.size);

    Buffer buf2 = buffer_clone(buf1);
    printf("cloned size: %zu\n", buf2.size);

    process_buf(buf2);
    printf("buf2 freed in process_buf\n");

    buffer_free(&buf1);
    return 0;
}
```

## Key Differences

- Move-by-default: assigning a resource variable transfers ownership
- Original variable becomes invalid after move (compile-time error to use it)
- `Clone` trait: explicit duplication via `a.clone()`
- `Copy` trait: marker for implicit duplication (value types)
- `Drop` trait: RAII cleanup called automatically when variable leaves scope
- C requires manual `free()`, manual tracking of ownership
- C has no protection against double-free or use-after-move
- "use of moved value" is a compile-time error in Zen C

## Output

buf1 size: 64
cloned size: 64
processing buffer of size 64
buf2 moved into process_buf
