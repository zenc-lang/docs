+++
title = "Temperature conversion"
+++

# Temperature conversion

```zc
import "std/math.zc"

fn temp_conv(k: f64) {
    let c = k - 273.15;
    let f = c * 1.8 + 32.0;
    let r = f + 459.67;
    println "{k:7.2f}˚ Kelvin";
    println "{c:7.2f}˚ Celsius";
    println "{f:7.2f}˚ Fahrenheit";
    println "{r:7.2f}˚ Rankine";
    println "";
}

fn main() {
    let ks: f64[3] = [0.0, 21.0, 100.0];
    for k in ks { temp_conv(k); }
}
```

**Output:**

```
0.00˚ Kelvin
-273.15˚ Celsius
-459.67˚ Fahrenheit
   0.00˚ Rankine

  21.00˚ Kelvin
-252.15˚ Celsius
-421.87˚ Fahrenheit
  37.80˚ Rankine

 100.00˚ Kelvin
-173.15˚ Celsius
-279.67˚ Fahrenheit
 180.00˚ Rankine
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Temperature conversion**](https://rosettacode.org/wiki/Temperature_conversion) in Zen C.

*This article uses material from the Rosetta Code article **Temperature conversion**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Temperature_conversion?action=history).*
