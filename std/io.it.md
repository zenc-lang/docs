# std/io

Il modulo `std/io` fornisce funzionalità standard di input/output, inclusa la stampa formattata su stdout e la lettura robusta da stdin.

## Panoramica

- **Output Formattato**: Fornisce `print` e `println` con supporto per gli specificatori di formato in stile C (`%s`, `%d`, ecc.).
- **Formattazione delle Stringhe**: Molteplici opzioni per la formattazione in buffer statici, forniti dall'utente o allocati nell'heap.
- **Supporto Unicode**: Include `read_rune` per leggere singoli caratteri UTF-8 da stdin.
- **Utilità di Conversione**: Metodi semplici per convertire interi e rune in stringhe.

## Utilizzo

```zc
import "std/io.zc"

fn main() {
    // Stampa di base
    println("Ciao, %s!", "Zen-C");
    
    // Lettura di una riga di input
    print("Inserisci il tuo nome: ");
    autofree let name = readln();
    
    if name != NULL {
        println("Saluti, %s", name);
    }
}
```

## Metodi

### Output

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **print** | `print(fmt: char*, ...) -> int` | Stampa l'output formattato su stdout. |
| **println** | `println(fmt: char*, ...) -> int` | Stampa l'output formattato su stdout seguito da una nuova riga. |

### Input

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **readln** | `readln() -> char*` | Legge una riga da stdin. Restituisce una stringa allocata nell'heap (il chiamante deve liberarla). |
| **read_rune** | `read_rune() -> rune` | Legge un singolo carattere UTF-8 (runa) da stdin. |

### Formattazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **format** | `format(fmt: char*, ...) -> char*` | Formatta in un buffer statico interno. **Attenzione**: Non è thread-safe. |
| **format_into** | `format_into(buf: char*, size: usize, fmt: char*, ...) -> int` | Formatta in un buffer fornito dall'utente di dimensioni specifiche. |
| **format_new** | `format_new(fmt: char*, ...) -> char*` | Formatta in un nuovo buffer allocato nell'heap. Il chiamante deve liberarlo. |

### Conversione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **itos** | `itos(n: int) -> char*` | Converte `n` in una stringa in un buffer statico. |
| **itos_new** | `itos_new(n: int) -> char*` | Converte `n` in una stringa allocata nell'heap. |
| **utos** | `utos(n: uint) -> char*` | Converte `n` senza segno in una stringa in un buffer statico. |
