# std/arena

O módulo `std/arena` fornece um alocador de memória baseado em região (arena), que permite uma alocação rápida e uma liberação eficiente de toda a memória de uma só vez.

## Visão Geral

- **Alocação Rápida**: Simplesmente incrementa um ponteiro dentro de blocos de memória pré-alocados.
- **Liberação Eficiente**: Toda a memória alocada na arena pode ser liberada com uma única operação (`free`).
- **Segurança**: Ajuda a evitar fugas de memória (memory leaks) e fragmentação ao gerenciar o ciclo de vida de objetos relacionados em conjunto.

## Uso

```zc
import "std/arena.zc"

fn main() {
    // Cria uma nova arena
    let a = Arena::new();

    // Aloca memória da arena
    let p1 = a.alloc(100);
    let p2 = a.alloc_type(int);

    // No final do escopo, toda a memória da arena é liberada automaticamente através do trait Drop
}
```

## Definição da Estrutura

```zc
struct Arena {
    blocks: Vec<void*>;
    current_block: void*;
    block_size: usize;
    offset: usize;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Arena::new() -> Arena` | Cria uma nova arena com o tamanho de bloco padrão (4096 bytes). |
| **with_capacity** | `Arena::with_capacity(size: usize) -> Arena` | Cria uma nova arena com um tamanho de bloco específico. |

### Alocação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **alloc** | `alloc(self, size: usize) -> void*` | Aloca `size` bytes da arena. |
| **alloc_type** | `alloc_type(self, type T) -> T*` | Macro de conveniência para alocar o tamanho de um tipo `T`. |
| **alloc_array** | `alloc_array(self, type T, count: usize) -> T*` | Aloca memória para um array de `count` elementos do tipo `T`. |

### Gerenciamento

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **clear** | `clear(self)` | Libera toda a memória alocada na arena sem destruir o objeto arena. |
| **free** | `free(self)` | Libera manualmente toda a memória e os blocos internos. |
| **Trait** | `impl Drop for Arena` | Chama automaticamente `free()` quando sai do escopo. |

## Detalhes de Implementação

- A arena utiliza uma lista vinculada ou um vetor de blocos de memória.
- As alocações são alinhadas de acordo com as necessidades da arquitetura.
- Quando o bloco atual está cheio, um novo bloco é alocado.
走
