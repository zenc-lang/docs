+++
title = "Multifactorial"
+++

# Multifactorial

{{trans|Wren}}

```zc
fn mf(n: int, d: int) -> int {
    let prod  = 1;
    while n > 1 {
        prod *= n;
        n -= d;
    }
    return prod;
}

fn main() {
    for d in 1..=5 {
        print "degree {d}: ";
        for n in 1..=10 { print "{mf(n, d):8d}"; }
        println "";
    }
}
```

**Output:**

```
degree 1:        1       2       6      24     120     720    5040   40320  362880 3628800
degree 2:        1       2       3       8      15      48     105     384     945    3840
degree 3:        1       2       3       4      10      18      28      80     162     280
degree 4:        1       2       3       4       5      12      21      32      45     120
degree 5:        1       2       3       4       5       6      14      24      36      50
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Multifactorial**](https://rosettacode.org/wiki/Multifactorial) in Zen C.

*This article uses material from the Rosetta Code article **Multifactorial**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Multifactorial?action=history).*
