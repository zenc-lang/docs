+++
title = "Tropical algebra overloading"
+++

# Tropical algebra overloading

{{trans|Wren}}

```zc
//> link: -lm
include <math.h>

def PLUS_INF  =  1.0 / 0.0;
def MINUS_INF = -1.0 / 0.0;

@derive(Copy)
struct MaxTropical {
    r: f64;
}

impl MaxTropical {
    fn new(r: f64) -> Self {
        assert(r != PLUS_INF && !isnan(r), "+inf and nan are not supported.\n");
        return MaxTropical{r: r};
    }

    fn eq(self, other: MaxTropical) -> bool {
        return self.r == other.r;
    }

    // equivalent to ⊕ operator
    fn add(self, other: MaxTropical) -> MaxTropical {
        if self.r  == MINUS_INF { return other; }
        if other.r == MINUS_INF { return *self; }
        return MaxTropical{r: fmax(self.r, other.r)};
    }

    // equivalent to ⊗ operator
    fn mul(self, other: MaxTropical) -> MaxTropical {
        if self.r  == 0.0 { return other; }
        if other.r == 0.0 { return *self; }
        return MaxTropical{r: self.r + other.r};
    }

    // exponentiation operator ^ (we would normally overload ** = pow)
    fn bitxor(self, e: uint) -> MaxTropical {
        let c = *self;
        if e == 1 { return c; }
        let p = *self;
        for i in 2..=e { p *= c; }
        return p;
    }

    fn to_string(self) -> string {
        return "{self.r:g}";
    }
}

fn btos(b: bool) -> string {
    return b ? "true" : "false";
}

fn main() {
    let data: f64[5][2] = [
        [2.0, -2.0],
        [-0.001, MINUS_INF],
        [0.0, MINUS_INF],
        [1.5, -1.0],
        [-0.5, 0.0]
    ];

    let ops = ["⊗", "⊕", "⊗", "⊕", "⊗"];

    for i in 0..5 {
        let a = MaxTropical::new(data[i][0]);
        let b = MaxTropical::new(data[i][1]);
        if ops[i] == "⊕" {
            println "{a} ⊕ {b} = {a + b}";
        } else {
            println "{a} ⊗ {b} = {a * b}";
        }
    }

    let c = MaxTropical::new(5.0);
    println "{c} ^ 7 = {c ^ 7}";

    let d = MaxTropical::new(8.0);
    let e = MaxTropical::new(7.0);
    let f = c * (d + e);
    let g = c * d + c * e;
    println "{c} ⊗ ({d} ⊕ {e}) = {f}";
    println "{c} ⊗ {d} ⊕ {c} ⊗ {e} = {g}";
    println "{c} ⊗ ({d} ⊕ {e}) == {c} ⊗ {d} ⊕ {c} ⊗ {e} is {btos(f == g)}";
}
```

**Output:**

```
2 ⊗ -2 = 0
-0.001 ⊕ -inf = -0.001
0 ⊗ -inf = -inf
1.5 ⊕ -1 = 1.5
-0.5 ⊗ 0 = -0.5
5 ^ 7 = 35
5 ⊗ (8 ⊕ 7) = 13
5 ⊗ 8 ⊕ 5 ⊗ 7 = 13
5 ⊗ (8 ⊕ 7) == 5 ⊗ 8 ⊕ 5 ⊗ 7 is true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Tropical algebra overloading**](https://rosettacode.org/wiki/Tropical_algebra_overloading) in Zen C.

*This article uses material from the Rosetta Code article **Tropical algebra overloading**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Tropical_algebra_overloading?action=history).*
