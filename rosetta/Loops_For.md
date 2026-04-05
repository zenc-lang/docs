+++
title = "Loops/For"
+++

# Loops/For

Zen C provides a clean <code>for-in</code> syntax with built-in range operators. However, it also fully supports the traditional C-style 3-part <code>for</code> loop. In keeping with Zen C's modern ergonomics, the enclosing parentheses around the loop conditions are optional, but they can still be used if preferred.

```zc
fn main() {
    println "Using a Zen C range loop:";
    // Inclusive range loop
    for i in 1..=5 {
        println "Iteration: {i}";
    }

    println "\nUsing a C-style for loop (without parentheses):";
    // Traditional 3-part loop, parenthesis-free
    for let j = 1; j <= 5; j += 1 {
        println "Iteration: {j}";
    }

    println "\nUsing a C-style for loop (with parentheses):";
    // Traditional 3-part loop, exactly like C
    for (let k = 1; k <= 5; k += 1) {
        println "Iteration: {k}";
    }
}
```

**Output:**

```
Using a Zen C range loop:
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
Iteration: 5

Using a C-style for loop (without parentheses):
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
Iteration: 5

Using a C-style for loop (with parentheses):
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
Iteration: 5
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/For**](https://rosettacode.org/wiki/Loops/For) in Zen C.

*This article uses material from the Rosetta Code article **Loops/For**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/For?action=history).*
