# std/arena

Il modulo `std/arena` fornisce un allocatore "bump" veloce per allocazioni di memoria di massa. Tutta la memoria allocata all'interno di un'arena viene liberata in un colpo solo quando l'arena stessa viene distrutta o resettata.

## Panoramica

- **Prestazioni**: Le allocazioni sono estremamente veloci, comportando solo un singolo incremento di puntatore.
- **Liberazione di Massa**: Ideale per allocazioni locali ad un task o ad una richiesta dove tutto può essere liberato contemporaneamente.
- **Salvataggio/Ripristino**: Supporto per "checkpoint" per liberare parzialmente la memoria all'interno dell'arena.
- **RAII**: Implementa il tratto `Drop` per garantire che il buffer sottostante venga liberato automaticamente.

## Utilizzo

```zc
import "std/arena.zc"

struct Node {
    val: int;
}

fn main() {
    // Crea un'arena con 1KB di capacità
    let a = Arena::new(1024);
    
    // Allocazioni veloci
    let n1 = a.alloc<Node>();
    let n2 = a.alloc<Node>();
    
    // Duplica una stringa nella memoria dell'arena
    let s = a.dup_str("Hello World");
    
    println "Arena utilizzata: {a.bytes_used()} byte";
    
    // Tutto viene liberato automaticamente quando 'a' esce dall'ambito
}
```

## Definizione della Struttura

```zc
struct Arena {
    data: void*;
    capacity: usize;
    used: usize;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `Arena::new(cap: usize) -> Arena` | Crea una nuova arena con la capacità specificata. |

### Allocazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **alloc\<T>** | `alloc<T>(self) -> T*` | Alloca e inizializza a zero la memoria per un tipo `T`. |
| **alloc_n\<T>**| `alloc_n<T>(self, count: usize) -> T*` | Alloca memoria per un array di `count` elementi di tipo `T`. |
| **alloc_bytes**| `alloc_bytes(self, size: usize) -> void*` | Allocazione di byte grezzi (allineata a 8 byte). |
| **dup_str** | `dup_str(self, src: char*) -> char*` | Duplica una stringa C nell'arena. |

### Interrogazione e Controllo

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **bytes_used** | `bytes_used(self) -> usize` | Restituisce i byte totali attualmente allocati. |
| **bytes_free** | `bytes_free(self) -> usize` | Restituisce la capacità rimanente. |
| **save** | `save(self) -> usize` | Restituisce un "checkpoint" che rappresenta l'utilizzo corrente. |
| **restore** | `restore(self, mark: usize)` | Libera parzialmente fino a un checkpoint precedente. |
| **reset** | `reset(self)` | Libera tutte le allocazioni resettando l'utilizzo a zero (il buffer viene mantenuto). |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera esplicitamente il buffer dell'arena sottostante. |
| **Tratto** | `impl Drop for Arena` | Chiama automaticamente `free()` quando l'arena esce dall'ambito. |
