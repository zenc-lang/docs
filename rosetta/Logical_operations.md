+++
title = "Logical operations"
+++

# Logical operations

```zc
fn logical_ops(a: bool, b: bool) {
    println "Inputs -> a: {a}, b: {b}";
    println "  a AND b: {a && b}";
    println "  a OR b:  {a || b}";
    println "  NOT a:   {!a}";
    println "  a XOR b: {a ^ b}";
}

fn main() {
    println "(true, false)";
    logical_ops(true, false);
    
    println "\n(true, true)";
    logical_ops(true, true);
    
    println "\n(false, false)";
    logical_ops(false, false);
}
```

**Output:**

```
(true, false)
Inputs -> a: true, b: false
  a AND b: false
  a OR b:  true
  NOT a:   false
  a XOR b: true

(true, true)
Inputs -> a: true, b: true
  a AND b: true
  a OR b:  true
  NOT a:   false
  a XOR b: false

(false, false)
Inputs -> a: false, b: false
  a AND b: false
  a OR b:  false
  NOT a:   true
  a XOR b: false
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Logical operations**](https://rosettacode.org/wiki/Logical_operations) in Zen C.

*This article uses material from the Rosetta Code article **Logical operations**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Logical_operations?action=history).*
