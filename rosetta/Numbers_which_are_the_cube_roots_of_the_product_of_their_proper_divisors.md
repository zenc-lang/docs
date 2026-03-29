+++
title = "Numbers which are the cube roots of the product of their proper divisors"
+++

# Numbers which are the cube roots of the product of their proper divisors

{{trans|Wren}}
A translation of the second version.

```zc
import "locale.h"

fn divisor_count(n: int) -> int {
    let i = 1;
    let k = (n % 2 == 0) ? 1 : 2;
    let count = 0;
    while i * i <= n {
        if n % i == 0 {
            count++;
            let j = n / i;
            if j != i { count++; }
        }
        i += k;
    }
    return count;
}

fn main() {
    let count = 0;
    let n = 1;
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println "First 50 numbers which are the cube roots of the products of their proper divisors:";
    loop {
        let dc = divisor_count(n);
        if n == 1 || dc  == 8 {
            if ++count <= 50 {
                print "{n:3d} ";
                if !(count % 10) { println ""; }
            } else if count == 500 {
                println "\n500th    : {n:'7d}";
            } else if count == 5_000 {
                println "\n5,000th  : {n:'7d}";
            } else if count == 50_000 {
                println "\n50,000th : {n:'7d}";
                break;
            }
        }
        n++;
    }
}
```

**Output:**

```
First 50 numbers which are the cube roots of the products of their proper divisors:
  1  24  30  40  42  54  56  66  70  78 
 88 102 104 105 110 114 128 130 135 136 
138 152 154 165 170 174 182 184 186 189 
190 195 222 230 231 232 238 246 248 250 
255 258 266 273 282 285 286 290 296 297 

500th    :   2,526

5,000th  :  23,118

50,000th : 223,735
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Numbers which are the cube roots of the product of their proper divisors**](https://rosettacode.org/wiki/Numbers_which_are_the_cube_roots_of_the_product_of_their_proper_divisors) in Zen C.

*This article uses material from the Rosetta Code article **Numbers which are the cube roots of the product of their proper divisors**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Numbers_which_are_the_cube_roots_of_the_product_of_their_proper_divisors?action=history).*
