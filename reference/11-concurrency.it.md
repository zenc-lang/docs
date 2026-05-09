+++
title = "11. Concorrenza (Async/Await)"
weight = 11
+++

# 11. Concorrenza (Async/Await)


Zen C utilizza un modello **stackless coroutine** per l'async/await, senza thread pool o pthread.

```zc
async fn fetch_data() -> string {
    return "Dati";
}

fn main() {
    let risultato = await fetch_data();
}
```

### Come funziona

Una funzione `async` viene trasformata dal compilatore in una **macchina a stati**.
Ogni punto di `await` diventa una transizione di stato. Il `Future` resultante
contiene lo stato, i parametri, e i sub-future per le chiamate awaitate.

### Pattern concorrente

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    // Chiamate sequenziali — ogni await completa prima del successivo
    let a = await task(5);
    let b = await task(a);
}
```
