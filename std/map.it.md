# std/map

`Map<V>` è un'implementazione di mappa hash generica che associa chiavi stringa a valori di tipo `V`.

## Utilizzo

```zc
import "std/map.zc"

fn main() {
    let m = Map<int>::new();
    
    m.put("uno", 1);
    m.put("due", 2);
    
    if (m.contains("uno")) {
        let val = m.get("uno");
        println "{val.unwrap()}";
    }
    
    m.remove("due");
} // m viene liberata automaticamente qui
```

## Definizione della Struttura

```zc
struct Map<V> {
    keys: char**;
    vals: V*;
    // ... campi interni
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Map<V>::new() -> Map<V>` | Crea una nuova mappa vuota. |

### Iterazione

Puoi iterare sulle coppie chiave-valore della mappa utilizzando un ciclo `for`.

```zc
let m = Map<int>::new();
m.put("a", 1);

for entry in m {
    println "Chiave: {entry.key}, Val: {entry.val}";
}
```

L'iteratore restituisce una struttura `MapEntry<V>`:
```zc
struct MapEntry<V> {
    key: char*;
    val: V;
}
```

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **put** | `put(self, key: char*, val: V)` | Inserisce o aggiorna una coppia chiave-valore. |
| **remove** | `remove(self, key: char*)` | Rimuove una chiave e il suo valore dalla mappa. |

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **get** | `get(self, key: char*) -> Option<V>` | Recupera il valore associato alla chiave. |
| **contains** | `contains(self, key: char*) -> bool` | Restituisce true se la chiave esiste. |
| **length** | `length(self) -> usize` | Restituisce il numero di elementi nella mappa. |
| **is_empty** | `is_empty(self) -> bool` | Restituisce true se la mappa è vuota. |
| **capacity** | `capacity(self) -> usize` | Restituisce la capacità corrente della mappa. |

### Supporti per l'Iterazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Controlla se un indice di slot grezzo è occupato. |
| **key_at** | `key_at(self, idx: usize) -> char*` | Ottiene la chiave all'indice dello slot grezzo. |
| **val_at** | `val_at(self, idx: usize) -> V` | Ottiene il valore all'indice dello slot grezzo. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera lo storage interno della mappa. **Nota**: Questo non libera i valori se sono puntatori/oggetti. |
| **Tratto** | `impl Drop for Map` | Chiama automaticamente `free()` quando esce dall'ambito. |
