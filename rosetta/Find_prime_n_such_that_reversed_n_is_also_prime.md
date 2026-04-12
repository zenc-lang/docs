+++
title = "Find prime n such that reversed n is also prime"
+++

# Find prime n such that reversed n is also prime

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

fn reverse_digits(n: int) -> int {
    let r = 0;
    while n > 0 {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}

fn main() {
    println "Primes under 500 which are also primes when the digits are reversed:";
    print "  2 ";
    let count = 1;
    let i = 3;
    while i < 500 {
        if is_prime(i) && is_prime(reverse_digits(i)) {
            print "{i:3d} ";
            if !(++count % 15) { println ""; }
        }
        i += 2;
    }
    println "\n\n{count} such primes found.";
}
```

**Output:**

```
Primes under 500 which are also primes when the digits are reversed:
  2   3   5   7  11  13  17  31  37  71  73  79  97 101 107 
113 131 149 151 157 167 179 181 191 199 311 313 337 347 353 
359 373 383 389 

34 such primes found.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Find prime n such that reversed n is also prime**](https://rosettacode.org/wiki/Find_prime_n_such_that_reversed_n_is_also_prime) in Zen C.

*This article uses material from the Rosetta Code article **Find prime n such that reversed n is also prime**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Find_prime_n_such_that_reversed_n_is_also_prime?action=history).*
