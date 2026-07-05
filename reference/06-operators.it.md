+++
title = "6. Operatori"
weight = 6
+++

# 6. Operatori {#6-operatori}


Zen C supporta l'overloading di operatori per gli struct definiti dall'utente per implementare nomi specifici di metodi.

#### Operatori Overload-abili

| Categoria | Operatore | Nome del Metodo |
|:---|:---|:---|
| **Aritmetico** | `+`, `-`, `*`, `/`, `%`, `**` | `add`, `sub`, `mul`, `div`, `rem`, `pow` |
| **Paragone** | `==`, `!=` | `eq`, `neq` |
| | `<`, `>`, `<=`, `>=` | `lt`, `gt`, `le`, `ge` |
| **Bitwise** | `&`, `\|`, `^` | `bitand`, `bitor`, `bitxor` |
| | `<<`, `>>` | `shl`, `shr` |
| **Unari** | `-` | `neg` |
| | `!` | `not` |
| | `~` | `bitnot` |
| **Indice** | `a[i]` | `get(a, i)` |
| | `a[i, j]` | `get(a, i, j)` |
| | `a[i] = v` | `set(a, i, v)` |

> **Nota sull'uguaglianza delle stringhe**:
> - `string == string` performa un controllo del **valore** (equivalente a `strcmp`).
> - `char* == char*` performa un controllo dei **puntatori** (controlla gli indirizzi di memoria).
> - Paragoni misti (e.g. `string == char*`) defaulta al controllo dei **pointer**.

**Esempio:**
```zc
impl Punto {
    fn add(self, altro: Punto) -> Punto {
        return Punto{x: self.x + altro.x, y: self.y + altro.y};
    }
}

let p3 = p1 + p2; // Chiama p1.somma(p2)
```

**Esempio Multi-Indice:**
```zc
struct Matrice {
    data: int[9];
}

impl Matrice {
    fn get(self, riga: int, col: int) -> int {
        return self.data[riga * 3 + col];
    }
}

let m = Matrice{data: [1,0,0, 0,1,0, 0,0,1]};
let val = m[1, 2]; // Chiama Matrice.get(m, 1, 2)
```

#### Zucchero Sintattico

Questi operatori sono funzionalità integrate del linguaggio e non è possibile overloadarli.

| Operatore | Nome | Descrizione |
|:---|:---|:---|
| `\|>` | Pipeline | `x \|> f(y)` viene dezuccherato a `f(x, y)` |
| `??` | Coalescenza nulla | `val ?? default` restituisce `default` se `val` è NULL (puntatori) |
| `??=` | Assegnazione nulla | `val ??= init` assegna se `val` è NULL |
| `?.` | Safe Navigation | `ptr?.campo` accede a 'campo' solo se `ptr` non è NULL |
| `?` | Try Operator | `res?` restituisce un errore se presente (tipi Result/Option) |

**Dereferenza Automatica**:
Pointer field access (`ptr.field`) and method calls (`ptr.method()`) automatically dereference the pointer, equivalent to `(*ptr).field`.
Accesso ai campi da un puntatore (`puntatore.campo`) e chiamate ai metodi (`puntatore.metodo()`) dereferenzano automaticamente il puntatore, ciò è equivalente a `(*puntatore).campo`
