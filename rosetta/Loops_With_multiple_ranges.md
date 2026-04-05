+++
title = "Loops/With multiple ranges"
+++

# Loops/With multiple ranges

{{trans|C}}

```zc
import "locale.h"

def ONE   = 1;
def THREE = 3;
def SEVEN = 7;

let sum  = 0;
let prod = 1;

fn abs(n: int) -> int {
    return n >= 0 ? n : -n;
}

fn process(j: int) {
    sum += abs(j);
    if abs(prod) < (1 << 27) && j { prod *= j; }
}

fn main() {
    let x: const int = 5;
    let y: const int = -5;
    let z: const int = -2;
    let p: const int = 11 ** 5;

    let j: int;
    for j = -THREE; j <= 3 ** 3; j += THREE { process(j); }
    for j = -SEVEN; j <= SEVEN; j += x      { process(j); }
    for j = 555; j <= 550 - y; ++j          { process(j); }
    for j = 22; j >= -28; j -= THREE        { process(j); }
    for j = 1927; j <= 1939; ++j            { process(j); }
    for j = x; j >= y; j -= -z              { process(j); }
    for j = p; j <= p + ONE; ++j            { process(j); }

    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println "sum  = {sum:' d}";
    println "prod = {prod:' d}";
}
```

**Output:**

```
sum  =  348,173
prod = -793,618,560
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/With multiple ranges**](https://rosettacode.org/wiki/Loops/With_multiple_ranges) in Zen C.

*This article uses material from the Rosetta Code article **Loops/With multiple ranges**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/With_multiple_ranges?action=history).*
