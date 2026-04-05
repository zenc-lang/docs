+++
title = "Least common multiple"
+++

# Least common multiple

```zc
fn gcd(x: int, y: int) -> int {
    while y {
        let t = y;
        y = x % y;
        x = t;
    }
    return abs(x);
}

fn lcm(x: int, y: int) -> int {
    if !x && !y { return 0; }
    return abs(x * y) / gcd(x, y);
}

fn main() {
    println "lcm(12, 18) = {lcm(12, 18)}";
    println "lcm(-6, 14) = {lcm(-6, 14)}";
    println "lcm(35,  0) = {lcm(35,  0)}";
}
```

**Output:**

```
lcm(12, 18) = 36
lcm(-6, 14) = 42
lcm(35,  0) = 0
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Least common multiple**](https://rosettacode.org/wiki/Least_common_multiple) in Zen C.

*This article uses material from the Rosetta Code article **Least common multiple**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Least_common_multiple?action=history).*
