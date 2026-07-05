+++
title = "6. Operators"
weight = 6
+++

# 6. Operators


Zen C supports operator overloading for user-defined structs by implementing specific method names.

#### Overloadable Operators

| Category | Operator | Method Name |
|:---|:---|:---|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **Comparison** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **Bitwise** | `&`, `\|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **Unary** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **Index** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

> **Note on String Equality**:
> - `string == string` performs **value comparison** (equivalent to `strcmp`).
> - `char* == char*` performs **pointer comparison** (checks memory addresses).
> - Mixed comparisons (e.g. `string == char*`) default to **pointer comparison**.

**Example:**
```zc
impl Point {
    fn add(self, other: Point) -> Point {
        return Point{x: self.x + other.x, y: self.y + other.y};
    }
}

let p3 = p1 + p2; // Calls p1.add(p2)
```

**Multi-Index Example:**
```zc
struct Matrix {
    data: int[9];
}

impl Matrix {
    fn get(self, row: int, col: int) -> int {
        return self.data[row * 3 + col];
    }
}

let m = Matrix{data: [1,0,0, 0,1,0, 0,0,1]};
let val = m[1, 2]; // Calls Matrix.get(m, 1, 2)
```

#### Syntactic Sugar

These operators are built-in language features and cannot be overloaded directly.

| Operator | Name | Description |
|:---|:---|:---|
| `\|>` | Pipeline | `x \|> f(y)` desugars to `f(x, y)` |
| `??` | Null Coalescing | `val ?? default` returns `default` if `val` is NULL (pointers) |
| `??=` | Null Assignment | `val ??= init` assigns if `val` is NULL |
| `?.` | Safe Navigation | `ptr?.field` accesses field only if `ptr` is not NULL |
| `?` | Try Operator | `res?` returns error if present (Result/Option types) |

**Auto-Dereference**:
Pointer field access (`ptr.field`) and method calls (`ptr.method()`) automatically dereference the pointer, equivalent to `(*ptr).field`.
