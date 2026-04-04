# std/iter

O módulo `std/iter` fornece tipos e traits básicos para suportar o mecanismo de iteração `for-in` em Zen-C.

## Visão Geral

O Zen-C utiliza o conceito de iteradores para permitir a travessia de coleções (`Vec`, `Map`, `Queue`, etc.) ou intervalos de forma segura e eficiente.

## Uso

```zc
import "std/iter.zc"

fn main() {
    // Iteração sobre um intervalo
    for i in Range::new(0, 5) {
        println "{i}"; // 0, 1, 2, 3, 4
    }
}
```

## Estrutura `Range`

Representa um intervalo numérico de `start` (inclusivo) até `end` (exclusivo).

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Range::new(start: int, end: int) -> Range` | Cria um novo intervalo. |
| **iterator** | `iterator(self) -> RangeIter` | Retorna um iterador para o intervalo. |

## Conceitos de Iterador

Um objeto iterador deve seguir uma interface que o motor do loop `for-in` possa compreender:

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **next** | `next(self) -> Option<T>` | Retorna o próximo elemento envolto num `Option` ou `None` quando termina. |

## Trait `Iterable`

Coleções que podem ser utilizadas num loop `for-in` devem implementar o método:

```zc
fn iterator(self) -> IteratorType
```

Onde `IteratorType` implementa o método `next`.
走
