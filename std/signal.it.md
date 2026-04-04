# std/sys/signal

Il modulo `std/sys/signal` fornisce primitive per la gestione dei segnali di sistema, avvolgendo la funzionalità `signal.h` di POSIX.

## Panoramica

- **Intercettazione dei Segnali**: Definisci gestori (handler) personalizzati per segnali come `SIGINT` (Ctrl+C).
- **Terminazione Graduale**: Usa i gestori dei segnali per eseguire la pulizia prima di uscire.
- **Costanti Comuni**: Fornisce definizioni cross-platform per i segnali standard.

## Utilizzo

```zc
import "std/sys/signal.zc"
import "std/io.zc"

fn al_momento_dell_interruzione(sig: int) {
    println "Ricevuto SIGINT ({sig}). Pulizia in corso...";
    exit(0);
}

fn main() {
    Signal::set_handler(Z_SIGINT, al_momento_dell_interruzione);
    println "In attesa di Ctrl+C...";
    while(true) {}
}
```

## Definizione della Struttura

```zc
struct Signal {
    // Implementazione interna
}
```

## Metodi

### Metodi di `Signal`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **set_handler** | `Signal::set_handler(sig: int, handler: fn*(int)) -> fn*(int)` | Registra un gestore per il segnale fornito e restituisce il gestore precedente. |

## Costanti

### Segnali Standard
- `Z_SIGINT`: Interruzione da tastiera (Ctrl+C).
- `Z_SIGILL`: Istruzione illegale.
- `Z_SIGABRT`: Segnale di interruzione (abort).
- `Z_SIGFPE`: Eccezione in virgola mobile.
- `Z_SIGSEGV`: Violazione di segmentazione (accesso alla memoria non valido).
- `Z_SIGTERM`: Segnale di terminazione.
走
