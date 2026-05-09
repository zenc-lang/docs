+++
title = "11. Concurrencia (Async/Await)"
weight = 11
+++


# 11. Concurrencia (Async/Await)

Zen C utiliza un modelo de **corrutina sin pila** para async/await — sin pool de hilos, sin dependencia de pthread.

```zc
async fn fetch_data() -> string {
    return "Datos";
}

fn main() {
    let result = await fetch_data();
}
```

### Cómo funciona

Una `async fn` es transformada por el compilador en una **máquina de estados**. Cada
punto `await` se convierte en una transición de estado. El `Future` resultante
contiene el estado, los parámetros y los sub-futures para las llamadas awaitadas.

### Patrón secuencial

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
