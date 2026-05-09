+++
title = "10. Generici"
weight = 10
+++

# 10. Generici


Template type-safe per struct e funzioni.

```zc
// Struct generico
struct Box<T> {
    item: T;
}

// Funzione generica
fn identity<T>(val: T) -> T {
    return val;
}

// Generici con parametri multipli
struct Pair<K, V> {
    key: K;
    value: V;
}
```
