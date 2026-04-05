+++
title = "Return multiple values"
+++

# Return multiple values

Zen C supports returning multiple values from a function natively using Tuples. These tuples can then be destructured directly into distinct variables at the call site.

```zc
// Function returning a tuple of two integers
fn add_and_subtract(a: int, b: int) -> (int, int) {
    return (a + b, a - b);
}

fn main() {
    // Destructuring the returned tuple directly into 'sum' and 'diff'
    let (sum, diff) = add_and_subtract(10, 4);
    
    println "Sum: {sum}";
    println "Difference: {diff}";
}
```

**Output:**

```
Sum: 14
Difference: 6
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Return multiple values**](https://rosettacode.org/wiki/Return_multiple_values) in Zen C.

*This article uses material from the Rosetta Code article **Return multiple values**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Return_multiple_values?action=history).*
