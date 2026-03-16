+++
title = "Array concatenation"
+++

# Array concatenation

Zen C is a systems language that provides both low-level memory control and high-level standard library abstractions. Here are two idiomatic ways to concatenate collections.

### Using Raw Arrays

For fixed-size C-style arrays, concatenation is typically done by allocating a new array and using fast memory block copying via <code>memcpy</code>.

```zc
fn main() {
    let a: int[3] = [1, 2, 3];
    let b: int[2] = [4, 5];
    
    let c: int[5]; 
    
    // Performant memory block copying for raw arrays
    memcpy(c, a, sizeof(int) * 3);
    // Offset by 3 integers to append 'b'
    memcpy((int*)c + 3, b, sizeof(int) * 2);
    
    print "Concatenated array: [";
    for let i = 0; i < 5; i += 1 {
        print "{c[i]}";
        if i < 4 {
            print ", ";
        }
    }
    println "]";
}
```

**Output:**

```
Concatenated array: [1, 2, 3, 4, 5]
```

### Using the Standard Library

For a more modern, ergonomic approach, Zen C's standard library provides a generic <code>Vec<T></code> type. Vectors support operator overloading, allowing them to be concatenated directly using the <code>+</code> operator.

```zc
import "std/vec.zc"

fn main() {
    let a = Vec<int>::new();
    a.push(1);
    a.push(2);
    a.push(3);
    
    let b = Vec<int>::new();
    b.push(4);
    b.push(5);
    
    let c = a + b;
    
    print "Concatenated array: [";
    let count = c.length();
    let i = 0;
    for val in c {
        print "{val}";
        if i < count - 1 {
            print ", ";
        }
        i += 1;
    }
    println "]";
}
```

**Output:**

```
Concatenated array: [1, 2, 3, 4, 5]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Array concatenation**](https://rosettacode.org/wiki/Array_concatenation) in Zen C.

*This article uses material from the Rosetta Code article **Array concatenation**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Array_concatenation?action=history).*
