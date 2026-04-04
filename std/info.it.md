# std/sys/info

Il modulo `std/sys/info` fornisce utilità per il recupero dell'identificazione e delle informazioni del sistema, avvolgendo `uname` di POSIX.

## Panoramica

- **Identificazione del Sistema**: Accedi al nome del sistema operativo, alla versione del kernel, all'architettura hardware e altro ancora.
- **Conformità RAII**: La struttura `Uname` gestisce automaticamente la memoria per le sue stringhe interne.

## Utilizzo

```zc
import "std/sys/info.zc"
import "std/io.zc"

fn main() {
    let info = SysInfo::get_uname();
    println "S.O.: {info.sysname}";
    println "Kernel: {info.release}";
    println "Architettura: {info.machine}";
}
```

## Definizione della Struttura

### `Uname`
Contiene campi di identificazione del sistema.
```zc
struct Uname {
    sysname: String;
    nodename: String;
    release: String;
    version: String;
    machine: String;
}
```

## Metodi

### Metodi di `SysInfo`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **get_uname** | `SysInfo::get_uname() -> Uname` | Restituisce una struttura `Uname` contenente varie stringhe di sistema. |

## Gestione della Memoria
- `Uname` implementa `impl Drop` e libererà automaticamente i suoi buffer `String` interni quando esce dall'ambito.
