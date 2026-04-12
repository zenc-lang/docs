+++
title = "Emirp primes"
+++

# Emirp primes

```zc
import "locale.h"

fn is_prime(n: int) -> bool {
    if n < 2 { return false; }
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

fn reverse_digits(n: int) -> int {
    let r = 0;
    while n > 0 {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}

fn is_emirp(n: int) -> bool {
    if is_prime(n) {
        let r = reverse_digits(n);
        if r != n && is_prime(r) { return true; }
    }
    return false;
}

fn main() {
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println "The first 20 emirps are:";
    let count = 0;
    let i = 3;
    while count < 20 {
        if is_emirp(i) { 
            print "{i:3d} ";
            if !(++count % 10) { println ""; }
        }
        i += 2;
    }

    println "\nThe emirps between 7,700 and 8,000 are:";
    count = 0;
    i = 7701;
    while i < 8000 {
        if is_emirp(i) {
            print "{i:'4d} ";
            if !(++count % 7) { println ""; }
        }
        i += 2;
    }

    print "\n\nThe 10,000th emirp is ";
    count = 0;
    i = 1;
    while count < 10000 {
        i += 2;
        if is_emirp(i) { count++; }
    }
    println "{i:'d}.";
}
```

**Output:**

```
The first 20 emirps are:
 13  17  31  37  71  73  79  97 107 113 
149 157 167 179 199 311 337 347 359 389 

The emirps between 7,700 and 8,000 are:
7,717 7,757 7,817 7,841 7,867 7,879 7,901 
7,927 7,949 7,951 7,963 

The 10,000th emirp is 948,349.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Emirp primes**](https://rosettacode.org/wiki/Emirp_primes) in Zen C.

*This article uses material from the Rosetta Code article **Emirp primes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Emirp_primes?action=history).*
