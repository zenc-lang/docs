# std/sort

O módulo `std/sort` fornece funções para ordenar coleções e fatias (slices).

## Uso

```zc
import "std/sort.zc"
import "std/vec.zc"

fn main() {
    let v = Vec<int>::new();
    v.push(3); v.push(1); v.push(2);
    
    // Ordenação in-place (padrão crescente)
    Sort::sort_int(v.as_slice());
}
```

## Funções de Ordenação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **sort_int** | `Sort::sort_int(s: Slice<int>)` | Ordena uma fatia de inteiros em ordem crescente. |
| **sort_float**| `Sort::sort_float(s: Slice<float>)` | Ordena uma fatia de floats em ordem crescente. |
| **sort_by** | `Sort::sort_by(s: Slice<T>, cmp: fn(T*, T*) -> int)` | Ordena uma fatia genérica usando uma função de comparação personalizada. |

## Algoritmo

- Atualmente utiliza o algoritmo **Quicksort** com uma estratégia de pivô otimizada para o desempenho médio em casos reais.
- A função `sort_by` é estável se a função de comparação personalizada for implementada corretamente.
走
