+++
title = "Brazilian numbers"
+++

# Brazilian numbers

{{trans|Wren}}

```zc
import "locale.h"

fn same_digits(n: int, b: int) -> bool {
    let f = n % b;
    n /= b;
    while n > 0 {
        if n % b != f { return false; }
        n /= b;
    }
    return true;
}

fn is_brazilian(n: int) -> bool {
    if n < 7 { return false; }
    if !(n % 2) && n >= 8 { return true; }
    for b in 2..(n - 1) {
        if same_digits(n, b) { return true; }
    }
    return false;
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
    setlocale(LC_NUMERIC, "");
    let kinds = [" ", " odd ", " prime "];
    for i, kind in kinds {
        println "First 20{kind}Brazilian numbers:";
        let c = 0;
        let n = 7;
        loop {
            if is_brazilian(n) {
                print "{n} ";
                if ++c == 20 {
                    let nl = i < 2 ? "\n" : "";
                    println "{nl}";
                    break;
                }
            }
            if kind == " " {
                n++;
            } else if kind == " odd " {
                n += 2;
            } else {
                loop {
                    n += 2;
                    if is_prime(n) { break; }
                }
            }
        }
    }
    let c = 0;
    let n = 7;
    while c < 100_000 {
        if is_brazilian(n) { c++; }
        n++;
    }
    println "The 100,000th Brazilian number: {n - 1:'d}";
}
```

**Output:**

```
First 20 Brazilian numbers:
7 8 10 12 13 14 15 16 18 20 21 22 24 26 27 28 30 31 32 33 

First 20 odd Brazilian numbers:
7 13 15 21 27 31 33 35 39 43 45 51 55 57 63 65 69 73 75 77 

First 20 prime Brazilian numbers:
7 13 31 43 73 127 157 211 241 307 421 463 601 757 1093 1123 1483 1723 2551 2801 
The 100,000th Brazilian number: 110,468
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Brazilian numbers**](https://rosettacode.org/wiki/Brazilian_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Brazilian numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Brazilian_numbers?action=history).*
