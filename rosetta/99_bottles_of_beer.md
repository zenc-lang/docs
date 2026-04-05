+++
title = "99 bottles of beer"
+++

# 99 bottles of beer

This implementation showcases Zen C's descending range loops (using the <code>step</code> keyword), the ternary operator for pluralization, and implicit string interpolation.

```zc
fn main() {
    // Descending loop from 99 down to 1
    for i in 99..0 step -1 {
        let b1 = i == 1 ? "bottle" : "bottles";
        println "{i} {b1} of beer on the wall, {i} {b1} of beer.";
        
        let next = i - 1;
        if next > 0 {
            let b2 = next == 1 ? "bottle" : "bottles";
            println "Take one down and pass it around, {next} {b2} of beer on the wall.\n";
        } else {
            println "Take one down and pass it around, no more bottles of beer on the wall.\n";
        }
    }
    
    println "No more bottles of beer on the wall, no more bottles of beer.";
    println "Go to the store and buy some more, 99 bottles of beer on the wall.";
}
```

**Output:**

```
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.

98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.

...

2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**99 bottles of beer**](https://rosettacode.org/wiki/99_bottles_of_beer) in Zen C.

*This article uses material from the Rosetta Code article **99 bottles of beer**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/99_bottles_of_beer?action=history).*
