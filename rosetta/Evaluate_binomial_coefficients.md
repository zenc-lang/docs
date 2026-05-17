+++
title = "Evaluate binomial coefficients"
+++

# Evaluate binomial coefficients

{{trans|Wren}}

```zc
fn factorial(n: uint) -> u64 {
    let prod: u64 = 1;
    for i in 2..=n { prod *= i; }
    return prod;
}

fn binomial(n: uint, k: uint) -> u64 {
    assert(n >= k, "The second argument cannot be more than the first");
    if n == k { return 1; }
    let prod: u64 = 1;
    let i = n - k + 1;
    while i <= n { prod *= i++; }
    return prod / factorial(k);
}

fn main() {
    def LIMIT = 14;
    print "n/k |";
    for k in 0..=LIMIT { print "{k:5d}"; }
    println "";
    print "----+";
    for i in 0..=LIMIT{ print "-----"; }
    println "";
    for n in 0..=LIMIT {
        print "{n:3d} |";
        for k in 0..=n { print "{binomial(n, k):5lu}"; }
        println "";
    }
}
```

**Output:**

```
n/k |    0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
----+---------------------------------------------------------------------------
  0 |    1
  1 |    1    1
  2 |    1    2    1
  3 |    1    3    3    1
  4 |    1    4    6    4    1
  5 |    1    5   10   10    5    1
  6 |    1    6   15   20   15    6    1
  7 |    1    7   21   35   35   21    7    1
  8 |    1    8   28   56   70   56   28    8    1
  9 |    1    9   36   84  126  126   84   36    9    1
 10 |    1   10   45  120  210  252  210  120   45   10    1
 11 |    1   11   55  165  330  462  462  330  165   55   11    1
 12 |    1   12   66  220  495  792  924  792  495  220   66   12    1
 13 |    1   13   78  286  715 1287 1716 1716 1287  715  286   78   13    1
 14 |    1   14   91  364 1001 2002 3003 3432 3003 2002 1001  364   91   14    1
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Evaluate binomial coefficients**](https://rosettacode.org/wiki/Evaluate_binomial_coefficients) in Zen C.

*This article uses material from the Rosetta Code article **Evaluate binomial coefficients**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Evaluate_binomial_coefficients?action=history).*
