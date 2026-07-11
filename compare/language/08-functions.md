+++
title = "Functions"
weight = 8
+++

# Functions

Function declaration, named arguments, default values,
const parameters, variadic functions, and function pointers.

## Zen C

```zc
import "std/io.zc"

fn greet(name: string, times: int = 1) {
    for _ in 0..times {
        println "Hello, {name}!";
    }
}

fn add(a: int, b: int) -> int {
    return a + b;
}

fn print_val(v: const int) {
    println "value: {v}";
}

fn log(fmt: char*, ...) {
    let ap: va_list;
    va_start(ap, fmt);
    print "[LOG] ";
    vprintf(fmt, ap);
    va_end(ap);
}

fn main() {
    greet("Zen");
    greet("World", times: 3);

    let result = add(10, 20);
    println "add: {result}";

    print_val(42);

    log("message: %s, code: %d\n", "test", 200);
}
```

## C

```c
#include <stdio.h>
#include <stdarg.h>

void greet(const char* name, int times) {
    for (int i = 0; i < times; i++) {
        printf("Hello, %s!\n", name);
    }
}

void greet_once(const char* name) {
    greet(name, 1);
}

int add(int a, int b) {
    return a + b;
}

void print_val(const int v) {
    printf("value: %d\n", v);
}

void log(const char* fmt, ...) {
    va_list args;
    printf("[LOG] ");
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
}

int main(void) {
    greet_once("C");
    greet("World", 3);

    int result = add(10, 20);
    printf("add: %d\n", result);

    print_val(42);

    log("message: %s, code: %d\n", "test", 200);
    return 0;
}
```

## Key Differences

- `fn add(a: int, b: int) -> int` vs `int add(int a, int b)`
- Named arguments: `add(b: 20, a: 10)` reorder calls
- Default arguments: `times: int = 1` (C needs manual overload/wrapper)
- `const` qualifier on params: `print_val(v: const int)`
- Variadic: `fn log(fmt: char*, ...)` uses `vprintf` internally
- `fn*` for raw C-compatible function pointers (no closures)
- C requires `stdarg.h` and `va_start`/`va_end` boilerplate

## Output

Hello, Zen!
Hello, World!
Hello, World!
Hello, World!
add: 30
value: 42
[LOG] message: test, code: 200
