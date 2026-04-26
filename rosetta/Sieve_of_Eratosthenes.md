+++
title = "Sieve of Eratosthenes"
+++

# Sieve of Eratosthenes

{{trans|Wren}}

```zc
import "std/vec.zc"

fn sieve_of_eratosthenes(n: int) -> Vec<int> {
    let primes = Vec<int>::new();
    if n < 2 { return primes; }
    autofree let comp = (bool*)calloc(n - 1, sizeof(bool));
    let p = 2;
    loop {
        let p2 = p * p;
        if p2 > n { break; }
        let i = p2;
        while i <= n {
            comp[i - 2] = true;
            i += p;
        }
        loop {
            p++;
            if !comp[p - 2] { break; }
        }
    }
    for i in 0..(n - 1) {
        if !comp[i] { primes << (i + 2); }
    }
    return primes;
}

fn main() {
    println "Primes less than 100:";
    let primes = sieve_of_eratosthenes(100);
    for p in primes { print "{p} "; }
    println "";
}
```

**Output:**

```
Primes less than 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sieve of Eratosthenes**](https://rosettacode.org/wiki/Sieve_of_Eratosthenes) in Zen C.

*This article uses material from the Rosetta Code article **Sieve of Eratosthenes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sieve_of_Eratosthenes?action=history).*
