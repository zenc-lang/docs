+++
title = "Munchausen numbers"
+++

# Munchausen numbers

{{trans|Wren}}

```zc
let powers: [uint; 10];

fn init() {
    for i in 1..10 { powers[i] = i ** i; }
}

fn munchausen(n: uint) -> bool {
    let nn = n;
    let sum: uint = 0;
    while n > 0 {
        let digit = n % 10;
        sum  += powers[digit];
        n /= 10;
    }
    return nn == sum;
}

fn main() {
    init();
    println "The Munchausen numbers <= 5000 are:";
    for let i: uint = 1; i <= 5000; ++i {
       if munchausen(i) { println "{i}"; }
    }
}
```

**Output:**

```
The Munchausen numbers <= 5000 are:
1
3435
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Munchausen numbers**](https://rosettacode.org/wiki/Munchausen_numbers) in Zen C.

*This article uses material from the Rosetta Code article **Munchausen numbers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Munchausen_numbers?action=history).*
