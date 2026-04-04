# std/utf8

Il modulo `std/utf8` fornisce utilità per lavorare con i punti di codice Unicode (tipo `rune`) e la codifica UTF-8.

## Utilizzo

```zc
import "std/utf8.zc"

fn main() {
    let r = 'ñ';
    
    if (Utf8::is_alpha(r)) {
        println "{r} è una lettera";
    }
}
```

## Metodi

### Interrogazione e Identificazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **is_digit** | `is_digit(r: rune) -> bool` | Restituisce true se la rune è una cifra decimale (0-9). |
| **is_alpha** | `is_alpha(r: rune) -> bool` | Restituisce true se la rune è un carattere alfabetico. |
| **is_whitespace** | `is_whitespace(r: rune) -> bool` | Restituisce true se la rune è un carattere di spazio bianco. |
| **is_upper** | `is_upper(r: rune) -> bool` | Restituisce true se la rune è una lettera maiuscola. |
| **is_lower** | `is_lower(r: rune) -> bool` | Restituisce true se la rune è una lettera minuscola. |
| **is_valid** | `is_valid(data: char*, len: usize) -> bool` | Restituisce true se il buffer contiene dati UTF-8 validi. |

### Trasformazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **to_upper** | `to_upper(r: rune) -> rune` | Restituisce la versione maiuscola della rune. |
| **to_lower** | `to_lower(r: rune) -> rune` | Restituisce la versione minuscola della rune. |

### Codifica e Decodifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **encode** | `encode(r: rune, buf: char*) -> usize` | Codifica una rune in UTF-8. Restituisce i byte scritti (1-4). |
| **rune_len** | `rune_len(r: rune) -> usize` | Restituisce il numero di byte necessari per codificare la rune. |
| **decode** | `decode(data: char*, len: usize, consumed: usize*) -> rune` | Decodifica la prima sequenza UTF-8 dai dati. |
走
