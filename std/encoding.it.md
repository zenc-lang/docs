# std/encoding

Il modulo `std/encoding` fornisce utilità per la codifica e decodifica dei dati.

## Base64 (`std/encoding/base64.zc`)

Implementazione della codifica Base64 (RFC 4648).

### Utilizzo

```zc
import "std/encoding/base64.zc"

fn main() {
    let data = "Hello";
    let encoded = Base64::encode((u8*)data, 5);
    // encoded è "SGVsbG8="
}
```

### Metodi

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **encode** | `Base64::encode(data: u8*, len: usize) -> char*` | Codifica i dati in una stringa Base64. |
| **decode** | `Base64::decode(s: char*) -> Vec<u8>` | Decodifica una stringa Base64 in byte grezzi. |

## Hex (`std/encoding/hex.zc`)

Codifica e decodifica esadecimale.

### Utilizzo

```zc
import "std/encoding/hex.zc"

fn main() {
    let data = "Zen";
    let encoded = Hex::encode((u8*)data, 3);
    // encoded è "5a656e"
}
```

### Metodi

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Codifica i dati in una stringa esadecimale. |
| **decode** | `Hex::decode(hex: String) -> Result<Vec<u8>>` | Decodifica una stringa esadecimale in byte grezzi. |
