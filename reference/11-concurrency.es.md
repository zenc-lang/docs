+++
title = "11. Concurrencia (Async/Await)"
weight = 11
+++

# 11. Concurrencia (Async/Await)


Construido sobre pthreads.

```zc
async fn obtener_datos() -> string {
    // Se ejecuta en segundo plano
    return "Datos";
}

fn main() {
    let futuro = obtener_datos();
    let resultado = await futuro;
}
```
