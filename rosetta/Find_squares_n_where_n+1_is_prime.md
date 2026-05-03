+++
title = "Find squares n where n+1 is prime"
+++

# Find squares n where n+1 is prime

```zc
import "std/math.zc"

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
    let limit: const int = (int)Math::sqrt(1000.0);
    let i = 1;
    let count = 0;
    println "Square numbers 'n' where 'n + 1' is prime: ";
    while i <= limit {
        let n = i * i;
        if is_prime(n + 1) {
            print "{n}, ";
            count++;
        }
        i = (i == 1) ? 2 : i + 2;
    }
    println "\b\b \n\nFound {count} such numbers."
}
```

**Output:**

```
Square numbers 'n' where 'n + 1' is prime: 
1, 4, 16, 36, 100, 196, 256, 400, 576, 676  

Found 10 such numbers.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Find squares n where n+1 is prime**](https://rosettacode.org/wiki/Find_squares_n_where_n+1_is_prime) in Zen C.

*This article uses material from the Rosetta Code article **Find squares n where n+1 is prime**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Find_squares_n_where_n+1_is_prime?action=history).*
