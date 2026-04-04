# std/info

O módulo `std/info` fornece acesso a metadados e informações sobre o compilador Zen-C e o ambiente de execução atual.

## Uso

```zc
import "std/info.zc"

fn main() {
    println "Compilador: {Info::compiler_name()}";
    println "Versão: {Info::version()}";
    
    if (Info::is_debug()) {
        println "A correr em modo de depuração.";
    }
}
```

## Métodos de Informação do Compilador

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **version** | `Info::version() -> char*` | Retorna a versão atual do compilador. |
| **compiler_name** | `Info::compiler_name() -> char*` | Retorna o nome do compilador (ex: "zenc"). |
| **build_date** | `Info::build_date() -> char*` | Retorna a data em que o compilador foi construído. |

## Diagnósticos de Execução

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **is_debug** | `Info::is_debug() -> bool` | Retorna true se o código foi compilado com símbolos de depuração (debug). |
| **is_release** | `Info::is_release() -> bool` | Retorna true se o código foi compilado com otimizações de lançamento (release). |
走
