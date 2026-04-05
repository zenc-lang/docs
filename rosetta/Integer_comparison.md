+++
title = "Integer comparison"
+++

# Integer comparison

```zc
fn main() {
    let a: int;
    let b: int;
    
    ? "Enter two integers separated by a space: " (a, b);
    
    if a < b {
        println "{a} is less than {b}";
    }
    
    if a == b {
        println "{a} is equal to {b}";
    }
    
    if a > b {
        println "{a} is greater than {b}";
    }
}
```

**Output:**

```
Enter two integers separated by a space: 42 17
42 is greater than 17
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Integer comparison**](https://rosettacode.org/wiki/Integer_comparison) in Zen C.

*This article uses material from the Rosetta Code article **Integer comparison**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Integer_comparison?action=history).*
