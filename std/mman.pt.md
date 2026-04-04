# std/sys/mman

O módulo `std/sys/mman` fornece uma interface para gerenciamento de memória virtual, envolvendo as primitivas `mmap` e `munmap` do sistema operacional.

## Visão Geral

- **Mapeamento de Ficheiros**: Transforma ficheiros do disco em memória virtual acessível por ponteiros.
- **Memória Anónima**: Alocação de grandes blocos de memória diretamente do sistema operacional.
- **Proteção de Memória**: Define permissões de leitura, escrita e execução em páginas de memória.

## Uso

```zc
import "std/sys/mman.zc"

fn main() {
    // Alocar um bloco anónimo de 4KB protegido para leitura e escrita
    let ptr = Memory::mmap(
        null, 
        4096, 
        PROT_READ | PROT_WRITE, 
        MAP_PRIVATE | MAP_ANON, 
        -1, 
        0
    );
    
    if (ptr != MAP_FAILED) {
        // ... usar a memória
        Memory::munmap(ptr, 4096);
    }
}
```

## Constantes de Proteção

- `PROT_READ`: Memória pode ser lida.
- `PROT_WRITE`: Memória pode ser escrita.
- `PROT_EXEC`: Memória pode ser executada.
- `PROT_NONE`: Memória não pode ser acedida.

## Constantes de Mapeamento

- `MAP_SHARED`: Mapeamento compartilhado entre processos.
- `MAP_PRIVATE`: Cria uma cópia privada (copy-on-write).
- `MAP_FIXED`: Usa exatamente o endereço fornecido.
- `MAP_ANON`: Não associado a nenhum ficheiro.

## Métodos

### Primitivas de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **mmap** | `Memory::mmap(addr: void*, len: usize, prot: int, flags: int, fd: int, offset: i64) -> void*` | Cria um novo mapeamento no espaço de endereçamento virtual do processo. |
| **munmap** | `Memory::munmap(addr: void*, len: usize) -> int` | Remove um mapeamento existente. |
| **mprotect**| `Memory::mprotect(addr: void*, len: usize, prot: int) -> int` | Altera as proteções de acesso às páginas de memória. |
走
