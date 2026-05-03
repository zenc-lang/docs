+++
title = "Piprimes"
+++

# Piprimes

```zc
fn is_prime(n: int) -> bool {
    if n < 2      { return false; }
    if n % 2 == 0 { return n == 2; }
    if n % 3 == 0 { return n == 3; }
    let d = 5;
    while d * d <= n {
        if n % d == 0 { return false; }
        d += 2;
        if n % d == 0 { return false; }
        d += 4;
    }
    return true;
}

fn main() {
    println "pi(n), the number of primes <= n, where n >= 1 and pi(n) < 22:";
    let n = 1;
    let count = 0;
    while count < 22 {
        print "{count:2d}  ";
        if !(n++ % 10) { println ""; }
        if is_prime(n) { count++; }
    }
    println "";
}
```

**Output:**

```
pi(n), the number of primes <= n, where n >= 1 and pi(n) < 22:
 0   1   2   2   3   3   4   4   4   4  
 5   5   6   6   6   6   7   7   8   8  
 8   8   9   9   9   9   9   9  10  10  
11  11  11  11  11  11  12  12  12  12  
13  13  14  14  14  14  15  15  15  15  
15  15  16  16  16  16  16  16  17  17  
18  18  18  18  18  18  19  19  19  19  
20  20  21  21  21  21  21  21
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Piprimes**](https://rosettacode.org/wiki/Piprimes) in Zen C.

*This article uses material from the Rosetta Code article **Piprimes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Piprimes?action=history).*
