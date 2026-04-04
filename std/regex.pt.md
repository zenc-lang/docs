# std/regex

O módulo `std/regex` fornece suporte para expressões regulares baseadas em `regex.h` do POSIX.

## Uso

```zc
import "std/regex.zc"

fn main() {
    if regex_match("^[a-z]+$", "olá") {
        println "Corresponde!";
    }
    
    let re = Regex::compile("\\d+");
    let contagem = re.count("123 abc 456");
    re.destroy();
}
```

## Definições de Estrutura

### `Regex`

Representa uma expressão regular compilada.

```zc
struct Regex {
    // Identificadores internos
}
```

### `Match`

Representa uma correspondência bem-sucedida de regex.

```zc
struct Match {
    text: char*;
    start: int;
    len: int;
}
```

## Métodos

### Construção de Regex

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **compile** | `Regex::compile(pattern: char*) -> Regex` | Compila um padrão de regex com os sinalizadores (flags) padrão. |
| **compile_with_flags** | `Regex::compile_with_flags(pattern: char*, flags: int) -> Regex` | Compila com sinalizadores POSIX personalizados. |
| **destroy** | `destroy(self)` | Liberta a regex compilada. |

### Correspondência e Pesquisa

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **match** | `match(self, text: char*) -> bool` | Retorna verdadeiro se o padrão corresponder em qualquer lugar no `text`. |
| **find** | `find(self, text: char*) -> Option<Match>` | Retorna a primeira correspondência, incluindo posição e comprimento. |
| **count** | `count(self, text: char*) -> int` | Retorna o número de correspondências não sobrepostas. |
| **split** | `split(self, text: char*) -> Vec<String>` | Divide o texto pelo padrão. |

### Acesso à Correspondência

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **as_string** | `as_string(self) -> char*` | Retorna um ponteiro para o início da correspondência. |
| **end** | `end(self) -> int` | Retorna o índice após o último caractere da correspondência. |

### Funções Auxiliares Estáticas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **regex_match** | `regex_match(pattern: char*, text: char*) -> bool` | Verificação rápida para uma correspondência. |
| **regex_find** | `regex_find(pattern: char*, text: char*) -> Option<Match>` | Encontra a primeira correspondência. |
| **regex_count** | `regex_count(pattern: char*, text: char*) -> int` | Conta todas as correspondências. |
| **regex_split** | `regex_split(pattern: char*, text: char*) -> Vec<String>` | Divide o texto pelo padrão. |
走
