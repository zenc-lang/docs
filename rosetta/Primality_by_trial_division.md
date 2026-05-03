+++
title = "Primality by trial division"
+++

# Primality by trial division

A 'cut-down' version of what we'd normally use to test for primality.

```zc
fn is_prime(n: int) -> bool {
    if n < 2 { return false; }
    if n % 2 == 0 { return n == 2; }
    for let p = 3; p * p <= n; p += 2 {
        if n % p == 0 { return false; }
    }
    return true;
}

fn main() {
    let tests = [2, 5, 12, 19, 57, 61, 97];
    println "Are the following prime?";
    for t in tests {
        println "{t:2d} -> {is_prime(t)}";
    }
}
```

**Output:**

```
Are the following prime?
 2 -> true
 5 -> true
12 -> false
19 -> true
57 -> false
61 -> true
97 -> true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Primality by trial division**](https://rosettacode.org/wiki/Primality_by_trial_division) in Zen C.

*This article uses material from the Rosetta Code article **Primality by trial division**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Primality_by_trial_division?action=history).*
