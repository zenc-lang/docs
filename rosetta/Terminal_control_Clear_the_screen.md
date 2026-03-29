+++
title = "Terminal control/Clear the screen"
+++

# Terminal control/Clear the screen

For terminals which support ANSI escape codes:

```zc

```

**Output:**

```
def ESC = "\x1b";

fn main() {
    println "{ESC}[2J";
}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Terminal control/Clear the screen**](https://rosettacode.org/wiki/Terminal_control/Clear_the_screen) in Zen C.

*This article uses material from the Rosetta Code article **Terminal control/Clear the screen**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Terminal_control/Clear_the_screen?action=history).*
