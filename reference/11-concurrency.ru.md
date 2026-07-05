+++
title = "11. Параллелизм (Async/Await)"
weight = 11
+++

# 11. Параллелизм (Async/Await)


Встроен на основе pthreads.

```zc
async fn fetch_data() -> string {
    // Запускается в фоне
    return "Data";
}

fn main() {
    let future = fetch_data();
    let result = await future;
}
```
