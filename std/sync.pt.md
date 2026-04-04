# std/sync

O módulo `std/sync` fornece um conjunto abrangente de primitivas de sincronização para gerenciar o acesso concorrente a dados compartilhados e coordenar a execução de threads.

## Visão Geral

- **Primitivas Padrão**: Inclui `Mutex`, `CondVar`, `RwLock`, `Once`, `Semaphore` e `Barrier`.
- **Integração RAII**: Todas as primitivas implementam o trait `Drop`, garantindo que os recursos do sistema (como handles pthread) sejam libertados automaticamente.
- **Multiplataforma**: Abstrai com segurança as peculiaridades de cada plataforma (por exemplo, implementando `Barrier` e `Semaphore` via mutex/condvars no macOS).
- **Eficiência**: Wrappers leves em torno das bibliotecas de sincronização otimizadas do sistema.

## Uso

```zc
import "std/sync.zc"

fn main() {
    let m = Mutex::new();
    
    // Bloqueio com escopo (RAII)
    {
        m.lock();
        // Seção crítica
        m.unlock();
    } // m é libertado automaticamente se fosse o último proprietário
    
    // Inicialização única
    let once = Once::new();
    once.call(|| {
        println "Inicializado!";
    });
}
```

## Definições das Estruturas

### `Mutex`
Um bloqueio de exclusão mútua (Mutually Exclusive lock) para proteger dados compartilhados.

### `CondVar`
Uma variável de condição para sinalização entre threads baseada em mudanças de estado.

### `RwLock`
Um bloqueio de leitura-escrita que permite múltiplos leitores concorrentes, mas apenas um escritor.

### `Once`
Garante que um pedaço específico de código de inicialização seja executado exatamente uma vez.

### `Semaphore`
Um semáforo de contagem para controlar o acesso a um pool de recursos.

### `Barrier`
Um ponto de sincronização onde múltiplas threads devem esperar até que um número específico tenha chegado.

## Métodos

### Métodos de `Mutex`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Mutex::new() -> Mutex` | Cria um novo mutex. |
| **lock** | `lock(self)` | Adquire o bloqueio (bloqueia o thread). |
| **try_lock** | `try_lock(self) -> bool` | Tenta adquirir o bloqueio sem bloquear. |
| **unlock** | `unlock(self)` | Liberta o bloqueio. |

### Métodos de `CondVar`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `CondVar::new() -> CondVar` | Cria uma nova variável de condição. |
| **wait** | `wait(self, mutex: Mutex*)` | Bloqueia o thread até ser sinalizado, libertando temporariamente o mutex. |
| **signal** | `signal(self)` | Acorda um thread que está à espera nesta condição. |
| **broadcast**| `broadcast(self)` | Acorda todos os threads que estão à espera nesta condição. |

### Métodos de `RwLock`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `RwLock::new() -> RwLock` | Cria um novo bloqueio de leitura-escrita. |
| **rdlock** | `rdlock(self)` | Adquire um bloqueio de leitura compartilhado. |
| **wrlock** | `wrlock(self)` | Adquire um bloqueio de escrita exclusivo. |
| **unlock** | `unlock(self)` | Liberta qualquer bloqueio detido. |

### Métodos de `Semaphore`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Semaphore::new(value: int) -> Semaphore` | Cria um novo semáforo com o `value` inicial. |
| **wait** | `wait(self)` | Decrementa o semáforo (bloqueando se for 0). |
| **post** | `post(self)` | Incrementa o semáforo. |
| **value** | `value(self) -> int` | Retorna o valor atual. |

### Métodos de `Barrier`

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Barrier::new(count: int) -> Barrier` | Cria uma nova barreira para `count` threads. |
| **wait** | `wait(self) -> bool` | Espera na barreira. Retorna `true` para o líder designado. |

## Gerenciamento de Memória

Todas as primitivas implementam `impl Drop` e chamarão automaticamente o seu método `free()` interno para libertar os recursos do sistema quando saírem do escopo.
走
