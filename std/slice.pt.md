# std/slice

Uma `Slice<T>` é uma visão (view) sobre uma sequência contígua de elementos numa coleção ou array. Consiste num ponteiro e num comprimento.

## Visão Geral

- **Leve**: Não possui a propriedade dos dados; é apenas uma referência a dados existentes.
- **Seguro**: O acesso através de fatias (slices) inclui verificação de limites (bounds checking).
- **Versátil**: Pode referenciar dados do Heap (`Vec`), da Stack (array) ou até de memória mapeada.

## Uso

```zc
import "std/slice.zc"
import "std/vec.zc"

fn main() {
    let v = Vec<int>::new();
    v.push(10); v.push(20); v.push(30);

    // Criar uma fatia dos dois primeiros elementos
    let s = v.as_slice().sub_slice(0, 2);
    
    println "Comprimento da fatia: {s.length()}"; // 2
    println "Primeiro elemento: {s[0]}"; // 10
}
```

## Definição da Estrutura

```zc
struct Slice<T> {
    ptr: T*;
    len: usize;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Slice<T>::new(ptr: T*, len: usize) -> Slice<T>` | Cria uma nova fatia a partir de um ponteiro e um comprimento. |
| **sub_slice**| `sub_slice(self, start: usize, len: usize) -> Slice<T>` | Cria uma nova fatia menor a partir da fatia atual. |

### Acesso & Consulta

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **get** | `get(self, idx: usize) -> T` | Retorna uma cópia do elemento. Entra em pânico se estiver fora dos limites. |
| **get_ptr** | `get_ptr(self, idx: usize) -> T*` | Retorna um ponteiro para o elemento. Entra em pânico se estiver fora dos limites. |
| **length** | `length(self) -> usize` | Retorna o número de elementos na fatia. |
| **is_empty** | `is_empty(self) -> bool` | Retorna true se o comprimento for 0. |

### Operações

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **copy_from** | `copy_from(self, src: Slice<T>)` | Copia elementos de outra fatia para esta. As fatias devem ter o mesmo comprimento. |
走
