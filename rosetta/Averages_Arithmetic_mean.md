+++
title = "Averages/Arithmetic mean"
+++

# Averages/Arithmetic mean

This implementation uses Zen C's standard library <code>Vec<T></code> type. To handle the edge case of an empty vector, the function checks if the vector is empty and returns <code>0.0</code> to avoid division by zero.

```zc
import "std/vec.zc"

fn mean(v: Vec<f64>*) -> f64 {
    if v.is_empty() {
        return 0.0;
    }

    let sum: f64 = 0.0;
    for x in v {
        sum += x;
    }
    
    return sum / (f64)v.length();
}

fn main() {
    let numbers = Vec<f64>::new();
    numbers.push(10.0);
    numbers.push(20.0);
    numbers.push(30.0);
    numbers.push(40.0);
    
    let m = mean(&numbers);
    println "Numbers: 10, 20, 30, 40";
    println "Mean: {m}";

    let empty = Vec<f64>::new();
    let m_empty = mean(&empty);
    println "Empty mean: {m_empty}";
}
```

**Output:**

```
Numbers: 10, 20, 30, 40
Mean: 25.000000
Empty mean: 0.000000
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Averages/Arithmetic mean**](https://rosettacode.org/wiki/Averages/Arithmetic_mean) in Zen C.

*This article uses material from the Rosetta Code article **Averages/Arithmetic mean**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Averages/Arithmetic_mean?action=history).*
