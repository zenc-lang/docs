+++
title = "11. Concurrency (Async/Await)"
weight = 11
+++

# 11. Concurrency (Async/Await)


Zen C uses a **stackless coroutine** model for async/await — no thread pool, no pthread dependency.

```zc
async fn fetch_data() -> string {
    return "Data";
}

fn main() {
    let result = await fetch_data();
}
```

### How it works

An `async fn` is transformed by the compiler into a **state machine**. Each `await`
point becomes a state transition. The resulting `Future` struct holds the state,
parameters, and sub-futures for awaited calls.

### Sequential pattern

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
