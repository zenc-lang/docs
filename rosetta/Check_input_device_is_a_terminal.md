+++
title = "Check input device is a terminal"
+++

# Check input device is a terminal

POSIX only.

```zc
import "unistd.h"

fn main() {
    let res = isatty(fileno(stdin)) ? "true" : "false";
    println "Input device is a terminal? {res}";
}
```

**Output:**

```
Input device is a terminal? true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Check input device is a terminal**](https://rosettacode.org/wiki/Check_input_device_is_a_terminal) in Zen C.

*This article uses material from the Rosetta Code article **Check input device is a terminal**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Check_input_device_is_a_terminal?action=history).*
