# std/path

Il modulo `std/path` fornisce utilità cross-platform per la manipolazione dei percorsi del file system. Semplifica compiti comuni come l'unione di percorsi, l'estrazione di estensioni e la ricerca di directory superiori (parent).

## Panoramica

- **Cross-platform**: Gestisce correttamente sia le barre in avanti (/) che quelle all'indietro (\) durante la manipolazione.
- **Type-safe**: La struttura `Path` incapsula le informazioni sul percorso, distinguendole dalle normali stringhe.
- **Parsing Pratico**: Estrai facilmente componenti come `extension`, `file_name` e `parent`.
- **RAII**: La memoria viene gestita automaticamente tramite il tratto `Drop`.

## Utilizzo

```zc
import "std/path.zc"

fn main() {
    let p = Path::new("/home/utente");
    let percorso_completo = p.join("docs/file.txt");
    
    println "Percorso completo: {percorso_completo.c_str()}";
    
    match percorso_completo.extension() {
        Some(ext) => println "Estensione: {ext}",
        None => println "Nessuna estensione trovata"
    }
} // percorso_completo e p vengono liberati automaticamente qui
```

## Definizione della Struttura

```zc
struct Path {
    str: String;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Path::new(s: char*) -> Path` | Crea un nuovo `Path` da una stringa C. |
| **from_string** | `Path::from_string(s: String) -> Path` | Crea un `Path` prendendo la proprietà di una `String`. |
| **clone** | `clone(self) -> Path` | Restituisce una copia profonda del `Path`. |

### Manipolazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **join** | `join(self, other: char*) -> Path` | Aggiunge `other` al percorso utilizzando il separatore di directory corretto. |

### Parsing

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **extension** | `extension(self) -> Option<String>` | Restituisce l'estensione del file (senza il punto iniziale), se presente. |
| **file_name** | `file_name(self) -> Option<String>` | Restituisce il componente finale del percorso. |
| **parent** | `parent(self) -> Option<Path>` | Restituisce il percorso della directory superiore. |

### Accesso

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Restituisce la rappresentazione della stringa C sottostante. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente la memoria della stringa interna del percorso. |
| **Tratto** | `impl Drop for Path` | Chiama automaticamente `free()` quando esce dall'ambito. |
