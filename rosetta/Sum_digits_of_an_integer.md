+++
title = "Sum digits of an integer"
+++

# Sum digits of an integer

```zc
fn digits_sum(n: int, b: const int) -> int {
    let sum = 0;
    while n > 0 {
        sum += n % b;
        n /= b;
    }
    return sum;
}

fn main() {
    let a: (int, int)[4] = [(1, 10), (1234, 10), (0xfe, 16), (0xf0e, 16)];
    for p in a {
        let (n, b) = p;
        println "{digits_sum(n, b)}";
    }
}
```

**Output:**

```
1
10
29
29
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sum digits of an integer**](https://rosettacode.org/wiki/Sum_digits_of_an_integer) in Zen C.

*This article uses material from the Rosetta Code article **Sum digits of an integer**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sum_digits_of_an_integer?action=history).*
