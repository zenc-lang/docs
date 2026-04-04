# std/json

Il modulo `std/json` fornisce un'implementazione di parser e builder JSON in stile DOM per Zen-C. Presenta un'API semplice per la creazione, manipolazione e serializzazione di dati JSON con gestione automatica della memoria.

## Panoramica

- **Stile DOM**: Struttura ad albero gerarchica di nodi `JsonValue`.
- **Accessi Type-safe**: Controlla i tipi (`is_string`, `is_number`) ed estrai i valori in modo sicuro.
- **Pulizia Automatica**: Implementa il tratto `Drop` per una gestione della memoria automatica e ricorsiva.
- **Conforme agli Standard**: Supporta i tipi JSON standard inclusi oggetti, array, stringhe, numeri, booleani e null.

## Utilizzo

```zc
import "std/json.zc"

fn main() {
    // Costruzione del JSON
    let obj = JsonValue::object();
    obj.set("name", JsonValue::string("Alice"));
    obj.set("age", JsonValue::number(30.0));
    obj.set("active", JsonValue::bool(true));
    
    // Serializzazione
    let json_str = obj.to_string();
    println "Serializzato: {json_str}";
    
    // Parsing
    let input = "{\"score\": 100}";
    match JsonValue::parse(input) {
        Ok(parsed) => {
            println "Punteggio: {parsed.get(\"score\").unwrap().as_int().unwrap()}";
            // parsed viene liberato automaticamente alla fine di questo blocco
        }
        Err(e) => println "Errore: {e}"
    }
} // obj viene liberato automaticamente qui
```

## Definizione della Struttura

```zc
struct JsonValue {
    kind: JsonType;
    // ... campi interni
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **null** | `JsonValue::null() -> JsonValue` | Crea un valore null. |
| **bool** | `JsonValue::bool(b: bool) -> JsonValue` | Crea un valore booleano. |
| **number** | `JsonValue::number(n: double) -> JsonValue` | Crea un valore numerico. |
| **string** | `JsonValue::string(s: char*) -> JsonValue` | Crea un valore stringa. |
| **array** | `JsonValue::array() -> JsonValue` | Crea un array JSON vuoto. |
| **object** | `JsonValue::object() -> JsonValue` | Crea un oggetto JSON vuoto. |

### Parsing

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **parse** | `JsonValue::parse(json: char*) -> Result<JsonValue*>` | Esegue il parsing di una stringa JSON in un albero allocato nell'heap. |

### Accessori

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **is_null** | `is_null(self) -> bool` | Restituisce true se il tipo è null. |
| **is_bool** | `is_bool(self) -> bool` | Restituisce true se il tipo è booleano. |
| **is_number** | `is_number(self) -> bool` | Restituisce true se il tipo è un numero. |
| **is_string** | `is_string(self) -> bool` | Restituisce true se il tipo è una stringa. |
| **is_array** | `is_array(self) -> bool` | Restituisce true se il tipo è un array. |
| **is_object** | `is_object(self) -> bool` | Restituisce true se il tipo è un oggetto. |
| **as_string** | `as_string(self) -> Option<char*>` | Restituisce il puntatore alla stringa se applicabile. |
| **as_int** | `as_int(self) -> Option<int>` | Restituisce il valore intero se applicabile. |
| **as_float** | `as_float(self) -> Option<double>` | Restituisce il valore numerico se applicabile. |
| **as_bool** | `as_bool(self) -> Option<bool>` | Restituisce il valore booleano se applicabile. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **push** | `push(self, val: JsonValue)` | Aggiunge un valore figlio ad un array JSON. |
| **set** | `set(self, key: char*, val: JsonValue)` | Inserisce o aggiorna una coppia chiave-valore in un oggetto JSON. |
| **get** | `get(self, key: char*) -> Option<JsonValue*>` | Recupera un valore figlio da un oggetto tramite chiave. |
| **at** | `at(self, index: usize) -> Option<JsonValue*>` | Recupera un valore figlio da un array tramite indice. |

### Serializzazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> String` | Restituisce una stringa JSON serializzata. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera ricorsivamente il valore e tutti i nodi discendenti. |
| **Tratto** | `impl Drop for JsonValue` | Innesca automaticamente la `free()` ricorsiva quando esce dall'ambito. |
