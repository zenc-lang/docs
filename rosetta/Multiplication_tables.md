+++
title = "Multiplication tables"
+++

# Multiplication tables

{{trans|C}}

```zc
fn main() {
    let n: const int = 12;
    for j in 1..=n { printf("%3d%c", j, j != n ? ' ' : '\n'); }
    for j in 0..=n { printf(j != n ? "----" : "+\n"); }

    for i in 1..=n {
        for j in 1..=n {
		    printf(j < i ? "  - " : "%3d ", i * j);
        }
        printf("| %d\n", i);
    }
}
```

**Output:**

```
1   2   3   4   5   6   7   8   9  10  11  12
------------------------------------------------+
  1   2   3   4   5   6   7   8   9  10  11  12 | 1
  -   4   6   8  10  12  14  16  18  20  22  24 | 2
  -   -   9  12  15  18  21  24  27  30  33  36 | 3
  -   -   -  16  20  24  28  32  36  40  44  48 | 4
  -   -   -   -  25  30  35  40  45  50  55  60 | 5
  -   -   -   -   -  36  42  48  54  60  66  72 | 6
  -   -   -   -   -   -  49  56  63  70  77  84 | 7
  -   -   -   -   -   -   -  64  72  80  88  96 | 8
  -   -   -   -   -   -   -   -  81  90  99 108 | 9
  -   -   -   -   -   -   -   -   - 100 110 120 | 10
  -   -   -   -   -   -   -   -   -   - 121 132 | 11
  -   -   -   -   -   -   -   -   -   -   - 144 | 12
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Multiplication tables**](https://rosettacode.org/wiki/Multiplication_tables) in Zen C.

*This article uses material from the Rosetta Code article **Multiplication tables**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Multiplication_tables?action=history).*
