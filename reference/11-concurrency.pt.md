+++
title = "11. Concorrência (Async/Await)"
weight = 11
+++


# 11. Concorrência (Async/Await)

Zen C usa um modelo de **corrotina sem pilha** para async/await — sem pool de threads, sem dependência de pthread.

```zc
async fn fetch_data() -> string {
    return "Dados";
}

fn main() {
    let result = await fetch_data();
}
```

### Como funciona

Uma `async fn` é transformada pelo compilador em uma **máquina de estados**. Cada
ponto `await` torna-se uma transição de estado. O `Future` resultante
contém o estado, os parâmetros e os sub-futures para chamadas aguardadas.

### Padrão sequencial

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
