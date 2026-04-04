# std/thread

Il modulo `std/thread` fornisce primitive di alto livello per la creazione e la gestione di thread di esecuzione concorrenti.

## Panoramica

- **Thread Nativi**: Utilizza il threading sottostante a livello di sistema (ad esempio, thread POSIX).
- **Supporto alle Closure**: `Thread::spawn` può accettare closure Zen-C, consentendo una facile condivisione dei dati tra i thread.
- **Ciclo di Vita Esplicito**: I thread devono essere esplicitamente uniti (joined) o distaccati (detached) per garantire una corretta pulizia delle risorse.
- **Sicurezza**: Gli errori durante la creazione o la manipolazione dei thread vengono segnalati tramite `Result<bool>`.

## Utilizzo

```zc
import "std/thread.zc"

fn lavoratore(id: int) {
    println "Saluti dal lavoratore {id}";
}

fn main() {
    // Avvio con una closure
    let t = Thread::spawn(|| {
        lavoratore(42);
    }).unwrap();
    
    // Attesa esplicita del completamento
    t.join();
}
```

## Definizioni delle Strutture

### `Thread`
Rappresenta un handle per un thread avviato.
```zc
struct Thread {
    handle: void*;
}
```

## Metodi

### Ciclo di Vita di `Thread`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **spawn** | `Thread::spawn(func: fn()) -> Result<Thread>` | Avvia un nuovo thread che esegue la closure o la funzione fornita. |
| **join** | `join(self) -> Result<bool>` | Blocca il thread corrente finché il thread avviato non termina. |
| **detach** | `detach(self) -> Result<bool>` | Distacca il thread, consentendogli di funzionare in modo indipendente. Le risorse vengono liberate automaticamente all'uscita. |
| **cancel** | `cancel(self) -> Result<bool>` | Invia una richiesta di cancellazione al thread. |

### Funzioni di Utilità

| Funzione | Firma | Descrizione |
| :--- | :--- | :--- |
| **sleep_ms** | `sleep_ms(ms: int)` | Sospende l'esecuzione del thread corrente per circa `ms` millisecondi. |
