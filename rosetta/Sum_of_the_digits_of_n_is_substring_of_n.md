+++
title = "Sum of the digits of n is substring of n"
+++

# Sum of the digits of n is substring of n

```zc
fn digit_sum(n: int) -> int {
    let sum: int = 0;
    while n > 0 {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

fn main() {
    println "Numbers under 1,000 whose sum of digits is a substring of themselves:"
    let count = 0;
    for n in 0..<1000 {
        let ns = "{n}";
        let ds = "{digit_sum(n)}";
        if strstr(ns, ds) {
            print "{n:3d} ";
            if ++count % 8 == 0 { println ""; }
        }
    }
    println "\n{count} such numbers found."
}
```

**Output:**

```
Numbers under 1,000 whose sum of digits is a substring of themselves:
  0   1   2   3   4   5   6   7 
  8   9  10  20  30  40  50  60 
 70  80  90 100 109 119 129 139 
149 159 169 179 189 199 200 300 
400 500 600 700 800 900 910 911 
912 913 914 915 916 917 918 919 

48 such numbers found.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sum of the digits of n is substring of n**](https://rosettacode.org/wiki/Sum_of_the_digits_of_n_is_substring_of_n) in Zen C.

*This article uses material from the Rosetta Code article **Sum of the digits of n is substring of n**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sum_of_the_digits_of_n_is_substring_of_n?action=history).*
