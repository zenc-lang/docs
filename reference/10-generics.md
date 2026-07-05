+++
title = "10. Generics"
weight = 10
+++

# 10. Generics {#10-generics}


Type-safe templates for Structs and Functions.

```zc
// Generic Struct
struct Box<T> {
    item: T;
}

// Generic Function
fn identity<T>(val: T) -> T {
    return val;
}

// Multi-parameter Generics
struct Pair<K, V> {
    key: K;
    value: V;
}
```
