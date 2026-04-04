# std/sys/signal

O módulo `std/sys/signal` fornece utilitários para lidar com sinais do sistema (como `SIGINT`, `SIGTERM`, etc.), envolvendo as primitivas `signal.h` do POSIX.

## Visão Geral

- **Tratadores de Sinais (Handlers)**: Registe funções para serem executadas quando o seu processo receber um sinal específico.
- **Sinais Comuns**: Acesso fácil a constantes de sinais padrão.
- **Interrupção de Processo**: Útil para encerramento gracioso (graceful shutdown) de aplicações.

## Uso

```zc
import "std/sys/signal.zc"
import "std/io.zc"

fn ao_interromper(sig: int) {
    println "Sinal {sig} recebido. A encerrar...";
    exit(0);
}

fn main() {
    // Registar tratador para Ctrl+C
    Signal::handle(SIGINT, ao_interromper);
    
    // Loop infinito
    while (true) {}
}
```

## Constantes de Sinais

| Constante | Descrição |
| :--- | :--- |
| **SIGINT** | Interrupção do terminal (Ctrl+C). |
| **SIGTERM** | Sinal de terminação (encerramento amigável). |
| **SIGKILL** | Sinal de morte imediata (não pode ser capturado). |
| **SIGSEGV** | Violação de segmentação (falha de memória). |
| **SIGABRT** | Sinal de aborto (geralmente de `panic`). |

## Métodos

### Gerenciamento de Sinais

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **handle** | `Signal::handle(sig: int, handler: fn(int))` | Define a função a ser chamada quando o sinal `sig` for recebido. |
| **raise** | `Signal::raise(sig: int) -> int` | Envia o sinal `sig` para o processo atual. |
| **ignore** | `Signal::ignore(sig: int)` | Configura o processo para ignorar completamente o sinal `sig`. |
| **reset** | `Signal::reset(sig: int)` | Restaura o comportamento padrão do sistema para o sinal `sig`. |
走
