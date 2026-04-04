# std/encoding/hex

El módulo `std/encoding/hex` proporciona utilidades para la codificación y decodificación hexadecimal de datos.

## Resumen

- **Codificación**: Convierte bytes crudos en una cadena hexadecimal.
- **Decodificación**: Convierte una cadena hexadecimal de nuevo en bytes crudos (`Vec<u8>`).

## Uso

```zc
import "std/encoding/hex.zc"
import "std/io.zc"

fn main() {
    let data = "Hola";
    let encoded = Hex::encode((u8*)data, 5);
    println "Hex: {encoded}"; // 48656c6c6f
    
    let decoded_res = Hex::decode(encoded);
    if (decoded_res.is_ok()) {
        let bytes = decoded_res.unwrap();
        // Usar bytes...
    }
}
```

## Definición de Estructura

```zc
struct Hex {}
```

## Métodos

### Métodos de `Hex`

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Codifica datos crudos en una cadena hexadecimal. |
| **decode** | `Hex::decode(hex: String) -> Result<Vec<u8>>` | Decodifica una cadena hexadecimal en un `Vec<u8>`. |
