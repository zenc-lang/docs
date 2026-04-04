# std/option

`Option<T>` repräsentiert einen optionalen Wert: Jedes `Option` ist entweder `Some` und enthält einen Wert, oder `None`. Es wird häufig verwendet, um die Abwesenheit eines Wertes zu handhaben, ohne auf Null-Zeiger zurückgreifen zu müssen.

## Überblick

- **Sicher**: Fördert die explizite Handhabung des `None`-Falls.
- **Generisch**: Kann jeden Typ `T` kapseln.
- **Nullkosten**: Wird zu einer einfachen Struktur mit einem booleschen Flag kompiliert.
- **Praktisch**: Bietet viele Hilfsmethoden zum Entpacken und Transformieren von Werten.

## Verwendung

```zc
import "std/option.zc"

fn main() {
    let val = Option<int>::Some(10);
    
    if (val.is_some()) {
        println "Wert ist {val.unwrap()}";
    }
    
    let empty = Option<int>::None();
    let x = empty.unwrap_or(0);
}
```

## Struktur-Definition

```zc
struct Option<T> {
    is_some: bool;
    val: T;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **Some** | `Option<T>::Some(v: T) -> Option<T>` | Erstellt eine `Some`-Option, die `v` enthält. |
| **None** | `Option<T>::None() -> Option<T>` | Erstellt eine `None`-Option. |

### Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **is_some** | `is_some(self) -> bool` | Gibt `true` zurück, wenn die Option `Some` ist. |
| **is_none** | `is_none(self) -> bool` | Gibt `true` zurück, wenn die Option `None` ist. |

### Extraktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **unwrap** | `unwrap(self) -> T` | Gibt den enthaltenen Wert zurück. Löst Panic aus, wenn `None`. |
| **unwrap_ref** | `unwrap_ref(self) -> T*` | Gibt einen Zeiger auf den enthaltenen Wert zurück. Löst Panic aus, wenn `None`. |
| **unwrap_or** | `unwrap_or(self, def: T) -> T` | Gibt den enthaltenen Wert oder `def` zurück. |
| **expect** | `expect(self, msg: char*) -> T` | Gibt den Wert zurück oder löst Panic mit `msg` aus. |
| **or_else** | `or_else(self, other: Option<T>) -> Option<T>` | Gibt die Option zurück, wenn `Some`, andernfalls wird `other` zurückgegeben. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **forget** | `forget(self)` | Setzt den internen Wert auf Null, ohne Destruktoren aufzurufen oder Speicher freizugeben. |
