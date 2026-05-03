+++
title = "Chowla numbers"
+++

# Chowla numbers

{{trans|Go}}

```zc
import "locale.h"

fn chowla(n: int) -> int {
    assert(n > 0, "argument must be a positive integer.");
    let sum = 0;
    for let i = 2; i * i <= n; ++i {
        if !(n % i) {
            let j = n / i;
            sum += (i == j) ? i : i + j;
        }
    }
    return sum;
}

fn sieve(c: bool*, limit: const int) {
    // True denotes composite, false denotes prime.
    // Only interested in odd numbers >= 3.
    for let i = 3; i * 3 < limit; i += 2 {
        if !c[i] && !chowla(i) {
            for let j = 3 * i; j < limit; j += 2 * i {
                c[j] = true;
            }
        }
    }
}

fn main() {
    setlocale(LC_NUMERIC, "");
    for let i = 1; i <= 37; ++i {
        println "chowla({i:2d}) = {chowla(i)}";
    }
    println "";
    let count = 1;
    let limit = 10_000_000;
    autofree let c = (bool*)calloc(limit, sizeof(bool));
    sieve(c, limit);
    let power = 100;
    for let i = 3; i < limit; i += 2 {
        if !c[i] { count++; }
        if i == power - 1 {
            println "Count of primes up to {power:'-10d} = {count:'d}";
            power *= 10;
        }
    }
    println "";
    count = 0;
    limit = 35_000_000;
    for let i = 2; ; ++i {
        let p = (1 << (i - 1)) * ((1 << i) - 1) // perfect numbers must be of this form
        if p > limit { break; }
        if chowla(p) == p - 1 {
            println "{p:'d} is a perfect number.";
            count++;
        }
    }
    println "\nThere are {count} perfect numbers <= 35,000,000.";
}
```

**Output:**

```
chowla( 1) = 0
chowla( 2) = 0
chowla( 3) = 0
chowla( 4) = 2
chowla( 5) = 0
chowla( 6) = 5
chowla( 7) = 0
chowla( 8) = 6
chowla( 9) = 3
chowla(10) = 7
chowla(11) = 0
chowla(12) = 15
chowla(13) = 0
chowla(14) = 9
chowla(15) = 8
chowla(16) = 14
chowla(17) = 0
chowla(18) = 20
chowla(19) = 0
chowla(20) = 21
chowla(21) = 10
chowla(22) = 13
chowla(23) = 0
chowla(24) = 35
chowla(25) = 5
chowla(26) = 15
chowla(27) = 12
chowla(28) = 27
chowla(29) = 0
chowla(30) = 41
chowla(31) = 0
chowla(32) = 30
chowla(33) = 14
chowla(34) = 19
chowla(35) = 12
chowla(36) = 54
chowla(37) = 0

Count of primes up to 100        = 25
Count of primes up to 1,000      = 168
Count of primes up to 10,000     = 1,229
Count of primes up to 100,000    = 9,592
Count of primes up to 1,000,000  = 78,498
Count of primes up to 10,000,000 = 664,579

6 is a perfect number.
28 is a perfect number.
496 is a perfect number.
8,128 is a perfect number.
33,550,336 is a perfect number.

There are 5 perfect numbers <= 35,000,000.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Chowla numbers**](https://rosettacode.org/wiki/Chowla_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Chowla numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Chowla_numbers?action=history).*
