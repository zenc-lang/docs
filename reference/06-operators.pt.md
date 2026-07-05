+++
title = "6. Operadores"
weight = 6
+++

# 6. Operadores {#6-operadores}


Zen C suporta sobrecarga de operadores para structs definidos pelo usuário através da implementação de nomes específicos de métodos.

#### Operadores Sobrecarregáveis

| Categoria | Operador | Nome do Método |
|:---|:---|:---|
| **Aritmético** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **Comparação** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **Bitwise** | `&`, `\|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **Unário** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **Índice** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

{% alert(type="note") %}
**Nota sobre a Igualdade de Strings**:
- `string == string` performa uma **comparação de valores** (equivalente a `strcmp`).
- `char* == char*` performa **comparação de ponteiros** (checa os endereços da memória).
- Comparações mistas (e.g. `string == char*`) são **comparação de ponteiros** por padrão.
{% end %}

**Exemplo:**
```zc
impl Point {
    fn add(self, other: Point) -> Point {
        return Point{x: self.x + other.x, y: self.y + other.y};
    }
}

let p3 = p1 + p2; // Chama p1.add(p2)
```

**Exemplo Multi-Índice:**
```zc
struct Matriz {
    data: int[9];
}

impl Matriz {
    fn get(self, linha: int, col: int) -> int {
        return self.data[linha * 3 + col];
    }
}

let m = Matriz{data: [1,0,0, 0,1,0, 0,0,1]};
let val = m[1, 2]; // Chama Matriz.get(m, 1, 2)
```

#### Açúcar Sintático

Estes operadores são funcionalidades embutidas na linguagem e não podem ser sobrecarregados diretamente.

| Operador | Nome | Descrição |
|:---|:---|:---|
| `\|>` | Pipeline | `x \|> f(y)` des-açucara para `f(x, y)` |
| `??` | Coalescência Null | `val ?? default` retorna `default` se `val` for NULL (ponteiros) |
| `??=` | Atribuição Null | `val ??= init` atribui se `val` for NULL |
| `?.` | Navegação Segura | `ptr?.field` acessa o campo apenas se `ptr` não for NULL |
| `?` | Operador Try | `res?` retorna erro se presente (tipos Result/Option) |

**Auto-Deferência**:
Acesso a campos de ponteiro (`ptr.field`) e chamadas de métodos (`ptr.method()`) automaticamente dereferencia o ponteiro, equivalente a `(*ptr).field`.
