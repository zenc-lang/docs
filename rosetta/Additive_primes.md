+++
title = "Additive primes"
+++

# Additive primes

```zc
fn digit_sum(n: int) -> int {
    let sum = 0;
    while n > 0 {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

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
    println "Additive primes less than 500:";
    let i = 2;
    let count = 0;
    while i < 500 {
        if is_prime(i) && is_prime(digit_sum(i)) {
            print "{i:3d}  ";
            if !(++count % 10) { println ""; }
        }
        i = (i > 2) ? i + 2 : 3;
    }
    println "\n\n{count} such primes found.";
}
```

**Output:**

```
Additive primes less than 500:
  2    3    5    7   11   23   29   41   43   47  
 61   67   83   89  101  113  131  137  139  151  
157  173  179  191  193  197  199  223  227  229  
241  263  269  281  283  311  313  317  331  337  
353  359  373  379  397  401  409  421  443  449  
461  463  467  487  

54 such primes found.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Additive primes**](https://rosettacode.org/wiki/Additive_primes) in Zen C.

*This article uses material from the Rosetta Code article **Additive primes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Additive_primes?action=history).*
