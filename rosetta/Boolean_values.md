+++
title = "Boolean values"
+++

# Boolean values

Zen C inherits C's flexible semantics for boolean evaluation, meaning any value equal to <code>0</code> is considered false, and any non-zero value is considered true. This applies to integers, floating-point numbers, characters (where <code>'\0'</code> is false), and pointers (where a null pointer is false). 

However, unlike older C standards that require including <code>&lt;stdbool.h&gt;</code>, Zen C modernizes this by providing a native <code>bool</code> data type and built-in <code>true</code> and <code>false</code> keywords directly in the language.

```zc
fn main() {
    // Native boolean type and keywords
    let is_valid: bool = true;
    let is_empty: bool = false;
    
    println "Native true evaluates to: {is_valid}";
    println "Native false evaluates to: {is_empty}\n";

    // C-style truthiness evaluation
    let zero_int = 0;
    let non_zero_int = 42;
    let zero_float = 0.0;
    
    if zero_int {
        println "0 is true";
    } else {
        println "0 evaluates to false";
    }
    
    if non_zero_int {
        println "42 evaluates to true";
    }
    
    if zero_float {
        println "0.0 is true";
    } else {
        println "0.0 evaluates to false";
    }
}
```

**Output:**

```
Native true evaluates to: 1
Native false evaluates to: 0

0 evaluates to false
42 evaluates to true
0.0 evaluates to false
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Boolean values**](https://rosettacode.org/wiki/Boolean_values) in Zen C.

*This article uses material from the Rosetta Code article **Boolean values**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Boolean_values?action=history).*
