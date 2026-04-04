# std/random

O módulo `std/random` fornece um wrapper orientado a objetos idiomático para o gerador de números pseudo-aleatórios (PRNG) em torno das funções de `<stdlib.h>` do POSIX.

## Uso

```zc
import "std/random.zc"

fn main() {
    // Semeia o gerador automaticamente com o tempo atual
    let rng = Random::new();

    // Gerar inteiros aleatórios
    let limitado = rng.next_int_range(1, 100); // 1 a 100 inclusive
    
    println "Resultado: {limitado}";
}
```

## Definição da Estrutura

```zc
struct Random {
    seed: U32;
}
```

## Métodos

### Inicialização

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Random::new() -> Random` | Cria um novo gerador aleatório semeado com o tempo atual do sistema. |
| **from_seed** | `Random::from_seed(seed: U32) -> Random` | Cria um novo gerador aleatório utilizando uma semente específica. |

### Geração

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **next_int** | `next_int(self) -> int` | Retorna um inteiro aleatório no intervalo bruto `[0, RAND_MAX]`. |
| **next_int_range** | `next_int_range(self, min: int, max: int) -> int` | Retorna um inteiro aleatório no intervalo `[min, max]` inclusive. |
| **next_double** | `next_double(self) -> double` | Retorna um número de vírgula flutuante aleatório no intervalo `[0.0, 1.0)`. |
| **next_bool** | `next_bool(self) -> bool` | Retorna um booleano aleatório. |
走
