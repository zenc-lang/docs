+++
title = "11. Concorrência (Async/Await)"
weight = 11
+++

# 11. Concorrência (Async/Await)


Construído sobre pthreads.

```zc
async fn fetch_data() -> string {
    // Executa em background
    return "Data";
}

fn main() {
    let future = fetch_data();
    let result = await future;
}
```
