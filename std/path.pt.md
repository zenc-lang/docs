# std/path

O módulo `std/path` fornece utilitários multiplataforma para manipular caminhos de sistemas de ficheiros. Simplifica tarefas comuns como unir caminhos, extrair extensões e encontrar diretórios pais.

## Visão Geral

- **Multiplataforma**: Lida corretamente com barras (/) e barras invertidas (\) durante a manipulação.
- **Segurança de Tipos**: A estrutura `Path` encapsula informações de caminho, distinguindo-as de strings comuns.
- **Parsing Conveniente**: Extraia facilmente componentes como `extension`, `file_name` e `parent`.
- **RAII**: A memória é gerenciada automaticamente através do trait `Drop`.

## Uso

```zc
import "std/path.zc"

fn main() {
    let p = Path::new("/home/usuario");
    let caminho_completo = p.join("docs/arquivo.txt");
    
    println "Caminho completo: {caminho_completo.c_str()}";
    
    match caminho_completo.extension() {
        Some(ext) => println "Extensão: {ext}",
        None => println "Nenhuma extensão encontrada"
    }
} // caminho_completo e p são libertados automaticamente aqui
```

## Definição da Estrutura

```zc
struct Path {
    str: String;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Path::new(s: char*) -> Path` | Cria um novo `Path` a partir de uma string C. |
| **from_string** | `Path::from_string(s: String) -> Path` | Cria um `Path` assumindo a propriedade de uma `String`. |
| **clone** | `clone(self) -> Path` | Retorna uma cópia profunda (deep copy) do `Path`. |

### Manipulação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **join** | `join(self, other: char*) -> Path` | Adiciona `other` ao caminho usando o separador de diretório correto. |

### Parsing

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **extension** | `extension(self) -> Option<String>` | Retorna a extensão do ficheiro (sem o ponto inicial), se existir. |
| **file_name** | `file_name(self) -> Option<String>` | Retorna o componente final do caminho. |
| **parent** | `parent(self) -> Option<Path>` | Retorna o caminho do diretório pai. |

### Acesso

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Retorna a representação da string C subjacente. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente a memória da string interna do caminho. |
| **Trait** | `impl Drop for Path` | Chama automaticamente `free()` quando sai do escopo. |
走
