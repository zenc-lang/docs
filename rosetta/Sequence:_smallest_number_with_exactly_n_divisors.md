+++
title = "Sequence: smallest number with exactly n divisors"
+++

# Sequence: smallest number with exactly n divisors

{{trans|Wren}}

```zc
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
    def LIMIT = 22;
    let numbers: [int; LIMIT];
    for let i = 1; ; ++i {
        let nd = divisor_count(i);
        if nd <= LIMIT && !numbers[nd - 1] {
            numbers[nd - 1] = i;
            let all = true;
            for n in numbers {
                if n <= 0 {
                    all = false;
                    break;
                }
            }
            if all { break; }
        } 
    }
    println "The first {LIMIT} terms are:";
    print "[";
    for i in 0..LIMIT { print "{numbers[i]}, "; }
    println "\b\b]";
}
```

**Output:**

```
The first 22 terms are:
[1, 2, 4, 6, 16, 12, 64, 24, 36, 48, 1024, 60, 4096, 192, 144, 120, 65536, 180, 262144, 240, 576, 3072]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sequence: smallest number with exactly n divisors**](https://rosettacode.org/wiki/Sequence:_smallest_number_with_exactly_n_divisors) in Zen C.

*This article uses material from the Rosetta Code article **Sequence: smallest number with exactly n divisors**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sequence:_smallest_number_with_exactly_n_divisors?action=history).*
