+++
title = "10. Genéricos"
weight = 10
+++

# 10. Genéricos {#10-genericos}


Plantillas seguras para tipos para Structs y Funciones.

```zc
// Struct Genérico
struct Box<T> {
    item: T;
}

// Función Genérica
fn identidad<T>(val: T) -> T {
    return val;
}

// Genéricos con múltiples parámetros
struct Par<K, V> {
    llave: K;
    valor: V;
}
```
