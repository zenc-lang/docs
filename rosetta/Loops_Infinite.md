+++
title = "Loops/Infinite"
+++

# Loops/Infinite

Zen C provides a dedicated <code>loop</code> keyword for creating infinite loops. This is the idiomatic alternative to <code>while (true)</code>. Zen C also supports loop labels (like, <code>outer: loop</code>) to easily break out of deeply nested infinite loops.

```zc
fn main() {
    // A simple infinite loop
    loop {
        println "SPAM";
    }
}
```

**Output:**

```
SPAM
SPAM
SPAM
SPAM
SPAM
...
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Loops/Infinite**](https://rosettacode.org/wiki/Loops/Infinite) in Zen C.

*This article uses material from the Rosetta Code article **Loops/Infinite**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Loops/Infinite?action=history).*
