# std/encoding

O módulo `std/encoding` fornece utilitários para conversão entre diferentes formatos de representação de dados, como Base64.

## Uso

```zc
import "std/encoding/base64.zc"

fn main() {
    let original = "Zen-C";
    let encoded = Base64::encode(original);
    
    println "Base64: {encoded}"; 
}
```

## Base64 (`std/encoding/base64.zc`)

O submódulo Base64 fornece funções para codificar e decodificar dados binários no formato Base64 (RFC 4648).

### Funções

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **encode** | `Base64::encode(input: char*) -> String` | Codifica uma string C para Base64. |
| **decode** | `Base64::decode(input: char*) -> String` | Decodifica uma string Base64 de volta para o formato original. |

## Outros Encodings

O módulo `std/encoding` também pode incluir suporte para:
- **Hexadecimal**: Através do módulo `std/hex`.
- **JSON**: Através do módulo `std/json`.
- **UTF-8**: Através do módulo `std/utf8`.
走
