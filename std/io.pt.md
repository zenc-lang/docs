# std/io

O módulo `std/io` fornece funções essenciais de entrada e saída, incluindo impressão na consola e leitura da entrada padrão.

## Uso

```zc
import "std/io.zc"

fn main() {
    // Impressão simples
    print "Olá, ";
    println "Mundo!"; // Adiciona nova linha

    // Com formatação
    let user = "Dev";
    println "Bem-vindo {user}!"; 
}
```

## Funções de Saída

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **print** | `print s: char*` | Imprime uma string na saída padrão (stdout). |
| **println** | `println s: char*` | Imprime uma string na saída padrão com uma nova linha. |
| **printf** | `printf(fmt: char*, ...args)` | Impressão formatada em estilo C. |

## Funções de Entrada

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **readln** | `readln() -> String` | Lê uma linha da entrada padrão (stdin) como uma `String`. |

## Fluxos de Erro

Para imprimir no erro padrão (stderr):

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **eprint** | `eprint s: char*` | Imprime uma string no erro padrão. |
| **eprintln**| `eprintln s: char*` | Imprime uma string no erro padrão com uma nova linha. |

## Outros Fluxos

O Zen-C trata `stdout`, `stdin` e `stderr` como descritores de ficheiros especiais que podem ser utilizados com os métodos do módulo `std/fs`.
走
