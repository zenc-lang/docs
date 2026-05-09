+++
title = "11. Nebenläufigkeit (Async/Await)"
weight = 11
+++


# 11. Nebenläufigkeit (Async/Await)

Zen C verwendet ein **stackless coroutine**-Modell für Async/Await — kein Thread-Pool, keine pthread-Abhängigkeit.

```zc
async fn fetch_data() -> string {
    return "Daten";
}

fn main() {
    let result = await fetch_data();
}
```

### Wie es funktioniert

Eine `async fn` wird vom Compiler in eine **Zustandsmaschine** umgewandelt. Jeder
`await`-Punkt wird zu einem Zustandsübergang. Der resultierende `Future`-Struct
enthält den Zustand, die Parameter und die Sub-Futures für awaitierte Aufrufe.

### Sequentielles Muster

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
