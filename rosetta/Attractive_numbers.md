+++
title = "Attractive numbers"
+++

# Attractive numbers

```zc
import "std/vec.zc"

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

fn count_factors(n: int) -> int {
    if n < 2 { return 0; }
    let factors = Vec<int>::new();
    let inc: int[8] = [4, 2, 4, 2, 4, 6, 2, 6];
    while n % 2 == 0 {
        factors << 2;
        n /= 2;
    }
    while n % 3 == 0 {
        factors << 3;
        n /= 3;
    }
    while n % 5 == 0 {
        factors << 5;
        n /= 5;
    }
    let k = 7;
    let i: usize = 0;
    while k * k <= n {
        if n % k == 0 {
            factors << k;
            n /= k;
        } else {
            k += inc[i];
            i = (i + 1) % 8;
        }
    }
    if n > 1 { factors << n; }
    return factors.length();
}

fn is_attractive(n: int) -> bool {
    let c = count_factors(n);
    return is_prime(c);
}

fn main() {
    let lim: const int = 120;
    println "The attractive numbers up to and including {lim} are:";
    let count = 0;
    for i in 1..=lim {
        if is_attractive(i) {
            print "{i:4d}";
            if !(++count % 20) { println ""; }
        }
    }
    println "\n\n{count} such numbers found.";
}
```

**Output:**

```
The attractive numbers up to and including 120 are:
   4   6   8   9  10  12  14  15  18  20  21  22  25  26  27  28  30  32  33  34
  35  38  39  42  44  45  46  48  49  50  51  52  55  57  58  62  63  65  66  68
  69  70  72  74  75  76  77  78  80  82  85  86  87  91  92  93  94  95  98  99
 102 105 106 108 110 111 112 114 115 116 117 118 119 120

74 such numbers found.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Attractive numbers**](https://rosettacode.org/wiki/Attractive_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Attractive numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Attractive_numbers?action=history).*
