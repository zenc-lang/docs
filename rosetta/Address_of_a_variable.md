+++
title = "Address of a variable"
+++

# Address of a variable

```zc
fn main() {
    let a = 10;
    let b = 20;

    // Get the address of 'a' and store it in a pointer
    let p: int* = &a;
    println "Pointer p holds the address of a: {(usize)p}";

    // Set the pointer to hold a new address
    p = &b;
    println "Pointer p now holds the address of b: {(usize)p}";
}
```

**Output:**

```
Pointer p holds the address of a: 140734141454332
Pointer p now holds the address of b: 140734141454328
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Address of a variable**](https://rosettacode.org/wiki/Address_of_a_variable) in Zen C.

*This article uses material from the Rosetta Code article **Address of a variable**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Address_of_a_variable?action=history).*
