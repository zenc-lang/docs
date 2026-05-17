+++
title = "Sudan function"
+++

# Sudan function

{{trans|Wren}}

```zc
fn F(n: int, x: int, y: int) -> int {
    if n == 0 { return x + y; }
    if y == 0 { return x; }
    return F(n - 1, F(n, x, y - 1), F(n, x, y - 1) + y);
}

fn main() {
    for n in 0..2 {
        println "Values of F({n}, x, y):";
        println "y/x    0   1   2   3   4   5";
        println "----------------------------";
        for y in 0..7 {
            print "{y}  |";
            for x in 0..6 {
                let sudan = F(n, x, y);
                print "{sudan:4d}";
            }
            println "";
        }
        println "";
    }
    println "F(2, 1, 1) = {F(2, 1, 1)}";
    println "F(3, 1, 1) = {F(3, 1, 1)}";
    println "F(2, 2, 1) = {F(2, 2, 1)}";
}
```

**Output:**

```
Values of F(0, x, y):
y/x    0   1   2   3   4   5
----------------------------
0  |   0   1   2   3   4   5
1  |   1   2   3   4   5   6
2  |   2   3   4   5   6   7
3  |   3   4   5   6   7   8
4  |   4   5   6   7   8   9
5  |   5   6   7   8   9  10
6  |   6   7   8   9  10  11

Values of F(1, x, y):
y/x    0   1   2   3   4   5
----------------------------
0  |   0   1   2   3   4   5
1  |   1   3   5   7   9  11
2  |   4   8  12  16  20  24
3  |  11  19  27  35  43  51
4  |  26  42  58  74  90 106
5  |  57  89 121 153 185 217
6  | 120 184 248 312 376 440

F(2, 1, 1) = 8
F(3, 1, 1) = 10228
F(2, 2, 1) = 27
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sudan function**](https://rosettacode.org/wiki/Sudan_function) in Zen C.

*This article uses material from the Rosetta Code article **Sudan function**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sudan_function?action=history).*
