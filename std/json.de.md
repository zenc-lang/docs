# std/json

Das Modul `std/json` bietet eine DOM-artige JSON-Parser- und Builder-Implementierung für Zen-C. Es zeichnet sich durch eine einfache API zum Erstellen, Bearbeiten und Serialisieren von JSON-Daten mit automatischer Speicherverwaltung aus.

## Überblick

- **DOM-artig**: Hierarchische Baumstruktur von `JsonValue`-Knoten.
- **Typsichere Accessoren**: Typen prüfen (`is_string`, `is_number`) und Werte sicher entpacken.
- **Automatische Bereinigung**: Implementiert das `Drop`-Trait für eine automatische, rekursive Speicherverwaltung.
- **Standardkonform**: Unterstützt standardmäßige JSON-Typen einschließlich Objekte, Arrays, Strings, Zahlen, Booleans und Null.

## Verwendung

```zc
import "std/json.zc"

fn main() {
    // JSON aufbauen
    let obj = JsonValue::object();
    obj.set("name", JsonValue::string("Alice"));
    obj.set("age", JsonValue::number(30.0));
    obj.set("active", JsonValue::bool(true));
    
    // Serialisierung
    let json_str = obj.to_string();
    println "Serialisiert: {json_str}";
    
    // Parsen
    let input = "{\"score\": 100}";
    match JsonValue::parse(input) {
        Ok(parsed) => {
            println "Punktzahl: {parsed.get(\"score\").unwrap().as_int().unwrap()}";
            // parsed wird am Ende dieses Blocks automatisch freigegeben
        }
        Err(e) => println "Fehler: {e}"
    }
} // obj wird hier automatisch freigegeben
```

## Struktur-Definition

```zc
struct JsonValue {
    kind: JsonType;
    // ... interne Felder
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **null** | `JsonValue::null() -> JsonValue` | Erstellt einen Null-Wert. |
| **bool** | `JsonValue::bool(b: bool) -> JsonValue` | Erstellt einen Booleschen Wert. |
| **number** | `JsonValue::number(n: double) -> JsonValue` | Erstellt einen numerischen Wert. |
| **string** | `JsonValue::string(s: char*) -> JsonValue` | Erstellt einen String-Wert. |
| **array** | `JsonValue::array() -> JsonValue` | Erstellt ein leeres JSON-Array. |
| **object** | `JsonValue::object() -> JsonValue` | Erstellt ein leeres JSON-Objekt. |

### Parsen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **parse** | `JsonValue::parse(json: char*) -> Result<JsonValue*>` | Parst einen JSON-String in einen auf dem Heap allokierten Baum. |

### Accessoren

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **is_null** | `is_null(self) -> bool` | Gibt wahr zurück, wenn der Typ Null ist. |
| **is_bool** | `is_bool(self) -> bool` | Gibt wahr zurück, wenn der Typ Boolesch ist. |
| **is_number** | `is_number(self) -> bool` | Gibt wahr zurück, wenn der Typ eine Zahl ist. |
| **is_string** | `is_string(self) -> bool` | Gibt wahr zurück, wenn der Typ ein String ist. |
| **is_array** | `is_array(self) -> bool` | Gibt wahr zurück, wenn der Typ ein Array ist. |
| **is_object** | `is_object(self) -> bool` | Gibt wahr zurück, wenn der Typ ein Objekt ist. |
| **as_string** | `as_string(self) -> Option<char*>` | Gibt den String-Zeiger zurück, falls zutreffend. |
| **as_int** | `as_int(self) -> Option<int>` | Gibt den Ganzzahlwert zurück, falls zutreffend. |
| **as_float** | `as_float(self) -> Option<double>` | Gibt den numerischen Wert zurück, falls zutreffend. |
| **as_bool** | `as_bool(self) -> Option<bool>` | Gibt den Booleschen Wert zurück, falls zutreffend. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **push** | `push(self, val: JsonValue)` | Fügt einem JSON-Array einen Kindwert hinzu. |
| **set** | `set(self, key: char*, val: JsonValue)` | Fügt ein Schlüssel-Wert-Paar in ein JSON-Objekt ein oder aktualisiert dieses. |
| **get** | `get(self, key: char*) -> Option<JsonValue*>` | Ruft einen Kindwert aus einem Objekt per Schlüssel ab. |
| **at** | `at(self, index: usize) -> Option<JsonValue*>` | Ruft einen Kindwert aus einem Array per Index ab. |

### Serialisierung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **to_string** | `to_string(self) -> String` | Gibt einen serialisierten JSON-String zurück. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den Wert und alle Nachfolgeknoten rekursiv frei. |
| **Trait** | `impl Drop for JsonValue` | Löst automatisch rekursives `free()` aus, wenn der Gültigkeitsbereich verlassen wird. |
