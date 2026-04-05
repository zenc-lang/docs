+++
title = "Time a function"
+++

# Time a function

```zc
import "std/time.zc" // uses system time

fn func() {
    for i in 0..10_000_000 {}
}

fn main() {
    let iterations = 100;
    let start = Time::now();
    for i in 0..iterations { func(); }
    let end = Time::now();
    println "Calling 'func' {iterations} times took {end - start} ms.";
}
```

**Output:**

Sample output:

```
Calling 'func' 100 times took 1175 ms.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Time a function**](https://rosettacode.org/wiki/Time_a_function) in Zen C.

*This article uses material from the Rosetta Code article **Time a function**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Time_a_function?action=history).*
