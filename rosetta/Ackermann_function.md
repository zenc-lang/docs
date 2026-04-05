+++
title = "Ackermann function"
+++

# Ackermann function

```zc
fn ackermann(m: int, n: int) -> int {
    if m == 0 {
        return n + 1;
    }
    if m > 0 && n == 0 {
        return ackermann(m - 1, 1);
    }
    return ackermann(m - 1, ackermann(m, n - 1));
}

fn main() {
    // Test the function for small values... 
    for let m = 0; m <= 3; m += 1 {
        for let n = 0; n <= 4; n += 1 {
            let a = ackermann(m, n);
            println "A({m}, {n}) = {a}";
        }
    }
}
```

**Output:**

```
A(0, 0) = 1
A(0, 1) = 2
A(0, 2) = 3
A(0, 3) = 4
A(0, 4) = 5
A(1, 0) = 2
A(1, 1) = 3
A(1, 2) = 4
A(1, 3) = 5
A(1, 4) = 6
A(2, 0) = 3
A(2, 1) = 5
A(2, 2) = 7
A(2, 3) = 9
A(2, 4) = 11
A(3, 0) = 5
A(3, 1) = 13
A(3, 2) = 29
A(3, 3) = 61
A(3, 4) = 125
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Ackermann function**](https://rosettacode.org/wiki/Ackermann_function) in Zen C.

*This article uses material from the Rosetta Code article **Ackermann function**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Ackermann_function?action=history).*
