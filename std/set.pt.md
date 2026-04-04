# std/set

`Set<T>` é uma implementação genérica de conjunto (hash set) para armazenar valores únicos do tipo `T`. Utiliza uma tabela de hash de endereçamento aberto com sondagem linear (linear probing).

## Visão Geral

- **Genérico**: Armazena qualquer tipo `T`.
- **Único**: Lida automaticamente com duplicados; adicionar um elemento existente retorna `false`.
- **Rápido**: Complexidade de tempo média O(1) para adições, remoções e pesquisas.
- **RAII**: Implementa o trait `Drop` para gerenciamento automático de memória.

## Uso

```zc
import "std/set.zc"

fn main() {
    let s = Set<int>::new();
    
    s.add(10);
    s.add(20);
    s.add(10); // Duplicado, retorna false
    
    if (s.contains(10)) {
        println "O conjunto contém 10";
    }
    
    s.remove(20);
    println "Comprimento: {s.length()}";
} // s é libertado automaticamente aqui
```

## Definição da Estrutura

```zc
struct Set<T> {
    data: T*;
    len: usize;
    cap: usize;
    // ... campos internos
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Set<T>::new() -> Set<T>` | Cria um novo conjunto vazio. |

### Modificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **add** | `add(self, val: T) -> bool` | Adiciona um valor ao conjunto. Retorna `true` se adicionado, `false` se já estiver presente. |
| **remove** | `remove(self, val: T) -> bool` | Remove um valor do conjunto. Retorna `true` se presente e removido. |
| **clear** | `clear(self)` | Remove todos os elementos do conjunto sem libertar a memória alocada. |

### Acesso & Consulta

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **contains** | `contains(self, val: T) -> bool` | Retorna `true` se o valor existe no conjunto. |
| **length** | `length(self) -> usize` | Retorna o número de elementos únicos. |
| **is_empty** | `is_empty(self) -> bool` | Retorna `true` se o conjunto não possui elementos. |
| **capacity** | `capacity(self) -> usize` | Retorna a capacidade interna atual. |

### Utilitários

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Verifica se um slot de hash interno específico está ocupado. |
| **val_at** | `val_at(self, idx: usize) -> Option<T>` | Retorna o valor em um slot interno específico, se houver. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente os buffers internos do conjunto. |
| **Trait** | `impl Drop for Set` | Chama automaticamente `free()` quando o conjunto sai do escopo. |
走
