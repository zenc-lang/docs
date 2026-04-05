+++
title = "Terminal control/Unicode output"
+++

# Terminal control/Unicode output

```zc
import "std/env.zc"

fn supports_unicode() -> bool {
    let lang = Env::get("LANG").unwrap();
    let res = strstr(lang, "utf-8") || strstr(lang, "UTF-8");
    return (bool)res;
}

fn main() {
    if supports_unicode() {
        println "Unicode is supported on this terminal and U+25B3 is : \u25b3";
    } else {
        println "Unicode is not supported on this terminal.";
    }
}
```

**Output:**

```
Unicode is supported on this terminal and U+25B3 is : △
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Terminal control/Unicode output**](https://rosettacode.org/wiki/Terminal_control/Unicode_output) in Zen C.

*This article uses material from the Rosetta Code article **Terminal control/Unicode output**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Terminal_control/Unicode_output?action=history).*
