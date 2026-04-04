# std/mem

O módulo `std/mem` fornece utilitários de baixo nível para manipulação de memória e gerenciamento manual do ciclo de vida de objetos.

## Visão Geral

- **Alocação Manual**: Funções para alocar e libertar memória no heap (`malloc`, `free`).
- **Cópia e Preenchimento**: Utilitários para grandes operações em blocos de memória (`copy`, `set`).
- **Informação de Tipos**: Utilitários para obter o tamanho de tipos em tempo de compilação.

## Uso

```zc
import "std/mem.zc"

fn main() {
    // Alocação manual
    let ptr = Mem::alloc(1024);
    
    // Definir memória como zero
    Mem::zero(ptr, 1024);
    
    // Liberação manual
    Mem::free(ptr);
}
```

## Métodos

### Alocação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **alloc** | `Mem::alloc(size: usize) -> void*` | Aloca `size` bytes no heap. |
| **calloc** | `Mem::calloc(num: usize, size: usize) -> void*` | Aloca memória inicializada a zero. |
| **realloc** | `Mem::realloc(ptr: void*, size: usize) -> void*` | Redimensiona um bloco de memória previamente alocado. |
| **free** | `Mem::free(ptr: void*)` | Liberta um bloco de memória no heap. |

### Operações em Blocos

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **copy** | `Mem::copy(dest: void*, src: void*, size: usize)` | Copia `size` bytes da origem para o destino. |
| **move** | `Mem::move(dest: void*, src: void*, size: usize)` | Semelhante ao copy, mas suporta áreas sobrepostas. |
| **set** | `Mem::set(ptr: void*, val: int, size: usize)` | Preenche o bloco com o byte `val`. |
| **zero** | `Mem::zero(ptr: void*, size: usize)` | Preenche o bloco com zeros. |

### Utilitários de Tipo

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **size_of** | `size_of(type T) -> usize` | Macro que retorna o tamanho do tipo `T` em bytes. |
| **align_of**| `align_of(type T) -> usize` | Macro que retorna o requisito de alinhamento do tipo `T`. |

## Segurança

> [!CAUTION]
> As funções neste módulo são inerentemente inseguras. Um uso incorreto pode causar fugas de memória (leaks), dangling pointers ou erros de segmentação. Sempre que possível, utilize tipos seguros como `Vec` ou `Arena`.
走
