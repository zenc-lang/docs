+++
title = "Factorial"
+++

# Factorial

This implementation uses a recursive function and a ternary operator for concise control flow. It also uses the <code>i64</code> fixed-width integer type to accommodate larger results before overflowing.

```zc
fn factorial(n: i64) -> i64 {
    // Using a ternary operator for the base case
    return n <= 1 ? 1 : n * factorial(n - 1);
}

fn main() {
    for i in 0..=15 {
        let res = factorial(i);
        println "{i}! = {res}";
    }
}
```

**Output:**

```
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
11! = 39916800
12! = 479001600
13! = 6227020800
14! = 87178291200
15! = 1307674368000
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Factorial**](https://rosettacode.org/wiki/Factorial) in Zen C.

*This article uses material from the Rosetta Code article **Factorial**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Factorial?action=history).*
