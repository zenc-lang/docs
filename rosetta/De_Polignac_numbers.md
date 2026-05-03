+++
title = "De Polignac numbers"
+++

# De Polignac numbers

{{trans|Wren}}

```zc
import "std/vec.zc"
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

fn main() {
    let pows2: [int; 20];
    for i in 0..20 { pows2[i] = (1 << i); }
    let dp = Vec<int>::new();
    dp << 1;
    let dp1000: int;
    let dp10000: int;
    let count = 1;
    for let n = 3; count < 10000; n += 2 {
        let found = false;
        for p in pows2 {
            if p > n { break; }
            if is_prime(n - p) {
                found = true;
                break;
            }
        }
        if !found {
            if ++count <= 50 {
                dp << n;
            } else if count == 1000 {
                dp1000 = n;
            } else if count == 10000 {
                dp10000 = n;
            }
        }
    }
    setlocale(LC_NUMERIC, "");
    println "First 50 De Polignac numbers:";
    for i in 0..dp.length() {
        print "{dp[i]:'5d} ";
        if !((i + 1) % 10) { println ""; }
    }
    println "\nOne thousandth: {dp1000:'d}";
    println "\nTen thousandth: {dp10000:'d}";
}
```

**Output:**

```
First 50 De Polignac numbers:
    1   127   149   251   331   337   373   509   599   701 
  757   809   877   905   907   959   977   997 1,019 1,087 
1,199 1,207 1,211 1,243 1,259 1,271 1,477 1,529 1,541 1,549 
1,589 1,597 1,619 1,649 1,657 1,719 1,759 1,777 1,783 1,807 
1,829 1,859 1,867 1,927 1,969 1,973 1,985 2,171 2,203 2,213 

One thousandth: 31,941

Ten thousandth: 273,421
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**De Polignac numbers**](https://rosettacode.org/wiki/De_Polignac_numbers) in Zen C.

*This article uses material from the Rosetta Code article **De Polignac numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/De_Polignac_numbers?action=history).*
