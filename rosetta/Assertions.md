+++
title = "Assertions"
+++

# Assertions

```zc
fn main() {
    let n = 42
    assert(n == 42)
    
    let not_n = 24
    assert(not_n == 42, "Why aren't you using n?!")
}
```

**Output:**

```
Assertion failed: Why aren't you using n?!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Assertions**](https://rosettacode.org/wiki/Assertions) in Zen C.

*This article uses material from the Rosetta Code article **Assertions**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Assertions?action=history).*
