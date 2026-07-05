+++
title = "10. Generische Typen"
weight = 10
+++

# 10. Generische Typen {#10-generische-typen}


Typ-sichere Templates für Structs und Funktionen.

```zc
// Generisches Struct
struct Box<T> {
    item: T;
}

// Generische Funktion
fn identity<T>(val: T) -> T {
    return val;
}

// Mehrere Typ-Parameter
struct Pair<K, V> {
    key: K;
    value: V;
}
```
