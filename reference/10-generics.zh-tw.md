+++
title = "10. 泛型"
weight = 10
+++

# 10. 泛型 {#10-fan-xing}


結構體和函數的類型安全模板。

```zc
// 泛型結構體
struct Box<T> {
    item: T;
}

// 泛型函數
fn identity<T>(val: T) -> T {
    return val;
}

// 多參數泛型
struct Pair<K, V> {
    key: K;
    value: V;
}
```
