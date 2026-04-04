# std/stack

`Stack<T>` é uma estrutura de dados genérica Last-In-First-Out (LIFO), implementada como um wrapper em torno de `Vec<T>`.

## Uso

```zc
import "std/stack.zc"

fn main() {
    let s = Stack<int>::new();
    
    s.push(10);
    s.push(20);
    
    println "Topo: {s.peek().unwrap()}"; // 20
    
    let val = s.pop().unwrap(); // 20
}
```

## Definição da Estrutura

```zc
struct Stack<T> {
    vec: Vec<T>;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Stack<T>::new() -> Stack<T>` | Cria uma nova pilha vazia. |

### Modificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **push** | `push(self, val: T)` | Adiciona um elemento ao topo da pilha. |
| **pop** | `pop(self) -> Option<T>` | Remove e retorna o elemento do topo. Retorna `None` se a pilha estiver vazia. |
| **clear** | `clear(self)` | Remove todos os elementos da pilha. |

### Acesso & Consulta

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **peek** | `peek(self) -> Option<T>` | Retorna uma cópia do elemento no topo sem removê-lo. |
| **peek_ref**| `peek_ref(self) -> T*` | Retorna um ponteiro para o elemento no topo. |
| **length** | `length(self) -> usize` | Retorna o número de elementos na pilha. |
| **is_empty** | `is_empty(self) -> bool` | Retorna true se a pilha estiver vazia. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta a memória do vetor interno. |
| **Trait** | `impl Drop for Stack` | Chama automaticamente `free()` quando sai do escopo. |
走
