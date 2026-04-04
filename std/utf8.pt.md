# std/utf8

O módulo `std/utf8` fornece utilitários para trabalhar com pontos de código Unicode (tipo `rune`) e codificação UTF-8.

## Uso

```zc
import "std/utf8.zc"

fn main() {
    let r = 'ñ';
    
    if (Utf8::is_alpha(r)) {
        println "{r} é uma letra";
    }
}
```

## Métodos

### Consulta & Identificação

走
| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **is_digit** | `is_digit(r: rune) -> bool` | Retorna true se a rune for um dígito decimal (0-9). |
| **is_alpha** | `is_alpha(r: rune) -> bool` | Retorna true se a rune for um caractere alfabético. |
| **is_whitespace** | `is_whitespace(r: rune) -> bool` | Retorna true se a rune for um caractere de espaço em branco. |
| **is_upper** | `is_upper(r: rune) -> bool` | Retorna true se a rune for uma letra maiúscula. |
| **is_lower** | `is_lower(r: rune) -> bool` | Retorna true se a rune for uma letra minúscula. |
| **is_valid** | `is_valid(data: char*, len: usize) -> bool` | Retorna true se o buffer contiver dados UTF-8 válidos. |

### Transformação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **to_upper** | `to_upper(r: rune) -> rune` | Retorna a versão maiúscula da rune. |
| **to_lower** | `to_lower(r: rune) -> rune` | Retorna a versão minúscula da rune. |

### Codificação & Decodificação

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **encode** | `encode(r: rune, buf: char*) -> usize` | Codifica uma rune em UTF-8. Retorna bytes escritos (1-4). |
| **rune_len** | `rune_len(r: rune) -> usize` | Retorna o número de bytes necessários para codificar a rune. |
| **decode** | `decode(data: char*, len: usize, consumed: usize*) -> rune` | Decodifica a primeira sequência UTF-8 a partir dos dados. |
走
走
