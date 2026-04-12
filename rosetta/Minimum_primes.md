+++
title = "Minimum primes"
+++

# Minimum primes

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

fn get_min_prime(a: int*, len: const usize) -> int {
    let max = a[0];
    for (let i: usize = 1; i < len; ++i) {
        if a[i] > max { max = a[i]; }
    }
    let i = max;
    loop {
        if is_prime(i) { break; }
        i++;
    }
    return i;
}

fn main() {
    let min_primes: [int; 5];
    let numbers1 = [ 5, 45, 23, 21, 67];
    let numbers2 = [43, 22, 78, 46, 38];
    let numbers3 = [ 9, 98, 12, 54, 53];
    for i in 0..5 {
        let numbers = [numbers1[i], numbers2[i], numbers3[i]];
        min_primes[i] = get_min_prime(numbers, 3);
    }
    print "[";
    for i in 0..5 { print "{min_primes[i]}, "; }
    println "\b\b]";
}
```

**Output:**

```
[43, 101, 79, 59, 67]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Minimum primes**](https://rosettacode.org/wiki/Minimum_primes) in Zen C.

*This article uses material from the Rosetta Code article **Minimum primes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Minimum_primes?action=history).*
