# std/sys/user

Il modulo `std/sys/user` fornisce l'accesso alle informazioni di identificazione dell'utente e del gruppo, avvolgendo `unistd.h` di POSIX.

## Panoramica

- **Identità Utente**: Recupera gli ID utente (UID) e gli ID gruppo (GID) reali ed effettivi.
- **Contesto del Processo**: Utile per il controllo dei privilegi e la gestione dei permessi nelle utilità di sistema.

## Utilizzo

```zc
import "std/sys/user.zc"
import "std/io.zc"

fn main() {
    println "UID attuale: {User::get_uid()}";
    println "GID attuale: {User::get_gid()}";
    
    if (User::get_euid() == 0) {
        println "In esecuzione con i privilegi di root.";
    }
}
```

## Definizione della Struttura

```zc
struct User {}
```

## Metodi

### Metodi di `User`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **get_uid** | `User::get_uid() -> u32` | Restituisce l'ID utente reale del processo corrente. |
| **get_gid** | `User::get_gid() -> u32` | Restituisce l'ID gruppo reale del processo corrente. |
| **get_euid** | `User::get_euid() -> u32` | Restituisce l'ID utente effettivo. |
| **get_egid** | `User::get_egid() -> u32` | Restituisce l'ID gruppo effettivo. |
