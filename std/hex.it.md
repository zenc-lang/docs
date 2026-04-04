# std/encoding/hex

Il modulo `std/encoding/hex` fornisce utilità per la codifica e decodifica esadecimale dei dati.

## Panoramica

- **Codifica**: Converte i byte grezzi in una stringa esadecimale.
- **Decodifica**: Converte una stringa esadecimale nuovamente in byte grezzi (`Vec<u8>`).

## Utilizzo

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
        // Usa i byte...
    }
}
```

## Definizione della Struttura

```zc
struct Hex {}
```

## Metodi

### Metodi di `Hex`

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Codifica i dati grezzi in una stringa esadecimale. |
| **decode** | `Hex::decode(hex: String) -> Result<Vec<u8>>` | Decodifica una stringa esadecimale in un `Vec<u8>`. |
