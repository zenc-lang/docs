# std/fs

O módulo `std/fs` fornece uma interface multiplataforma abrangente para tarefas de manipulação de ficheiros e diretórios.

## Visão Geral

- **Manipulação de Ficheiros**: Abrir, ler, escrever e fechar ficheiros.
- **Gerenciamento de Diretórios**: Criar, remover e listar conteúdos de diretórios.
- **RAII**: Os tipos `File` e `Dir` implementam o trait `Drop`, garantindo que os descritores de ficheiros sejam fechados automaticamente.
- **Captura de Erros**: Fornece códigos de erro detalhados através do tipo `Result`.

## Uso

```zc
import "std/fs.zc"

fn main() {
    // Ler todo o conteúdo de um ficheiro
    match File::read_to_string("app.config") {
        Ok(content) => println "Configuração: {content}",
        Err(e)      => println "Erro ao ler ficheiro: {e}"
    }

    // Escrever num ficheiro
    let f = File::create("output.txt").unwrap();
    f.write_string("Olá Zen-C!");
} // f é fechado automaticamente aqui
```

## Métodos de Ficheiro (`File`)

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **open** | `File::open(path: char*) -> Result<File>` | Abre um ficheiro existente em modo de leitura. |
| **create** | `File::create(path: char*) -> Result<File>` | Cria um novo ficheiro ou trunca um existente. |

### Leitura & Escrita

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **read** | `read(self, buf: char*, size: usize) -> Result<usize>` | Lê até `size` bytes para o buffer. |
| **write** | `write(self, buf: char*, size: usize) -> Result<usize>` | Escreve `size` bytes do buffer. |
| **write_string** | `write_string(self, s: char*) -> Result<usize>` | Escreve uma string C no ficheiro. |
| **read_to_string**| `File::read_to_string(path: char*) -> Result<String>` | Função utilitária estática para ler todo um ficheiro. |

## Métodos de Diretório (`Dir`)

### Gerenciamento

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **mkdir** | `Dir::mkdir(path: char*) -> Result<bool>` | Cria um novo diretório. |
| **rmdir** | `Dir::rmdir(path: char*) -> Result<bool>` | Remove um diretório vazio. |
| **remove** | `Dir::remove(path: char*) -> Result<bool>` | Remove um ficheiro. |
| **exists** | `Dir::exists(path: char*) -> bool` | Verifica se um ficheiro ou diretório existe. |

### Listagem

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **list** | `Dir::list(path: char*) -> Result<Vec<String>>` | Retorna os nomes de todos os itens dentro do diretório. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **close** | `close(self)` | Fecha manualmente o descritor de ficheiro ou diretório. |
| **Trait** | `impl Drop for File` | Fecha automaticamente o ficheiro quando sai do escopo. |
走
