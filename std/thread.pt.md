# std/thread

O módulo `std/thread` fornece primitivas de alto nível para criar e gerenciar threads de execução concorrentes.

## Visão Geral

- **Threads Nativos**: Utiliza o threading nativo do sistema subjacente (ex: threads POSIX).
- **Suporte a Closures**: `Thread::spawn` pode aceitar closures Zen-C, permitindo uma fácil compartilhamento de dados entre threads.
- **Ciclo de Vida Explícito**: Os threads devem ser explicitamente unidos (joined) ou destacados (detached) para garantir a limpeza correta dos recursos.
- **Segurança**: Erros durante a criação ou manipulação de threads são reportados via `Result<bool>`.

## Uso

```zc
import "std/thread.zc"

fn trabalhador(id: int) {
    println "Saudações do trabalhador {id}";
}

fn main() {
    // Lançar com uma closure
    let t = Thread::spawn(|| {
        trabalhador(42);
    }).unwrap();
    
    // Esperar explicitamente pela conclusão
    t.join();
}
```

## Definições das Estruturas

### `Thread`
Representa um handle para um thread lançado.
```zc
struct Thread {
    handle: void*;
}
```

## Métodos

### Ciclo de Vida de `Thread`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **spawn** | `Thread::spawn(func: fn()) -> Result<Thread>` | Lança um novo thread executando a closure ou função fornecida. |
| **join** | `join(self) -> Result<bool>` | Bloqueia o thread atual até que o thread lançado termine. |
| **detach** | `detach(self) -> Result<bool>` | Destaca o thread, permitindo que ele corra independentemente. Os recursos são libertados automaticamente ao terminar. |
| **cancel** | `cancel(self) -> Result<bool>` | Envia um pedido de cancelamento ao thread. |

### Funções Utilitárias

| Função | Assinatura | Descrição |
| :--- | :--- | :--- |
| **sleep_ms** | `sleep_ms(ms: int)` | Suspende a execução do thread atual por aproximadamente `ms` milissegundos. |
走
走
走
