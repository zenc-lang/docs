# std/hex

O módulo `std/hex` fornece funções utilitárias para conversão entre dados binários e as suas representações em strings hexadecimais.

## Uso

```zc
import "std/hex.zc"

fn main() {
    let raw: u8[3] = [0xDE, 0xAD, 0xBE];
    
    // Codificar para hexadecimal
    let encoded = Hex::encode(&raw[0], 3);
    println "Hex: {encoded}"; // "deadbe"
    
    // Decodificar de volta
    let decoded = Hex::decode(encoded.c_str());
}
```

## Métodos

### Codificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, len: usize) -> String` | Converte dados binários para uma string hexadecimal em minúsculas. |
| **encode_upper** | `Hex::encode_upper(data: u8*, len: usize) -> String` | Converte dados binários para uma string hexadecimal em maiúsculas. |

### Decodificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **decode** | `Hex::decode(s: char*) -> Vec<u8>` | Decodifica uma string hexadecimal de volta para dados binários originais. |

## Detalhes de Implementação

- **Encode**: Produz 2 caracteres por cada byte de entrada.
- **Decode**: Requer que a string de entrada tenha um comprimento par e contenha apenas caracteres hexadecimais válidos (`0-9`, `a-f`, `A-F`).
走
