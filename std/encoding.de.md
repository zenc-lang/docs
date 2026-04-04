# std/encoding

Das Modul `std/encoding` bietet Hilfsprogramme zur Datenkodierung und -dekodierung.

## Base64 (`std/encoding/base64.zc`)

Base64-Kodierungsimplementierung (RFC 4648).

### Verwendung

```zc
import "std/encoding/base64.zc"

fn main() {
    let data = "Hello";
    let encoded = Base64::encode((u8*)data, 5);
    // encoded ist "SGVsbG8="
}
```

### Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **encode** | `Base64::encode(data: u8*, len: usize) -> char*` | Kodiert Daten in einen Base64-String. |
| **decode** | `Base64::decode(s: char*) -> Vec<u8>` | Dekodiert einen Base64-String in rohe Bytes. |

## Hex (`std/encoding/hex.zc`)

Hexadezimale Kodierung und Dekodierung.

### Verwendung

```zc
import "std/encoding/hex.zc"

fn main() {
    let data = "Zen";
    let encoded = Hex::encode((u8*)data, 3);
    // encoded ist "5a656e"
}
```

### Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Kodiert Daten in einen Hex-String. |
| **decode** | `Hex::decode(hex: String) -> Result<Vec<u8>>` | Dekodiert einen Hex-String in rohe Bytes. |
