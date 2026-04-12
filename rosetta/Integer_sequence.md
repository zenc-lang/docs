+++
title = "Integer sequence"
+++

# Integer sequence

This will carry on until it reaches 340282366920938463463374607431768211455 (= 2^128 - 1) and then wrap around to 0 at which point we break from the loop.

```zc
fn main() {
    let i: u128 = 1;
    while i > 0 {
        println "{i++}";
    }
}
```

Alternatively, using bigints, this will carry on (in theory at least) until memory is exhausted.

```zc
import "std/bigint.zc"

fn main() {
    let bi  = BigInt::from_int(1);
    let one = BigInt::from_int(1);
    let count = 0;
    loop {
         println "{bi}";
         bi.add_in_place(&one);
    }
}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Integer sequence**](https://rosettacode.org/wiki/Integer_sequence) in Zen C.

*This article uses material from the Rosetta Code article **Integer sequence**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Integer_sequence?action=history).*
