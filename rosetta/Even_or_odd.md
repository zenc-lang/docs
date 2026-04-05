+++
title = "Even or odd"
+++

# Even or odd

```zc
fn is_even<T>(n: T) -> bool {
    return n & 1 == 0;
}

fn is_odd<T>(n: T) -> bool {
    return n & 1 == 1;
}

fn main() {
    let n1: i32 = 124;
    println "{n1} is even? {is_even(n1)}";
    println "{n1} is odd ? {is_odd(n1)}";
    println "";
    let n2: i64 = -1231231231231231237;
    println "{n2} is even? {is_even(n2)}";
    println "{n2} is odd ? {is_odd(n2)}";
}
```

**Output:**

```
124 is even? true
124 is odd ? false

-1231231231231231237 is even? false
-1231231231231231237 is odd ? true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Even or odd**](https://rosettacode.org/wiki/Even_or_odd) in Zen C.

*This article uses material from the Rosetta Code article **Even or odd**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Even_or_odd?action=history).*
