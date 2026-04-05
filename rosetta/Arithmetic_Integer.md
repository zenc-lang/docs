+++
title = "Arithmetic/Integer"
+++

# Arithmetic/Integer

Zen C inherits standard C arithmetic operators and semantics for basic math, but modernizes the toolset with a native exponentiation operator. 
* Integer quotient (<code>/</code>) truncates towards zero.
* Remainder (<code>%</code>) matches the sign of the first operand (the dividend). 
* Integer exponentiation (<code>**</code>) handles powers natively.

To fulfill the <code>divmod</code> bonus, this example leverages Zen C's Tuple types to return both the quotient and remainder from a single function call.

```zc
// Custom divmod using Tuples for multiple return values
fn divmod(a: int, b: int) -> (int, int) {
    return (a / b, a % b);
}

fn main() {
    let a: int;
    let b: int;
    
    // Read two integers using the input shorthand
    ? "Enter two integers separated by a space: " (a, b);
    
    let sum = a + b;
    let diff = a - b;
    let prod = a * b;
    let quot = a / b;
    let rem = a % b;
    let pow = a ** b;
    let (q, r) = divmod(a, b);
    
    println "a + b  = {sum}";
    println "a - b  = {diff}";
    println "a * b  = {prod}";
    println "a / b  = {quot}";
    println "a % b  = {rem}";
    println "a ** b = {pow}"; 
    println "divmod(a, b) = ({q}, {r})";
}
```

**Output:**

```
Enter two integers separated by a space: 2 4
a + b  = 6
a - b  = -2
a * b  = 8
a / b  = 0
a % b  = 2
a ** b = 16
divmod(a, b) = (0, 2)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Arithmetic/Integer**](https://rosettacode.org/wiki/Arithmetic/Integer) in Zen C.

*This article uses material from the Rosetta Code article **Arithmetic/Integer**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Arithmetic/Integer?action=history).*
