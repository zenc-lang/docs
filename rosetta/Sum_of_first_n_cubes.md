+++
title = "Sum of first n cubes"
+++

# Sum of first n cubes

```zc
import "locale.h"

fn main() {
    setlocale(LC_NUMERIC, "en_US.UTF-8");
    println "Sums of the first 'n' cubes (0 <= n < 50):";
    let sum = 0;
    for i in 0..50 {
        sum += i * i * i;
        print "{sum:'9d} ";
        if i % 10 == 9 { println ""; }
    }
}
```

**Output:**

```
Sums of the first 'n' cubes (0 <= n < 50):
        0         1         9        36       100       225       441       784     1,296     2,025 
    3,025     4,356     6,084     8,281    11,025    14,400    18,496    23,409    29,241    36,100 
   44,100    53,361    64,009    76,176    90,000   105,625   123,201   142,884   164,836   189,225 
  216,225   246,016   278,784   314,721   354,025   396,900   443,556   494,209   549,081   608,400 
  672,400   741,321   815,409   894,916   980,100 1,071,225 1,168,561 1,272,384 1,382,976 1,500,625
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sum of first n cubes**](https://rosettacode.org/wiki/Sum_of_first_n_cubes) in Zen C.

*This article uses material from the Rosetta Code article **Sum of first n cubes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sum_of_first_n_cubes?action=history).*
