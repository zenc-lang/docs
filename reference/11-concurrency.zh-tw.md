+++
title = "11. 並發 (Async/Await)"
weight = 11
+++


# 11. 並發 (Async/Await)

Zen C 使用**無棧協程**模型實現 async/await — 無需執行緒池，無需 pthread 依賴。

```zc
async fn fetch_data() -> string {
    return "資料";
}

fn main() {
    let result = await fetch_data();
}
```

### 工作原理

`async fn` 會被編譯器轉換為一個**狀態機**。每個
`await` 點成為一個狀態轉換。生成的 `Future` 結構體
包含狀態、參數以及被等待呼叫的子 Future。

### 順序模式

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
