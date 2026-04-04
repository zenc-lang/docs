# std/env

O módulo `std/env` fornece acesso a argumentos de linha de comando, variáveis de ambiente e informações do sistema.

## Uso

```zc
import "std/env.zc"

fn main() {
    // Aceder a variáveis de ambiente
    match Env::get("PATH") {
        Some(path) => println "CAMINHO: {path}",
        None => println "PATH não definido"
    }

    // Iterar sobre argumentos de linha de comando
    for arg in Env::args() {
        println "Arg: {arg}";
    }
}
```

## Métodos

### Argumentos

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **args** | `Env::args() -> Vec<String>` | Retorna um vetor dos argumentos fornecidos ao processo. |

### Variáveis de Ambiente

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **get** | `Env::get(key: char*) -> Option<String>` | Procura uma variável de ambiente por nome. |
| **set** | `Env::set(key: char*, value: char*)` | Define ou atualiza uma variável de ambiente. |
| **remove** | `Env::remove(key: char*)` | Remove uma variável de ambiente. |

### Informação do Sistema

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **os** | `Env::os() -> char*` | Retorna o nome do sistema operativo (ex: "linux", "macos", "windows"). |
| **arch** | `Env::arch() -> char*` | Retorna a arquitetura do CPU (ex: "x86_64", "arm64"). |
走
