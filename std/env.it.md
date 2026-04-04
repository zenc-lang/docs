# std/env

Il modulo `std/env` fornisce l'accesso cross-platform alle variabili d'ambiente del processo.

## Panoramica

- **Accesso Chiave-Valore**: API semplice per ottenere, impostare e rimuovere variabili d'ambiente.
- **Borrowed o Owned**: Scegli tra `get` (restituisce una stringa C in prestito) e `get_dup` (restituisce una `String` di proprietà, allocata nell'heap).
- **Multiplataforma**: Abstrae in modo sicuro le chiamate di sistema sottostanti per la manipolazione dell'ambiente.

## Utilizzo

```zc
import "std/env.zc"

fn main() {
    // Impostazione di una variabile d'ambiente
    Env::set("MY_APP_MODE", "development");

    // Recupo (In prestito)
    match Env::get("MY_APP_MODE") {
        Some(val) => println "Modalità: {val}",
        None => println "Modalità non impostata"
    }

    // Recupero (String di proprietà per RAII)
    match Env::get_dup("HOME") {
        Some(home) => {
             println "Home: {home}";
             // home viene liberata automaticamente
        }
        None => println "HOME non trovata"
    }
}
```

## Definizione dell'Enum

```zc
enum EnvRes {
    OK,
    ERR,
}
```

## Metodi

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **get** | `Env::get(name: char*) -> Option<char*>` | Recupera un puntatore in prestito ad una variabile d'ambiente. Non liberare. |
| **get_dup** | `Env::get_dup(name: char*) -> Option<String>` | Recupera una variabile d'ambiente come un nuovo oggetto `String`. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **set** | `Env::set(name: char*, value: char*) -> EnvRes` | Imposta o aggiorna una variabile d'ambiente. |
| **unset** | `Env::unset(name: char*) -> EnvRes` | Rimuove una variabile d'ambiente dal processo corrente. |
