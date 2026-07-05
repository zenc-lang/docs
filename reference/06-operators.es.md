+++
title = "6. Operadores"
weight = 6
+++

# 6. Operadores {#6-operadores}


Zen C soporta la sobrecarga de operadores para structs definidos por el usuario implementando nombres de métodos específicos.

#### Operadores Sobrecargables

| Categoría | Operador | Nombre del Método |
|:---|:---|:---|
| **Aritméticos** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **Comparación** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **Bitwise** | `&`, `|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **Unarios** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **Índice** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

> **Nota sobre la igualdad de cadenas**:
> - `string == string` realiza una **comparación de valores** (equivalente a `strcmp`).
> - `char* == char*` realiza una **comparación de punteros** (comprueba direcciones de memoria).
> - Comparaciones mixtas (ej. `string == char*`) por defecto realizan una **comparación de punteros**.

**Ejemplo:**
```zc
impl Point {
    fn add(self, other: Point) -> Point {
        return Point{x: self.x + other.x, y: self.y + other.y};
    }
}

let p3 = p1 + p2; // Llama a p1.add(p2)
```

**Ejemplo Multi-Índice:**
```zc
struct Matriz {
    data: int[9];
}

impl Matriz {
    fn get(self, fila: int, col: int) -> int {
        return self.data[fila * 3 + col];
    }
}

let m = Matriz{data: [1,0,0, 0,1,0, 0,0,1]};
let val = m[1, 2]; // Llama a Matriz.get(m, 1, 2)
```

#### Azúcar Sintáctico

Estos operadores son características integradas del lenguaje y no pueden sobrecargarse directamente.

| Operador | Nombre | Descripción |
|:---|:---|:---|
| `|>` | Pipeline | `x |> f(y)` se desazucara a `f(x, y)` |
| `??` | Null Coalescing | `val ?? default` retorna `default` si `val` es NULL (punteros) |
| `??=` | Null Assignment | `val ??= init` asigna si `val` es NULL |
| `?.` | Navegación Segura | `ptr?.campo` accede al campo solo si `ptr` no es NULL |
| `?` | Operador Try | `res?` retorna el error si está presente (tipos Result/Option) |

**Auto-Dereferencia**:
El acceso a campos por puntero (`ptr.campo`) y las llamadas a métodos (`ptr.metodo()`) dereferencian automáticamente el puntero, equivalente a `(*ptr).campo`.
