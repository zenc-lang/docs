# std/sys/stat

O módulo `std/sys/stat` fornece uma interface para recuperar metadados estendidos de ficheiros e informações de status, envolvendo o `sys/stat.h` do POSIX.

## Visão Geral

- **Metadados de Ficheiros**: Recupere o tamanho do ficheiro, o modo (permissões) e os timestamps.
- **Timestamps**: Aceda aos tempos de acesso, modificação e alteração como timestamps Unix.
- **Verificação de Tipo**: Métodos auxiliares para determinar se um modo representa um ficheiro ou um diretório.

## Uso

```zc
import "std/sys/stat.zc"
import "std/io.zc"

fn main() {
    let res = FileStat::stat("meu_documento.txt");
    if (res.is_some()) {
        let st = res.unwrap();
        println "Tamanho: {st.size} bytes";
        println "Permissões: {st.mode}";
        
        if (FileStat::is_dir(st.mode)) {
            println "É um diretório.";
        }
    }
}
```

## Definição da Estrutura

### `Stat`
Contém metadados de ficheiros no estilo Unix.
```zc
struct Stat {
    mode: u32;
    size: u64;
    atime: i64;
    mtime: i64;
    ctime: i64;
    uid: u32;
    gid: u32;
}
```

## Métodos

### Métodos de `FileStat`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **stat** | `FileStat::stat(path: char*) -> Option<Stat>` | Retorna os metadados para o caminho fornecido, ou `None` em caso de falha. |
| **is_dir** | `FileStat::is_dir(mode: u32) -> bool` | Verifica se o modo fornecido representa um diretório. |
| **is_file** | `FileStat::is_file(mode: u32) -> bool` | Verifica se o modo fornecido representa um ficheiro regular. |
走
