# std/time

O módulo `std/time` fornece utilitários para medição de tempo de alta precisão e suspensão de threads.

## Visão Geral

- **Precisão de Milissegundos**: `Time::now()` retorna o tempo atual do sistema em milissegundos.
- **Tipo Duration**: A estrutura `Duration` permite cálculos fáceis de intervalos de tempo.
- **Suspensão Simples**: Funções fáceis de usar para suspender a execução.
- **Leve**: Overhead mínimo, envolvendo as funções de tempo padrão do sistema.

## Uso

```zc
import "std/time.zc"

fn main() {
    let inicio = Time::now();
    
    // Dormir por 1.5 segundos
    Time::sleep(Duration::from_ms(1500));
    
    let fim = Time::now();
    println "Decorrido: {fim - inicio} ms";
}
```

## Definições das Estruturas

### `Duration`
Representa um intervalo de tempo.
```zc
struct Duration {
    millis: U64;
}
```

### `Time`
Estrutura utilitária estática para operações de tempo do sistema.
```zc
struct Time {}
```

## Métodos

### Métodos de `Duration`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **from_ms** | `Duration::from_ms(ms: U64) -> Duration` | Cria um `Duration` a partir de uma contagem de milissegundos. |
| **from_secs** | `Duration::from_secs(s: U64) -> Duration` | Cria um `Duration` a partir de uma contagem de segundos. |

### Métodos Estáticos de `Time`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **now** | `Time::now() -> U64` | Retorna o tempo atual do sistema em milissegundos desde o epoch. |
| **sleep** | `Time::sleep(d: Duration)` | Suspende o thread atual pela `Duration` especificada. |
| **sleep_ms** | `Time::sleep_ms(ms: U64)` | Suspende o thread atual pela contagem especificada de milissegundos. |
走
走
走
走
走
