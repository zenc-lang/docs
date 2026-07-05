+++
title = "10. 泛型"
weight = 10
+++

# 10. 泛型 {#10-fan-xing}


结构体和函数的类型安全模板。

```zc
// 泛型结构体
struct Box<T> {
    item: T;
}

// 泛型函数
fn identity<T>(val: T) -> T {
    return val;
}

// 多参数泛型
struct Pair<K, V> {
    key: K;
    value: V;
}
```
