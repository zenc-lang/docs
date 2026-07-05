+++
title = "11. Generici"
weight = 11
+++

# 11. Generici


Template type-safe per struct e funzioni.

```zc
// Struct Generico
struct Scatola<T> {
    oggetto: T;
}

// Funzione Generica
fn identità<T>(valore: T) -> T {
    return valore;
}

// Generici Multi-parametro
struct Paio<K, V> {
    chiavi: K;
    valore: V;
}
```
