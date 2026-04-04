# std/encoding

El módulo `std/encoding` proporciona utilidades de codificación y decodificación de datos.

## Base64 (`std/encoding/base64.zc`)

Implementación de la codificación Base64 (RFC 4648).

### Uso

```zc
import "std/encoding/base64.zc"

fn main() {
    let data = "Hola";
    let encoded = Base64::encode((u8*)data, 5);
    // encoded es "SGVsbG8="
}
```

### Métodos

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **encode** | `Base64::encode(data: u8*, len: usize) -> char*` | Codifica datos en una cadena Base64. |
| **decode** | `Base64::decode(s: char*) -> Vec<u8>` | Decodifica una cadena Base64 en bytes crudos. |

## Hex (`std/encoding/hex.zc`)

Codificación y decodificación hexadecimal.

### Uso

```zc
import "std/encoding/hex.zc"

fn main() {
    let data = "Zen";
    let encoded = Hex::encode((u8*)data, 3);
    // encoded es "5a656e"
}
```

### Métodos

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Codifica datos en una cadena Hex. |
| **decode** | `Hex::decode(hex: String) -> Result<Vec<u8>>` | Decodifica una cadena Hex en bytes crudos. |
