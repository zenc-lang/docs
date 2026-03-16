+++
title = "Array length"
+++

# Array length

Zen C provides different ways to determine the number of elements depending on whether you are using raw fixed-size arrays or standard library vectors.

### Using Raw Arrays

For raw C-style arrays, the number of elements is determined using the classic <code>sizeof</code> technique, dividing the total byte size of the array by the byte size of a single element.

```zc
fn main() {
    let fruits: string[2] = ["apple", "orange"];
    
    // Calculate the number of elements using sizeof
    let count = sizeof(fruits) / sizeof(fruits[0]);
    
    println "Raw array length: {count}";
}
```

**Output:**

```
Raw array length: 2
```

### Using the Standard Library

When using the <code>Vec<T></code> type from the standard library, determining the number of elements is as simple as calling the <code>.length()</code> method.

```zc
import "std/vec.zc"

fn main() {
    let fruits = Vec<string>::new();
    fruits.push("apple");
    fruits.push("orange");
    
    // Retrieve the length using the built-in method
    let count = fruits.length();
    
    println "Vector length: {count}";
}
```

**Output:**

```
Vector length: 2
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Array length**](https://rosettacode.org/wiki/Array_length) in Zen C.

*This article uses material from the Rosetta Code article **Array length**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Array_length?action=history).*
