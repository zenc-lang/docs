# std/queue

`Queue<T>` é uma fila genérica First-In-First-Out (FIFO) implementada como um **Ring Buffer (Buffer Circular)**.

## Uso

```zc
import "std/queue.zc"

fn main() {
    let q = Queue<int>::new();
    
    q.push(1);
    q.push(2);
    q.push(3);
    
    // Pop retorna um Option<T>
    if (q.pop().is_some()) {
        println "Removido: {q.pop().unwrap()}"; // 1
    }
}
```

## Detalhes de Implementação

- **Ring Buffer**: Utiliza um buffer circular com índices `head` (cabeça) e `tail` (cauda).
- **Desempenho**:
    - `push`: **O(1) amortizado** (redimensiona quando cheio).
    - `pop`: **O(1)** (avança o índice head).
    - `clone`: **O(N)**.
- **Segurança**: Manuseio seguro de envolvimento de memória e redimensionamento.

## Definição da Estrutura

```zc
struct Queue<T> {
    data: T*;
    cap: usize;
    head: usize;
    tail: usize;
    count: usize;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Queue<T>::new() -> Queue<T>` | Cria uma nova fila vazia. |
| **clone** | `clone(self) -> Queue<T>` | Cria uma cópia profunda da fila. |

### Modificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **push** | `push(self, value: T)` | Adiciona um elemento ao final da fila. |
| **pop** | `pop(self) -> Option<T>` | Remove e retorna o elemento na frente. Retorna `None` se estiver vazia. |
| **clear** | `clear(self)` | Remove todos os itens da fila. |

### Acesso & Consulta

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **length** | `length(self) -> usize` | Retorna o número de itens. |
| **is_empty** | `is_empty(self) -> bool` | Retorna `true` se a fila estiver vazia. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta o buffer interno. |
| **Trait** | `impl Drop for Queue` | Chama automaticamente `free()` quando sai do escopo. |
走
