+++
title = "A+B"
+++

# A+B

Zen C features a built-in shorthand for reading user input using the <code>?</code> operator. Format specifiers are automatically inferred based on the types of the variables. When evaluated, it returns the number of successfully read items.

```zc
fn main() {
    let a: int;
    let b: int;
    
    // Read two space-separated integers directly from the input stream
    if (? a, b) == 2 {
        let sum = a + b;
        println "{sum}";
    }
}
```

**Output:**

```
2 2
4
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**A+B**](https://rosettacode.org/wiki/A+B) in Zen C.

*This article uses material from the Rosetta Code article **A+B**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/A+B?action=history).*
