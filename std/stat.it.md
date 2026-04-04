# std/sys/stat

Il modulo `std/sys/stat` fornisce un'interfaccia per il recupero dei metadati estesi dei file e delle informazioni sullo stato, avvolgendo `sys/stat.h` di POSIX.

## Panoramica

- **Metadati dei File**: Recupera la dimensione del file, la modalità (permessi) e i timestamp.
- **Timestamp**: Accedi ai tempi di accesso, modifica e cambiamento come timestamp Unix.
- **Controllo del Tipo**: Metodi di supporto per determinare se una modalità rappresenta un file o una directory.

## Utilizzo

```zc
import "std/sys/stat.zc"
import "std/io.zc"

fn main() {
    let res = FileStat::stat("miodocumento.txt");
    if (res.is_some()) {
        let st = res.unwrap();
        println "Dimensione: {st.size} byte";
        println "Permessi: {st.mode}";
        
        if (FileStat::is_dir(st.mode)) {
            println "È una directory.";
        }
    }
}
```

## Definizione della Struttura

### `Stat`
Contiene metadati dei file in stile Unix.
```zc
struct Stat {
    mode: u32;
    size: u64;
    atime: i64;
    mtime: i64;
    ctime: i64;
    uid: u32;
    gid: u32;
}
```

## Metodi

### Metodi di `FileStat`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **stat** | `FileStat::stat(path: char*) -> Option<Stat>` | Restituisce i metadati per il percorso fornito, o `None` in caso di fallimento. |
| **is_dir** | `FileStat::is_dir(mode: u32) -> bool` | Controlla se la modalità fornita rappresenta una directory. |
| **is_file** | `FileStat::is_file(mode: u32) -> bool` | Controlla se la modalità fornita rappresenta un file regolare. |
