# std/process

O módulo `std/process` fornece uma API de alto nível para lançar processos filhos, executar comandos do sistema e capturar a sua saída.

## Visão Geral

- **Padrão Builder**: A estrutura `Command` utiliza um padrão builder fluído para construir linhas de comando.
- **Captura de Saída**: Capture facilmente a saída padrão e os códigos de saída de processos finalizados.
- **RAII**: Tanto `Command` quanto `Output` implementam o trait `Drop` para limpeza automática de buffers internos.
- **Interoperabilidade Padrão**: Envolve perfeitamente a manipulação de processos em nível de sistema subjacente.

## Uso

```zc
import "std/process.zc"

fn main() {
    // Execução básica de comando
    let output = Command::new("echo")
        .arg("olá mundo")
        .output();
        
    if (output.exit_code == 0) {
        println "Capturado: {output.std_out}";
        // output.std_out é uma String, libertada automaticamente
    } else {
        println "Comando falhou com código {output.exit_code}";
    }
}
```

## Definições de Estrutura

### `Command`
Um builder para configurar e lançar um processo.
```zc
struct Command {
    program: String;
    args: Vec<String>;
}
```

### `Output`
O resultado de uma execução de processo finalizada.
```zc
struct Output {
    std_out: String;
    exit_code: int;
}
```

## Métodos

### Métodos de `Command`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Command::new(program: char*) -> Command` | Cria um novo Command para o programa fornecido. |
| **arg** | `arg(self, arg: char*) -> Command*` | Adiciona um argumento e retorna um ponteiro para si mesmo para encadeamento. |
| **output** | `output(self) -> Output` | Executa o comando e aguarda a finalização, capturando o stdout. |
| **status** | `status(self) -> int` | Executa o comando e retorna o código de status de saída. |

## Gerenciamento de Memória

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **free** | `free(self)` | Liberta manualmente os buffers internos do comando. |
| **Trait** | `impl Drop for Command` | Limpa automaticamente os buffers do comando. |
| **Trait** | `impl Drop for Output` | Liberta automaticamente a string de saída capturada. |
走
