# std/sync

Il modulo `std/sync` fornisce una suite completa di primitive di sincronizzazione per la gestione dell'accesso concorrente ai dati condivisi e il coordinamento dell'esecuzione dei thread.

## Panoramica

- **Primitive Standard**: Include `Mutex`, `CondVar`, `RwLock`, `Once`, `Semaphore` e `Barrier`.
- **Integrazione RAII**: Tutte le primitive implementano il tratto `Drop`, garantendo che le risorse di sistema (come gli handle pthread) vengano rilasciate automaticamente.
- **Cross-platform**: Astrae in modo sicuro le peculiarità specifiche della piattaforma (ad esempio, implementando `Barrier` e `Semaphore` tramite mutex/condvars su macOS).
- **Efficienza**: Wrapper sottili intorno alle librerie di sincronizzazione ottimizzate a livello di sistema.

## Utilizzo

```zc
import "std/sync.zc"

fn main() {
    let m = Mutex::new();
    
    // Lock con ambito (RAII)
    {
        m.lock();
        // Sezione critica
        m.unlock();
    } // m viene liberato automaticamente se era l'ultimo proprietario
    
    // Inizializzazione una tantum
    let once = Once::new();
    once.call(|| {
        println "Inizializzato!";
    });
}
```

## Definizioni delle Strutture

### `Mutex`
Un blocco di mutua esclusione per proteggere i dati condivisi.

### `CondVar`
Una variabile di condizione per la segnalazione tra thread basata sui cambiamenti di stato.

### `RwLock`
Un blocco lettore-scrittore che consente più lettori concorrenti ma solo uno scrittore.

### `Once`
Garantisce che un pezzo specifico di codice di inizializzazione venga eseguito esattamente una volta.

### `Semaphore`
Un semaforo a conteggio per controllare l'accesso a un pool di risorse.

### `Barrier`
Un punto di sincronizzazione in cui più thread devono attendere fino a quando non ne è arrivato un numero specifico.

## Metodi

### Metodi di `Mutex`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Mutex::new() -> Mutex` | Crea un nuovo mutex. |
| **lock** | `lock(self)` | Acquisisce il blocco (bloccante). |
| **try_lock** | `try_lock(self) -> bool` | Tenta di acquisire il blocco senza bloccare. |
| **unlock** | `unlock(self)` | Rilascia il blocco. |

### Metodi di `CondVar`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `CondVar::new() -> CondVar` | Crea una nuova variabile di condizione. |
| **wait** | `wait(self, mutex: Mutex*)` | Blocca il thread fino alla segnalazione, rilasciando temporaneamente il mutex. |
| **signal** | `signal(self)` | Sveglia un thread in attesa su questa condizione. |
| **broadcast**| `broadcast(self)` | Sveglia tutti i thread in attesa su questa condizione. |

### Metodi di `RwLock`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `RwLock::new() -> RwLock` | Crea un nuovo blocco lettore-scrittore. |
| **rdlock** | `rdlock(self)` | Acquisisce un blocco di lettura condiviso. |
| **wrlock** | `wrlock(self)` | Acquisisce un blocco di scrittura esclusivo. |
| **unlock** | `unlock(self)` | Rilascia qualsiasi blocco detenuto. |

### Metodi di `Semaphore`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Semaphore::new(value: int) -> Semaphore` | Crea un nuovo semaforo con il `value` iniziale. |
| **wait** | `wait(self)` | Decrementa il semaforo (bloccando se è 0). |
| **post** | `post(self)` | Incrementa il semaforo. |
| **value** | `value(self) -> int` | Restituisce il valore corrente. |

### Metodi di `Barrier`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Barrier::new(count: int) -> Barrier` | Crea una nuova barriera per `count` thread. |
| **wait** | `wait(self) -> bool` | Attende alla barriera. Restituisce `true` per il leader designato. |

## Gestione della Memoria

Tutte le primitive implementano `impl Drop` e chiameranno automaticamente il loro metodo `free()` interno per rilasciare le risorse di sistema quando escono dall'ambito.
