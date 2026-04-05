+++
title = "Averages/Simple moving average"
+++

# Averages/Simple moving average

{{trans|Wren}}

```zc
import "std/vec.zc"

alias clos = fn(f64) -> f64;

fn sma(period: usize) -> clos {
    let storage = Vec<f64>::new();
    let i = 0;
    let sum = 0.0;
    return fn[=](input: f64) -> f64 {
        if storage.length() < period {
            sum += input;
            storage << input;
        }
        sum += input - storage[i];
        storage[i] = input;
        i = (i + 1) % period;
        return sum / storage.length();
    }
}

fn main() {
    let sma3 = sma(3);
    let sma5 = sma(5);
    println "  x     sma3   sma5";
    let a: f64[10] = [1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 4.0, 3.0, 2.0, 1.0];
    for i in 0..10 {
        let x = a[i];
        printf("%5.2f  %5.2f  %5.2f\n", x, sma3(x), sma5(x));
    }
}
```

**Output:**

```
x     sma3   sma5
 1.00   1.00   1.00
 2.00   1.50   1.50
 3.00   2.00   2.00
 4.00   3.00   2.50
 5.00   4.00   3.00
 5.00   4.67   3.80
 4.00   4.67   4.20
 3.00   4.00   4.20
 2.00   3.00   3.80
 1.00   2.00   3.00
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Averages/Simple moving average**](https://rosettacode.org/wiki/Averages/Simple_moving_average) in Zen C.

*This article uses material from the Rosetta Code article **Averages/Simple moving average**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Averages/Simple_moving_average?action=history).*
