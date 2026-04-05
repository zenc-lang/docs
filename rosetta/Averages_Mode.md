+++
title = "Averages/Mode"
+++

# Averages/Mode

```zc
import "std/map.zc"
import "std/vec.zc"

fn mode<T>(a: T*, n: const usize) {
    if n == 0 {
        println "There are no modes as the array is empty.";
        return;
    }
    let m = Map<int>::new();
    for i in 0..n {
        let k = "{a[i]}";
        if m.contains(k) {
            let val = m[k].unwrap();
            m.put(k, ++val);
        } else {
            m.put(k, 1);
        }
    }
    let most = 0;
    for entry in m {
        if entry.val > most { most = entry.val; }
    }
    let modes = Vec<string>::new();
    for entry in m {
        if entry.val == most { modes << entry.key; }
    }
    print "For the array : [";
    for i in 0..n { print "{a[i]}, "; }
    println "\b\b]";
    print "  mode(s)     : ";
    for mo in modes { print "{mo}, "; }
    println "\b\b \n  occurrences : {most}";
}

fn main() {
    let a = [1, 3, 5, 7, 1, 3, 1, 2, 3];
    mode<int>(a, 9);
    println "";
    let b = ["a", "b", "c", "a", "b", "a", "b", "b", "c"];
    mode<string>(b, 9);
}
```

**Output:**

```
For the array : [1, 3, 5, 7, 1, 3, 1, 2, 3] 
  mode(s)     : 3, 1  
  occurrences : 3

For the array : [a, b, c, a, b, a, b, b, c] 
  mode(s)     : b  
  occurrences : 4
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Averages/Mode**](https://rosettacode.org/wiki/Averages/Mode) in Zen C.

*This article uses material from the Rosetta Code article **Averages/Mode**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Averages/Mode?action=history).*
