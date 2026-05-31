+++
title = "Nice primes"
+++

# Nice primes

{{trans|Wren}}

```zc
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

fn digit_sum(n: int) -> int {
    let sum = 0;
    while n > 0 {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

fn main() {
    println "Nice primes in the open interval (500, 1000) are:";
    let c = 0;
    for i in 501..1000 step 2 {
        if is_prime(i) {
            let s = i;
            while s >= 10  { s = digit_sum(s); }
            if is_prime(s) { println "{++c:2d}: {i} -> Σ = {s}"; }
        }
    }
}
```

**Output:**

```
Nice primes in the open interval (500, 1000) are:
 1: 509 -> Σ = 5
 2: 547 -> Σ = 7
 3: 563 -> Σ = 5
 4: 569 -> Σ = 2
 5: 587 -> Σ = 2
 6: 599 -> Σ = 5
 7: 601 -> Σ = 7
 8: 617 -> Σ = 5
 9: 619 -> Σ = 7
10: 641 -> Σ = 2
11: 653 -> Σ = 5
12: 659 -> Σ = 2
13: 673 -> Σ = 7
14: 677 -> Σ = 2
15: 691 -> Σ = 7
16: 709 -> Σ = 7
17: 727 -> Σ = 7
18: 743 -> Σ = 5
19: 761 -> Σ = 5
20: 797 -> Σ = 5
21: 821 -> Σ = 2
22: 839 -> Σ = 2
23: 853 -> Σ = 7
24: 857 -> Σ = 2
25: 887 -> Σ = 5
26: 907 -> Σ = 7
27: 911 -> Σ = 2
28: 929 -> Σ = 2
29: 941 -> Σ = 5
30: 947 -> Σ = 2
31: 977 -> Σ = 5
32: 983 -> Σ = 2
33: 997 -> Σ = 7
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Nice primes**](https://rosettacode.org/wiki/Nice_primes) in Zen C.

*This article uses material from the Rosetta Code article **Nice primes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Nice_primes?action=history).*
