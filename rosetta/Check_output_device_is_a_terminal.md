+++
title = "Check output device is a terminal"
+++

# Check output device is a terminal

POSIX only.

```zc
import "unistd.h"

fn main() {
    let res = isatty(fileno(stdout)) ? "true" : "false";
    println "Output device is a terminal? {res}";
}
```

**Output:**

```
Output device is a terminal? true
```

Or, if we redirect output to a file:

```
$ zc build Check_output_device_is_a_terminal.zc
$./Check_output_device_is_a_terminal > tmp
$cat tmp
Output device is a terminal? false
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Check output device is a terminal**](https://rosettacode.org/wiki/Check_output_device_is_a_terminal) in Zen C.

*This article uses material from the Rosetta Code article **Check output device is a terminal**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Check_output_device_is_a_terminal?action=history).*
