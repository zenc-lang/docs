+++
title = "Arrays"
+++

# Arrays

Zen C supports fixed-size arrays with value semantics. Arrays can be initialized explicitly with a list of values, or they can be zero-initialized automatically by the compiler. Iteration is handled natively using the <code>for-in</code> loop.

```zc
fn main() {
    def SIZE = 3;

    // Explicitly initialized array
    let ints: int[5] = [1, 2, 3, 4, 5];
    
    // Zero-initialized array using a compile-time constant for size
    let zeros: [int; SIZE];
    
    // Element access and mutation
    zeros[0] = 42;
    zeros[2] = 100;
    
    println "Iterating over ints array:";
    for val in ints {
        println "{val}";
    }
    
    println "\nIterating over zeros array:";
    for val in zeros {
        println "{val}";
    }
}
```

**Output:**

```
Iterating over ints array:
1
2
3
4
5

Iterating over zeros array:
42
0
100
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Arrays**](https://rosettacode.org/wiki/Arrays) in Zen C.

*This article uses material from the Rosetta Code article **Arrays**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Arrays?action=history).*
