+++
title = "11. Параллельность (Async/Await)"
weight = 11
+++


# 11. Параллельность (Async/Await)

Zen C использует модель **бесстековых корутин** для async/await — без пула потоков, без зависимости от pthread.

```zc
async fn fetch_data() -> string {
    return "Данные";
}

fn main() {
    let result = await fetch_data();
}
```

### Как это работает

`async fn` преобразуется компилятором в **конечный автомат**. Каждая
точка `await` становится переходом состояния. Результирующая структура `Future`
содержит состояние, параметры и под-футуры для ожидаемых вызовов.

### Последовательный шаблон

```zc
async fn task(n: int) -> int {
    return n * 2;
}

fn main() {
    let a = await task(5);
    let b = await task(a);
}
```
