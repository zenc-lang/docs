+++
title = "6. Operatoren"
weight = 6
+++

# 6. Operatoren {#6-operatoren}


Zen C unterstützt Operatorüberladung für selbst definierte Strukturen, indem bestimmte Methodennamen implementiert werden.

#### Überladbare Operatoren

| Kategorie | Operator | Methodenname |
|:---|:---|:---|
| **Arithmetisch** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **Vergleich** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **Bitweise** | `&`, `\|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **Unary (einfach)** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **Indexzugriff** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

> **Hinweis zur String-Gleichheit**:
> - `string == string` führt einen **Wertvergleich** durch (entspricht `strcmp`).  
> - `char* == char*` führt einen **Zeigervergleich** durch (prüft Speicheradressen).  
> - Gemischte Vergleiche (z. B. `string == char*`) verwenden standardmäßig **Zeigervergleich**.

**Beispiel:**
```zc
impl Punkt {
    fn add(self, other: Punkt) -> Punkt {
        return Punkt{x: self.x + other.x, y: self.y + other.y};
    }
}

let p3 = p1 + p2; // Ruft p1.add(p2) auf
```

**Beispiel für Mehrfach-Index:**
```zc
struct Matrix {
    daten: int[9];
}

impl Matrix {
    fn get(self, zeile: int, spalte: int) -> int {
        return self.daten[zeile * 3 + spalte];
    }
}

let m = Matrix{daten: [1,0,0, 0,1,0, 0,0,1]};
let wert = m[1, 2]; // Ruft Matrix.get(m, 1, 2) auf
```

#### Syntaktischer Zucker

Diese Operatoren sind eingebaute Sprachfeatures und können nicht direkt überladen werden.

| Operator | Name | Beschreibung |
|:---|:---|:---|
| `\|>` | Pipeline | `x \|> f(y)` wird zu `f(x, y)` expandiert |
| `??` | Null-Koaleszenz | `wert ?? default` gibt `default` zurück, falls `wert` NULL ist (Zeiger) |
| `??=` | Null-Zuweisung | `wert ??= init` weist zu, falls `wert` NULL ist |
| `?.` | Safe Navigation | `ptr?.feld` greift nur auf `feld` zu, wenn `ptr` nicht NULL ist |
| `?` | Try-Operator | `res?` gibt einen Fehler zurück, falls vorhanden (Result/Option-Typen) |

**Auto-Dereferenzierung**:  
Der Zugriff auf Zeigerfelder (`ptr.feld`) und Methodenaufrufe (`ptr.methode()`) dereferenziert automatisch den Zeiger, entspricht `(*ptr).feld`.
