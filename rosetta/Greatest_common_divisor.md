+++
title = "Greatest common divisor"
+++

# Greatest common divisor

```zc
fn gcd(x: int, y: int) -> int {
    while y {
        let t = y;
        y = x % y;
        x = t;
    }
    return abs(x);
}

fn main() {
    println "gcd(33, 77) = {gcd(33, 77)}";
    println "gcd(49865, 69811) = {gcd(49865, 69811)}";
}
```

**Output:**

```
gcd(33, 77) = 11
gcd(49865, 69811) = 9973
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Greatest common divisor**](https://rosettacode.org/wiki/Greatest_common_divisor) in Zen C.

*This article uses material from the Rosetta Code article **Greatest common divisor**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Greatest_common_divisor?action=history).*
