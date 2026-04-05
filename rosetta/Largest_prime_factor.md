+++
title = "Largest prime factor"
+++

# Largest prime factor

```zc
fn largest_prime_factor(n: u64) -> u64 {
    if n < 2 { return 1; }
    let inc: int[8] = [4, 2, 4, 2, 4, 6, 2, 6];
    let largest: u64;
    while n % 2 == 0 {
        largest = 2;
        n /= 2;
    }
    while n % 3 == 0 {
        largest = 3;
        n /= 3;
    }
    while n % 5 == 0 {
        largest = 5;
        n /= 5;
    }
    let k: u64 = 7;
    let i: usize = 0;
    while k * k <= n {
        if n % k == 0 {
            largest = k;
            n /= k;
        } else {
            k += inc[i];
            i = (i + 1) % 8;
        }
    }
    if n > 1 { largest = n; }
    return largest;
}

fn main() {
    let n: u64 = 600_851_475_143;
    println "{largest_prime_factor(n)}";
}
```

**Output:**

```
6857
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Largest prime factor**](https://rosettacode.org/wiki/Largest_prime_factor) in Zen C.

*This article uses material from the Rosetta Code article **Largest prime factor**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Largest_prime_factor?action=history).*
