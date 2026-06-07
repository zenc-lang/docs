+++
title = "Stack"
+++

# Stack

```zc
import "std/stack.zc"

fn main() {
    let s = Stack<int>::new();
    println "Stack created.";
    let i = 2;
    s.push(i);
    println "'{i}' pushed onto the stack.";
    if s.length() > 0 {
         i = s.pop().unwrap();
         println "'{i}' popped from the stack.";
    }
    if s.is_empty() { println "Stack is now empty." }
}
```

**Output:**

```
Stack created.
'2' pushed onto the stack.
'2' popped from the stack.
Stack is now empty.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Stack**](https://rosettacode.org/wiki/Stack) in Zen C.

*This article uses material from the Rosetta Code article **Stack**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Stack?action=history).*
