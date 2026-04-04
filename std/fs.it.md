# std/fs

Il modulo `std/fs` fornisce un'API completa per l'interazione con il file system, inclusi l'I/O di file, la manipolazione di directory e il recupero di metadati.

## Panoramica

- **Handle Sicuri**: La struttura `File` fornisce un wrapper sicuro intorno agli handle di file grezzi.
- **RAII**: Gli handle di file vengono chiusi automaticamente quando escono dall'ambito tramite il tratto `Drop`.
- **Gestione degli Errori**: Utilizza `Result<T>` per tutte le operazioni che possono fallire, fornendo messaggi di errore descrittivi.
- **Praticità**: Include metodi statici per attività comuni come la lettura o la scrittura di un intero file in una singola chiamata.

## Utilizzo

```zc
import "std/fs.zc"

fn main() {
    // Lettura di base del file utilizzando RAII
    match File::read_all("config.txt") {
        Ok(content) => println "Configurazione: {content}",
        Err(e) => println "Errore durante la lettura della configurazione: {e}"
    }
    
    // Handle di file esplicito con chiusura automatica
    match File::open("data.log", "a") {
        Ok(file) => {
            file.write_string("Voce di log\n");
            // il file viene chiuso automaticamente qui
        }
        Err(e) => println "Impossibile aprire il log: {e}"
    }
}
```

## Definizioni delle Strutture

### `File`
Rappresenta un handle di file aperto.
```zc
struct File {
    handle: void*;
}
```

### `Metadata`
Metadati di file o directory.
```zc
struct Metadata {
    size: U64;
    is_dir: bool;
    is_file: bool;
}
```

### `DirEntry`
Rappresenta una voce in una directory.
```zc
struct DirEntry {
    name: String;
    is_dir: bool;
}
```

## Metodi

### Apertura / Chiusura

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **open** | `File::open(path: char*, mode: char*) -> Result<File>` | Apre un file in `path` con `mode`. |
| **close** | `close(self)` | Chiude esplicitamente l'handle del file. |

### Lettura / Scrittura

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **read_to_string** | `read_to_string(self) -> Result<String>` | Legge l'intero file in una `String`. |
| **read_all** | `File::read_all(path: char*) -> Result<String>` | Utilità statica per leggere completamente un file. |
| **read_lines** | `File::read_lines(path: char*) -> Result<Vec<String>>` | Utilità statica per leggere un file in un vettore di righe. |
| **write_string** | `write_string(self, content: char*) -> Result<bool>` | Scrive una stringa nel file. |
| **write_lines** | `File::write_lines(path: char*, lines: Vec<String>*) -> Result<bool>` | Utilità statica per scrivere un vettore di righe in un file. |

### Utilità per i Percorsi

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **exists** | `File::exists(path: char*) -> bool` | Restituisce true se il percorso esiste. |
| **current_dir** | `File::current_dir() -> Result<String>` | Restituisce il percorso assoluto della directory di lavoro corrente. |
| **metadata** | `File::metadata(path: char*) -> Result<Metadata>` | Recupera i metadati per il percorso specificato. |

### Operazioni su File e Directory

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **create_dir** | `File::create_dir(path: char*) -> Result<bool>` | Crea una nuova directory. |
| **remove_file** | `File::remove_file(path: char*) -> Result<bool>` | Elimina il file specificato. |
| **remove_dir** | `File::remove_dir(path: char*) -> Result<bool>` | Elimina la directory specificata (deve essere vuota). |
| **read_dir** | `File::read_dir(path: char*) -> Result<Vec<DirEntry>>` | Restituisce un elenco di voci in una directory. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **Tratto** | `impl Drop for File` | Chiude automaticamente l'handle del file quando esce dall'ambito. |
