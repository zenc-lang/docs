+++
title = "2. Tipos Primitivos"
weight = 2
+++

# 2. Tipos Primitivos {#2-tipos-primitivos}


| Tipo | Equivalente em C | Descrição |
|:---|:---|:---|
| `int`, `uint` | `int`, `unsigned int` | Inteiro padrão da plataforma |
| `I8` .. `I128` ou `i8` .. `i128` | `int8_t` .. `__int128_t` | Inteiros sinalizados de tamanho fixo |
| `U8` .. `U128` ou `u8` .. `u128` | `uint8_t` .. `__uint128_t` | Inteiros não-sinalizados de tamanho fixo |
| `isize`, `usize` | `ptrdiff_t`, `size_t` | Inteiros do tamanho de ponteiro |
| `byte` | `uint8_t` | Alias para U8 |
| `F32`, `F64` ou `f32`, `f64`  | `float`, `double` | Números de ponto flutuante |
| `bool` | `bool` | `true` (verdadeiro) ou `false` (falso) |
| `char` | `char` | Caractere único |
| `string` | `char*` | C-string (terminada em NULL) |
| `U0`, `u0`, `void` | `void` | Tipo vazio |
| `iN` (ex. `i256`) | `_BitInt(N)` | Inteiro com sinal de largura arbitrária (C23) |
| `uN` (ex. `u42`) | `unsigned _BitInt(N)` | Inteiro sem sinal de largura arbitrária (C23) |
| `rune` | `uint32_t` | Valor escalar Unicode (ponto de código UTF-32) |

#### Literais
- **Inteiros**: Decimal (`123`), Hex (`0xFF`), Octal (`0o755`), Binário (`0b1011`).
  - *Nota*: Números com zeros à esquerda são tratados como decimais (`0123` é `123`), diferente de C.
  - *Nota*: Números podem conter sublinhados para legibilidade (`1_000_000`, `0b_1111_0000`).
- **Flutuantes**: Padrão (`3.14`), Científico (`1e-5`, `1.2E3`). Números de ponto flutuante também suportam sublinhados (`3_14.15_92`).

#### Unicode e Runas

O Zen C fornece suporte de primeira classe para valores escalares Unicode via o tipo `rune`. Uma `rune` representa um único ponto de código Unicode (codificado como um inteiro não assinalado de 32 bits).

| Literal | Descrição |
|:---|:---|
| `'a'` | Caractere ASCII padrão |
| `'🚀'` | Caractere Unicode multi-byte |
| `'\u{2764}'` | Sequência de escape Unicode (Hex) |

```zc
import "std.zc"

fn main() {
    let c = 'a';
    println "O caractere '{c}' tem um código de {(int)c} em ASCII/Unicode";

    let codigo = 97;
    println "O código {codigo} corresponde ao caractere {(char)codigo}";

    let r: rune = '🚀';
    println "A runa '{r}' tem um código de {(uint)r} em Unicode";
    
    let r_code: uint = 128640;
    println "O código {r_code} corresponde à runa '{(rune)r_code}'";

    let r_esc: rune = '\u{2764}';
    println "A runa '{r_esc}' tem código {(uint)r_esc} (0x{(uint)r_esc:X})";
}
```
