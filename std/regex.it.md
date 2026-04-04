# std/regex

Il modulo `std/regex` fornisce il supporto alle espressioni regolari basato su `regex.h` di POSIX.

## Utilizzo

```zc
import "std/regex.zc"

fn main() {
    if regex_match("^[a-z]+$", "ciao") {
        println "Corrispondenza trovata!";
    }
    
    let re = Regex::compile("\\d+");
    let conteggio = re.count("123 abc 456");
    re.destroy();
}
```

## Definizioni delle Strutture

### `Regex`

Rappresenta un'espressione regolare compilata.

```zc
struct Regex {
    // Handle interni
}
```

### `Match`

Rappresenta una corrispondenza (match) riuscita dell'espressione regolare.

```zc
struct Match {
    text: char*;
    start: int;
    len: int;
}
```

## Metodi

### Costruzione dell'Espressione Regolare

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **compile** | `Regex::compile(pattern: char*) -> Regex` | Compila un pattern regex con i flag predefiniti. |
| **compile_with_flags** | `Regex::compile_with_flags(pattern: char*, flags: int) -> Regex` | Compila con flag POSIX personalizzati. |
| **destroy** | `destroy(self)` | Libera la regex compilata. |

### Corrispondenza e Ricerca

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **match** | `match(self, text: char*) -> bool` | Restituisce true se il pattern trova una corrispondenza in qualsiasi punto di `text`. |
| **find** | `find(self, text: char*) -> Option<Match>` | Restituisce la prima corrispondenza inclusi posizione e lunghezza. |
| **count** | `count(self, text: char*) -> int` | Restituisce il numero di corrispondenze non sovrapposte. |
| **split** | `split(self, text: char*) -> Vec<String>` | Suddivide il testo in base al pattern. |

### Accesso alla Corrispondenza

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **as_string** | `as_string(self) -> char*` | Restituisce un puntatore all'inizio della corrispondenza. |
| **end** | `end(self) -> int` | Restituisce l'indice dopo l'ultimo carattere della corrispondenza. |

### Funzioni di Supporto Statiche

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **regex_match** | `regex_match(pattern: char*, text: char*) -> bool` | Controllo rapido per una corrispondenza. |
| **regex_find** | `regex_find(pattern: char*, text: char*) -> Option<Match>` | Trova la prima corrispondenza. |
| **regex_count** | `regex_count(pattern: char*, text: char*) -> int` | Conta tutte le corrispondenze. |
| **regex_split** | `regex_split(pattern: char*, text: char*) -> Vec<String>` | Suddivide il testo in base al pattern. |
