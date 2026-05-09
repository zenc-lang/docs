+++
title = "11. 并发 (Async/Await)"
weight = 11
+++


# 11. 并发 (Async/Await)

Zen C 使用**无栈协程**模型实现 async/await — 无需线程池，无需 pthread 依赖。

```zc
async fn fetch_data() -> string {
    return "数据";
}

fn main() {
    let result = await fetch_data();
}
```

### 工作原理

`async fn` 会被编译器转换为一个**状态机**。每个
`await` 点成为一个状态转换。生成的 `Future` 结构体
包含状态、参数以及被等待调用的子 Future。

### 顺序模式

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
