+++
title = "11. 並發 (Async/Await)"
weight = 11
+++

# 11. 並發 (Async/Await)


基於 pthreads 構建。

```zc
async fn fetch_data() -> string {
    // 在後台運行
    return "Data";
}

fn main() {
    let future = fetch_data();
    let result = await future;
}
```
