+++
title = "Real constants and functions"
+++

# Real constants and functions

```zc
import "std/math.zc"

fn main() {
    println "e           = {Math::E()}";
    println "pi          = {Math::PI()}";
    println "sqrt(2)     = {Math::sqrt(2)}";
    println "log(3)      = {Math::log(3)}";
    println "exp(2)      = {Math::exp(2)}";
    println "abs(-1.2)   = {Math::abs(-1.2)}";
    println "floor(3.4)  = {Math::floor(3.4)}";
    println "ceil(5.6)   = {Math::ceil(5.6)}";
    println "pow(1.2, 3) = {Math::pow(1.2, 3.0)}";
}
```

**Output:**

```
e           = 2.718282
pi          = 3.141593
sqrt(2)     = 1.414214
log(3)      = 1.098612
exp(2)      = 7.389056
abs(-1.2)   = 1.200000
floor(3.4)  = 3.000000
ceil(5.6)   = 6.000000
pow(1.2, 3) = 1.728000
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Real constants and functions**](https://rosettacode.org/wiki/Real_constants_and_functions) in Zen C.

*This article uses material from the Rosetta Code article **Real constants and functions**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Real_constants_and_functions?action=history).*
