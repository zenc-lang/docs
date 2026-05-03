+++
title = "Amicable pairs"
+++

# Amicable pairs

```zc
fn proper_divisor_sum(n: int) -> int {
    let i = 1;
    let k = (n % 2 == 0) ? 1 : 2;
    let sum = 0;
    while i * i <= n {
        if n % i == 0 {
            sum += i;
            let j = n / i;
            if j != i { sum += j; }
        }
        i += k;
    }
    return sum - n;
}

fn main() {
    def LIMIT = 20_000;
    println "The amicable pairs below {LIMIT} are:";
    for m in 1..LIMIT {
        let n = proper_divisor_sum(m);
        if m < n && m == proper_divisor_sum(n) {
            println "  {m:5d} and {n:5d}";
        }
    }
}
```

**Output:**

```
The amicable pairs below 20000 are:
    220 and   284
   1184 and  1210
   2620 and  2924
   5020 and  5564
   6232 and  6368
  10744 and 10856
  12285 and 14595
  17296 and 18416
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Amicable pairs**](https://rosettacode.org/wiki/Amicable_pairs) in Zen C.

*This article uses material from the Rosetta Code article **Amicable pairs**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Amicable_pairs?action=history).*
