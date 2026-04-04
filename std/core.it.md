# std/core

Il modulo `std/core` fornisce le definizioni più fondamentali e le primitive per la gestione degli errori per i programmi Zen-C. È implicitamente richiesto dalla maggior parte delle altre librerie standard.

## Panoramica

- **Header Standard**: Include header C critici come `stdlib.h`, `stdio.h` e `stdbool.h`.
- **Meccanismo di Panic**: Fornisce la macro `panic` per la segnalazione di errori non recuperabili.
- **Controllo del Processo**: Include funzioni di base per il controllo del processo come `exit`.

## Metodi

### Gestione degli Errori

| Metodo/Macro | Firma | Descrizione |
| :--- | :--- | :--- |
| **panic** | `panic(msg: char*)` | Stampa un messaggio di errore formattato includendo file, riga e funzione, quindi termina il processo. |

### Controllo del Processo

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **exit** | `exit(code: int)` | Termina immediatamente il processo con il codice di ritorno fornito. |
