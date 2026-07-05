+++
title = "11. Concurrency (Async/Await)"
weight = 11
+++

# 11. Concurrency (Async/Await)


Built on pthreads.

```zc
async fn fetch_data() -> string {
    // Runs in background
    return "Data";
}

fn main() {
    let future = fetch_data();
    let result = await future;
}
```
