# std/encoding/hex

Das Modul `std/encoding/hex` bietet Hilfsprogramme für die hexadezimale Kodierung und Dekodierung von Daten.

## Überblick

- **Kodierung**: Konvertiert rohe Bytes in einen Hexadezimal-String.
- **Dekodierung**: Konvertiert einen Hexadezimal-String zurück in rohe Bytes (`Vec<u8>`).

## Verwendung

```zc
import "std/encoding/hex.zc"
import "std/io.zc"

fn main() {
    let data = "Hello";
    let encoded = Hex::encode((u8*)data, 5);
    println "Hex: {encoded}"; // 48656c6c6f
    
    let decoded_res = Hex::decode(encoded);
    if (decoded_res.is_ok()) {
        let bytes = decoded_res.unwrap();
        // Bytes verwenden...
    }
}
```

## Struktur-Definition

```zc
struct Hex {}
```

## Methoden

### `Hex` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Kodiert Rohdaten in einen Hexadezimal-String. |
| **decode** | `Hex::decode(hex: String) -> Result<Vec<u8>>` | Dekodiert einen Hexadezimal-String in einen `Vec<u8>`. |
