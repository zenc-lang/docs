# std/set

`Set<T>` è un'implementazione di set hash generico per la memorizzazione di valori univoci di tipo `T`. Utilizza una tabella hash ad indirizzamento aperto con scansione lineare (linear probing).

## Panoramica

- **Generico**: Memorizza qualsiasi tipo `T`.
- **Univoco**: Gestisce automaticamente i duplicati; l'aggiunta di un elemento esistente restituisce `false`.
- **Veloce**: Complessità temporale media O(1) per aggiunte, rimozioni e ricerche.
- **RAII**: Implementa il tratto `Drop` per la gestione automatica della memoria.

## Utilizzo

```zc
import "std/set.zc"

fn main() {
    let s = Set<int>::new();
    
    s.add(10);
    s.add(20);
    s.add(10); // Duplicato, restituisce false
    
    if (s.contains(10)) {
        println "Il set contiene 10";
    }
    
    s.remove(20);
    println "Lunghezza: {s.length()}";
} // s viene liberato automaticamente qui
```

## Definizione della Struttura

```zc
struct Set<T> {
    data: T*;
    len: usize;
    cap: usize;
    // ... campi interni
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Set<T>::new() -> Set<T>` | Crea un nuovo set vuoto. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **add** | `add(self, val: T) -> bool` | Aggiunge un valore al set. Restituisce `true` se aggiunto, `false` se già presente. |
| **remove** | `remove(self, val: T) -> bool` | Rimuove un valore dal set. Restituisce `true` se presente e rimosso. |
| **clear** | `clear(self)` | Rimuove tutti gli elementi dal set senza liberare la memoria allocata. |

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **contains** | `contains(self, val: T) -> bool` | Restituisce `true` se il valore esiste nel set. |
| **length** | `length(self) -> usize` | Restituisce il numero di elementi univoci. |
| **is_empty** | `is_empty(self) -> bool` | Restituisce `true` se il set non ha elementi. |
| **capacity** | `capacity(self) -> usize` | Restituisce la capacità interna corrente. |

### Utilità

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **is_slot_occupied** | `is_slot_occupied(self, idx: usize) -> bool` | Controlla se uno specifico slot hash interno è occupato. |
| **val_at** | `val_at(self, idx: usize) -> Option<T>` | Restituisce il valore in uno specifico slot interno, se presente. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente i buffer interni del set. |
| **Tratto** | `impl Drop for Set` | Chiama automaticamente `free()` quando il set esce dall'ambito. |
