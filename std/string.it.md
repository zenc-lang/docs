# std/string

`String` è un tipo di stringa allocata nell'heap e ridimensionabile. Avvolge un `Vec<char>` e garantisce la terminazione nulla per la compatibilità con il C.

## Utilizzo

```zc
import "std/string.zc"

fn main() {
    let s = String::from("Ciao");

    // L'aggiunta richiede un puntatore a un'altra String
    let parte = String::from(" Mondo");
    s.append(&parte);
    
    // Iterazione (consapevole di UTF-8)
    for c in s {
        println "{c}";
    }

    // Usa c_str() per stampare
    println "{s.c_str()}"; // Stampa "Ciao Mondo"
    
    if (s.starts_with("Ciao")) {
        // ...
    }
} // s viene liberata automaticamente qui
```

## Definizione della Struttura

```zc
struct String {
    vec: Vec<char>;
}
```

## Metodi

### Costruzione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **new** | `String::new(s: char*) -> String` | Crea una nuova String da una stringa C primitiva. |
| **from** | `String::from(s: char*) -> String` | Alias per `new`. |
| **from_rune** | `String::from_rune(r: rune) -> String` | Crea una nuova String da una singola `rune`. |
| **from_runes** | `String::from_runes(runes: rune*, count: usize) -> String` | Crea una nuova String da un array di `runes`. |
| **from_runes_vec** | `String::from_runes_vec(runes: Vec<rune>) -> String` | Crea una nuova String da un vettore di oggetti `rune`. |

### Modifica

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **append** | `append(self, other: String*)` | Aggiunge un'altra stringa a questa. |
| **append_c** | `append_c(self, s: char*)` | Aggiunge una stringa C letterale. |
| **push_rune** | `push_rune(self, r: rune)` | Aggiunge un singolo punto di codice Unicode (`rune`) alla stringa. |
| **insert_rune** | `insert_rune(self, idx: usize, r: rune)` | Inserisce una `rune` all' *indice di carattere* specificato. |
| **remove_rune_at** | `remove_rune_at(self, idx: usize) -> rune` | Rimuove e restituisce la `rune` all' *indice di carattere* specificato. |
| **reserve** | `reserve(self, cap: usize)` | Garantisce che la stringa abbia almeno `cap` caratteri di capacità. |
| **clear** | `clear(self)` | Pulisce la stringa. |

### Accesso e Interrogazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Restituisce il puntatore alla stringa C sottostante. |
| **length** | `length(self) -> usize` | Restituisce la lunghezza della stringa (escluso il terminatore nullo). |
| **is_empty** | `is_empty(self) -> bool` | Restituisce true se la lunghezza è 0. |
| **to_string** | `to_string(self) -> char*` | Mappa a `c_str()`. Usato per l'interpolazione `{var}`. |
| **starts_with** | `starts_with(self, prefix: char*) -> bool` | Controlla se la stringa inizia con il prefisso fornito. |
| **ends_with** | `ends_with(self, suffix: char*) -> bool` | Controlla se la stringa finisce con il suffisso fornito. |
| **contains** | `contains(self, target: char) -> bool` | Controlla se la stringa contiene il carattere fornito. |
| **contains_str** | `contains_str(self, target: char*) -> bool` | Controlla se la stringa contiene la sottostringa fornita. |
| **find** | `find(self, target: char) -> Option<usize>` | Restituisce l'indice della prima occorrenza del byte `target`. |
| **find_str** | `find_str(self, target: char*) -> Option<usize>` | Restituisce l'indice della prima occorrenza della sottostringa `target`. |
| **find_all_str** | `find_all_str(self, target: char*) -> Vec<usize>` | Restituisce un vettore contenente tutti gli indici in cui appare `target`. |
| **substring** | `substring(self, start: usize, len: usize) -> String` | Restituisce una nuova String contenente la sottostringa specificata. |

### Supporto UTF-8

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **utf8_len** | `utf8_len(self) -> usize` | Restituisce il numero di punti di codice Unicode (caratteri). |
| **utf8_at** | `utf8_at(self, idx: usize) -> String` | Restituisce il carattere all'indice specificato come una nuova String. |
| **utf8_get** | `utf8_get(self, idx: usize) -> rune` | Restituisce il carattere all'indice specificato come una `rune`. |
| **utf8_substr** | `utf8_substr(self, start_idx: usize, num_chars: usize) -> String` | Restituisce una sottostringa basata sugli indici dei caratteri. |
| **runes** | `runes(self) -> Vec<rune>` | Restituisce un vettore contenente tutti i punti di codice Unicode. |
| **chars** | `chars(self) -> StringCharsIter` | Restituisce un iteratore manuale che produce `Option<rune>`. |

### Trasformazioni

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **to_lowercase** | `to_lowercase(self) -> String` | Restituisce una nuova stringa convertita in minuscolo. |
| **to_uppercase** | `to_uppercase(self) -> String` | Restituisce una nuova stringa convertita in maiuscolo. |
| **split** | `split(self, delim: char) -> Vec<String>` | Suddivide la stringa in un vettore di sottostringhe. |
| **trim** | `trim(self) -> String` | Restituisce una nuova stringa con gli spazi bianchi iniziali/finali rimossi. |
| **replace** | `replace(self, target: char*, replacement: char*) -> String` | Restituisce una nuova stringa con le sostituzioni effettuate. |
| **pad_left** | `pad_left(self, target_len: usize, pad_char: char) -> String` | Restituisce una nuova stringa imbottita (padded) a sinistra. |
| **pad_right** | `pad_right(self, target_len: usize, pad_char: char) -> String` | Restituisce una nuova stringa imbottita (padded) a destra. |

### Confronto

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **eq** | `eq(self, other: String*) -> bool` | Controllo di uguaglianza strutturale. |
| **neq** | `neq(self, other: String*) -> bool` | Controllo di disuguaglianza strutturale. |
| **compare** | `compare(self, other: String*) -> int` | Confronto lessicale. |
| **compare_ignore_case** | `compare_ignore_case(self, other: String*) -> int` | Confronto lessicale case-insensitive. |
| **eq_ignore_case** | `eq_ignore_case(self, other: String*) -> bool` | Controllo di uguaglianza case-insensitive. |

## Operatori

| Operatore | Metodo | Descrizione |
| :--- | :--- | :--- |
| `+` | **add** | `s1 + &s2`. Concatena le stringhe in una nuova `String`. |
| `+=` | **add_assign** | `s1 += &s2`. Aggiunge `s2` a `s1` sul posto. |
| `==` | **eq** | `s1 == &s2`. Controllo di uguaglianza strutturale. |
| `!=` | **neq** | `s1 != &s2`. Controllo di disuguaglianza strutturale. |
| `<` | **lt** | `s1 < &s2`. Confronto lessicale. |
| `>` | **gt** | `s1 > &s2`. Confronto lessicale. |
| `<=` | **le** | `s1 <= &s2`. Confronto lessicale. |
| `>=` | **ge** | `s1 >= &s2`. Confronto lessicale. |
| `{}` | **to_string** | Utilizzato per l'interpolazione delle stringhe in `printf`/`println`. |

## Iterazione

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> StringCharsIter` | Restituisce un iteratore che produce `rune`. Usato da `for c in s`. |

## Gestione della Memoria

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **free** | `free(self)` | Libera manualmente la memoria della stringa. |
| **destroy** | `destroy(self)` | Alias per `free`. |
| **forget** | `forget(self)` | Impedisce la liberazione automatica (trasferimento di proprietà). |
| **Tratto** | `impl Drop for String` | Chiama automaticamente `free()` quando esce dall'ambito. |
