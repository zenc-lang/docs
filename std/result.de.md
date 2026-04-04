# std/result

`Result<T>` ist der Standardtyp für die Fehlerbehandlung in Zen-C. Es repräsentiert entweder den Erfolg (`Ok`), der einen Wert vom Typ `T` enthält, oder ein Scheitern (`Err`), das eine String-Fehlermeldung enthält.

## Überblick

- **Sicher**: Erzwingt die explizite Handhabung von Erfolgs- und Fehlerpfaden.
- **Informativ**: `Err`-Fälle tragen eine beschreibende Fehlermeldung.
- **Generisch**: Unterstützt jeden Erfolgs-Werttyp `T`.
- **Integriert**: Arbeitet nahtlos mit `Result`-basierten Makros und Mustern für eine prägnante Fehlerfortpflanzung zusammen.

## Verwendung

```zc
import "std/result.zc"

fn divide(a: int, b: int) -> Result<int> {
    if (b == 0) {
        return Result<int>::Err("Division durch Null");
    }
    return Result<int>::Ok(a / b);
}

fn main() {
    match divide(10, 0) {
        Ok(val) => println "Ergebnis: {val}",
        Err(e)  => println "Fehler: {e}"
    }
}
```

## Struktur-Definition

```zc
struct Result<T> {
    is_ok: bool;
    val: T;
    err: char*;
}
```

## Methoden

### Konstruktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **Ok** | `Result<T>::Ok(v: T) -> Result<T>` | Erstellt ein Erfolgs-Ergebnis, das `v` enthält. |
| **Err** | `Result<T>::Err(e: char*) -> Result<T>` | Erstellt ein Fehler-Ergebnis mit der Meldung `e`. |

### Abfrage

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **is_ok** | `is_ok(self) -> bool` | Gibt `true` zurück, wenn das Ergebnis `Ok` ist. |
| **is_err** | `is_err(self) -> bool` | Gibt `true` zurück, wenn das Ergebnis `Err` ist. |

### Extraktion

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **unwrap** | `unwrap(self) -> T` | Gibt den Ok-Wert zurück. Löst Panic mit der Fehlermeldung aus, wenn `Err`. |
| **unwrap_ref** | `unwrap_ref(self) -> T*` | Gibt einen Zeiger auf den Ok-Wert zurück. Löst Panic aus, wenn `Err`. |
| **expect** | `expect(self, msg: char*) -> T` | Gibt den Wert zurück oder löst Panic mit `msg` und der Fehlermeldung aus, wenn `Err`. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **forget** | `forget(self)` | Setzt den Ok-Wert auf Null, ohne Destruktoren aufzurufen oder Speicher freizugeben. |
