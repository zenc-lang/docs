+++
title = "Factors of an integer"
+++

# Factors of an integer

```zc
import "std/vec.zc"

fn divisors(n: int) -> Vec<int> {
    let divs = Vec<int>::new();
    if n < 1 { return divs; }
    let divs2 = Vec<int>::new();
    let i = 1;
    let k = (n % 2 == 0) ? 1 : 2;
    while i * i <= n {
        if n % i == 0 {
            divs << i;
            let j = n / i;
            if j != i { divs2 << j; }
        }
        i += k;
    }
    if divs2.length() {
        divs2.reverse();
        for l in 0..divs2.length() { divs << divs2[l]; }
    }
    return divs;
}

fn main() {
    let a = [11, 21, 32, 45, 67, 96, 159, 723, 1024, 5673, 12345, 32767, 123459, 999997];
    println "The factors of the following numbers are:";
    for e in a {
        print "{e:6d} => [";
        let divs = divisors(e);
        for i in 0..divs.length() { print "{divs[i]}, "; }
        println "\b\b]";
    }
}
```

**Output:**

```
The factors of the following numbers are:
    11 => [1, 11] 
    21 => [1, 3, 7, 21] 
    32 => [1, 2, 4, 8, 16, 32] 
    45 => [1, 3, 5, 9, 15, 45] 
    67 => [1, 67] 
    96 => [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96] 
   159 => [1, 3, 53, 159] 
   723 => [1, 3, 241, 723] 
  1024 => [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] 
  5673 => [1, 3, 31, 61, 93, 183, 1891, 5673] 
 12345 => [1, 3, 5, 15, 823, 2469, 4115, 12345] 
 32767 => [1, 7, 31, 151, 217, 1057, 4681, 32767] 
123459 => [1, 3, 7, 21, 5879, 17637, 41153, 123459] 
999997 => [1, 757, 1321, 999997]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Factors of an integer**](https://rosettacode.org/wiki/Factors_of_an_integer) in Zen C.

*This article uses material from the Rosetta Code article **Factors of an integer**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Factors_of_an_integer?action=history).*
