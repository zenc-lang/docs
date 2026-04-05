+++
title = "Environment variables"
+++

# Environment variables

```zc
import "std/env.zc"

fn main() {
    let shell = Env::get_dup("SHELL").unwrap();
    println "{shell}";
}
```

**Output:**

```
/bin/bash
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Environment variables**](https://rosettacode.org/wiki/Environment_variables) in Zen C.

*This article uses material from the Rosetta Code article **Environment variables**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Environment_variables?action=history).*
