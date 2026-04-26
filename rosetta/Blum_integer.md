+++
title = "Blum integer"
+++

# Blum integer

{{trans|Wren}}

```zc
import "locale.h"

let inc = [4, 2, 4, 2, 4, 6, 2, 6];

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

// Assumes n is odd.
fn first_prime_factor(n: int) -> int {
    if n == 1 { return 1; }
    if n % 3 == 0 { return 3; }
    if n % 5 == 0 { return 5; }
    let k = 7;
    let i = 0;
    while k * k <= n {
        if n % k == 0 {
            return k;
        } else {
            k += inc[i];
            i = (i + 1) % 8;
        }
    }
    return n;
}

fn main() {
    setlocale(LC_NUMERIC, "");
    let blum: [int; 50];
    let bc = 0;
    let counts: [int; 10];
    let digits = [1, 3, 7, 9];
    let i = 1;
    loop {
        let p = first_prime_factor(i);
        if p % 4 == 3 {
            let q = i / p;
            if q != p && q % 4 == 3 && is_prime(q) {
                if bc < 50 { blum[bc] = i; }
                counts[i % 10]++;
                bc++;
                if bc == 50 {
                    println "First 50 Blum integers:";
                    for j in 0..50 {
                        print "{blum[j]:3d} ";
                        if !((j + 1) % 10) { println ""; }
                    }
                    println "";
                } else if bc == 26_828 || bc % 100_000 == 0 {
                    println "The {bc:'7d}th Blum integer is: {i:'9d}";
                    if bc == 400_000 {
                        println "\n% distribution of the first 400,000 Blum integers:";
                        for j in digits {
                            println "  {counts[j] / 4000.0:6.3f}% end in {j}";
                        }
                        break;
                    }
                }
            }
        }
        i = (i % 5 == 3) ? i + 4 : i + 2;
    }
}
```

**Output:**

```
First 50 Blum integers:
 21  33  57  69  77  93 129 133 141 161 
177 201 209 213 217 237 249 253 301 309 
321 329 341 381 393 413 417 437 453 469 
473 489 497 501 517 537 553 573 581 589 
597 633 649 669 681 713 717 721 737 749 

The  26,828th Blum integer is:   524,273
The 100,000th Blum integer is: 2,075,217
The 200,000th Blum integer is: 4,275,533
The 300,000th Blum integer is: 6,521,629
The 400,000th Blum integer is: 8,802,377

% distribution of the first 400,000 Blum integers:
  25.001% end in 1
  25.017% end in 3
  24.997% end in 7
  24.985% end in 9
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Blum integer**](https://rosettacode.org/wiki/Blum_integer) in Zen C.

*This article uses material from the Rosetta Code article **Blum integer**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Blum_integer?action=history).*
