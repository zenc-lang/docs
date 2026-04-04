# std/string

`String` ist ein wachsender, auf dem Heap allokierter String-Typ. Er kapselt ein `Vec<char>` ein und stellt die Null-Terminierung für die C-Kompatibilität sicher.

## Verwendung

```zc
import "std/string.zc"

fn main() {
    let s = String::from("Hallo");

    // Anhängen erfordert einen Zeiger auf einen anderen String
    let part = String::from(" Welt");
    s.append(&part);
    
    // Iteration (Unicode-bewusst)
    for c in s {
        println "{c}";
    }

    // c_str() zum Drucken verwenden
    println "{s.c_str()}"; // Druckt "Hallo Welt"
    
    if (s.starts_with("Hallo")) {
        // ...
    }
} // s wird hier automatisch freigegeben
```

## Struktur-Definition

```zc
struct String {
    vec: Vec<char>;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `String::new(s: char*) -> String` | Erstellt einen neuen String aus einem C-String-Primitiv. |
| **from** | `String::from(s: char*) -> String` | Alias für `new`. |
| **from_rune** | `String::from_rune(r: rune) -> String` | Erstellt einen neuen String aus einer einzelnen `rune`. |
| **from_runes** | `String::from_runes(runes: rune*, count: usize) -> String` | Erstellt einen neuen String aus einem Array von `runes`. |
| **from_runes_vec** | `String::from_runes_vec(runes: Vec<rune>) -> String` | Erstellt einen neuen String aus einem Vektor von `rune`-Objekten. |

### Modifikation

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **append** | `append(self, other: String*)` | Hängt einen anderen String an diesen an. |
| **append_c** | `append_c(self, s: char*)` | Hängt ein C-String-Literal an. |
| **push_rune** | `push_rune(self, r: rune)` | Hängt einen einzelnen Unicode-Codepunkt (`rune`) an den String an. |
| **insert_rune** | `insert_rune(self, idx: usize, r: rune)` | Fügt eine `rune` am angegebenen *Zeichen-Index* ein. |
| **remove_rune_at** | `remove_rune_at(self, idx: usize) -> rune` | Entfernt und gibt die `rune` am angegebenen *Zeichen-Index* zurück. |
| **reserve** | `reserve(self, cap: usize)` | Stellt sicher, dass der String eine Kapazität von mindestens `cap` Zeichen hat. |
| **clear** | `clear(self)` | Leert den String. |

### Zugriff & Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **c_str** | `c_str(self) -> char*` | Gibt den zugrunde liegenden C-String-Zeiger zurück. |
| **length** | `length(self) -> usize` | Gibt die Länge des Strings zurück (ohne Null-Terminator). |
| **is_empty** | `is_empty(self) -> bool` | Gibt wahr zurück, wenn die Länge 0 ist. |
| **to_string** | `to_string(self) -> char*` | Wird auf `c_str()` abgebildet. Wird für die `{var}` Interpolation verwendet. |
| **starts_with** | `starts_with(self, prefix: char*) -> bool` | Prüft, ob der String mit dem angegebenen Präfix beginnt. |
| **ends_with** | `ends_with(self, suffix: char*) -> bool` | Prüft, ob der String mit dem angegebenen Suffix endet. |
| **contains** | `contains(self, target: char) -> bool` | Prüft, ob der String das angegebene Zeichen enthält. |
| **contains_str** | `contains_str(self, target: char*) -> bool` | Prüft, ob der String den angegebenen Teilstring enthält. |
| **find** | `find(self, target: char) -> Option<usize>` | Gibt den Index des ersten Vorkommens des Bytes `target` zurück. |
| **find_str** | `find_str(self, target: char*) -> Option<usize>` | Gibt den Index des ersten Vorkommens des Teilstrings `target` zurück. |
| **find_all_str** | `find_all_str(self, target: char*) -> Vec<usize>` | Gibt einen Vektor mit allen Indizes zurück, an denen `target` vorkommt. |
| **substring** | `substring(self, start: usize, len: usize) -> String` | Gibt einen neuen String zurück, der den angegebenen Teilstring enthält. |

### UTF-8 Unterstützung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **utf8_len** | `utf8_len(self) -> usize` | Gibt die Anzahl der Unicode-Codepunkte (Zeichen) zurück. |
| **utf8_at** | `utf8_at(self, idx: usize) -> String` | Gibt das Zeichen am angegebenen Index als neuen String zurück. |
| **utf8_get** | `utf8_get(self, idx: usize) -> rune` | Gibt das Zeichen am angegebenen Index als `rune` zurück. |
| **utf8_substr** | `utf8_substr(self, start_idx: usize, num_chars: usize) -> String` | Gibt einen Teilstring basierend auf Zeichen-Indizes zurück. |
| **runes** | `runes(self) -> Vec<rune>` | Gibt einen Vektor zurück, der alle Unicode-Codepunkte enthält. |
| **chars** | `chars(self) -> StringCharsIter` | Gibt einen manuellen Iterator zurück, der `Option<rune>` liefert. |

### Transformationen

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **to_lowercase** | `to_lowercase(self) -> String` | Gibt einen neuen String in Kleinschreibung zurück. |
| **to_uppercase** | `to_uppercase(self) -> String` | Gibt einen neuen String in Großschreibung zurück. |
| **split** | `split(self, delim: char) -> Vec<String>` | Teilt den String in einen Vektor von Teilstrings auf. |
| **trim** | `trim(self) -> String` | Gibt einen neuen String zurück, bei dem führende/abschließende Leerzeichen entfernt wurden. |
| **replace** | `replace(self, target: char*, replacement: char*) -> String` | Gibt einen neuen String mit Ersetzungen zurück. |
| **pad_left** | `pad_left(self, target_len: usize, pad_char: char) -> String` | Gibt einen neuen links aufgefüllten String zurück. |
| **pad_right** | `pad_right(self, target_len: usize, pad_char: char) -> String` | Gibt einen neuen rechts aufgefüllten String zurück. |

### Vergleich

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **eq** | `eq(self, other: String*) -> bool` | Strukturelle Gleichheitsprüfung. |
| **neq** | `neq(self, other: String*) -> bool` | Strukturelle Ungleichheitsprüfung. |
| **compare** | `compare(self, other: String*) -> int` | Lexikalischer Vergleich. |
| **compare_ignore_case** | `compare_ignore_case(self, other: String*) -> int` | Fallunabhängiger lexikalischer Vergleich. |
| **eq_ignore_case** | `eq_ignore_case(self, other: String*) -> bool` | Fallunabhängige Gleichheitsprüfung. |

## Operatoren

| Operator | Methode | Beschreibung |
| :--- | :--- | :--- |
| `+` | **add** | `s1 + &s2`. Konkateniert Strings zu einem neuen `String`. |
| `+=` | **add_assign** | `s1 += &s2`. Hängt `s2` in-place an `s1` an. |
| `==` | **eq** | `s1 == &s2`. Strukturelle Gleichheitsprüfung. |
| `!=` | **neq** | `s1 != &s2`. Strukturelle Ungleichheitsprüfung. |
| `<` | **lt** | `s1 < &s2`. Lexikalischer Vergleich. |
| `>` | **gt** | `s1 > &s2`. Lexikalischer Vergleich. |
| `<=` | **le** | `s1 <= &s2`. Lexikalischer Vergleich. |
| `>=` | **ge** | `s1 >= &s2`. Lexikalischer Vergleich. |
| `{}` | **to_string** | Wird für die String-Interpolation in `printf`/`println` verwendet. |

## Iteration

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **iterator** | `iterator(self) -> StringCharsIter` | Gibt einen Iterator zurück, der `rune` liefert. Wird von `for c in s` verwendet. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt den Stringspeicher manuell frei. |
| **destroy** | `destroy(self)` | Alias für `free`. |
| **forget** | `forget(self)` | Verhindert die automatische Freigabe (Besitzübergabe). |
| **Trait** | `impl Drop for String` | Ruft beim Verlassen des Gültigkeitsbereichs automatisch `free()` auf. |
