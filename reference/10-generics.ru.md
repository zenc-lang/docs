+++
title = "10. Обобщения"
weight = 10
+++

# 10. Обобщения {#10-obobshcheniia}


Типобезопасные шаблоны для структур и функций.

```zc
// Обобщённая структура
struct Box<T> {
    item: T;
}

// Обобщённая функция
fn identity<T>(val: T) -> T {
    return val;
}

// Обобщения с несколькими параметрами
struct Pair<K, V> {
    key: K;
    value: V;
}
```
