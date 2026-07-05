+++
title = "11. 并发 (Async/Await)"
weight = 11
+++

# 11. 并发 (Async/Await)


基于 pthreads 构建。

```zc
async fn fetch_data() -> string {
    // 在后台运行
    return "Data";
}

fn main() {
    let future = fetch_data();
    let result = await future;
}
```
