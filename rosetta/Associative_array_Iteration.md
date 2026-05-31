+++
title = "Associative array/Iteration"
+++

# Associative array/Iteration

{{trans|Wren}}
Note that Zen C makes no guarantee about iteration order which is not necessarily the same order in which the entries were added. 

```zc
import "std/map.zc"

fn main() {
    // Create a new map with four entries.
    let capitals = Map<string>::new();
    capitals.put("France","Paris");
    capitals.put("Germany", "Berlin");
    capitals.put("Spain", "Madrid");
    capitals.put("Russia", "Moscow");

    // Iterate through the map and print out the key/value pairs.
    for entry in capitals {
        println "{{{entry.key}: {entry.val}}}";
    }
    println "";

    // Iterate through the map's slots and, if they're occupied, print out the keys.
    for i in 0..capitals.capacity() {
        if capitals.is_slot_occupied(i) { println "{capitals.key_at(i)}"; }
    }
    println "";

    // Iterate through the map's slots and, if they're occupied, print out the values.
    for i in 0..capitals.capacity() {
        if capitals.is_slot_occupied(i) { println "{capitals.val_at(i)}"; }
    }
}
```

**Output:**

```
{France: Paris}
{Russia: Moscow}
{Germany: Berlin}
{Spain: Madrid}

France
Russia
Germany
Spain

Paris
Moscow
Berlin
Madrid
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Associative array/Iteration**](https://rosettacode.org/wiki/Associative_array/Iteration) in Zen C.

*This article uses material from the Rosetta Code article **Associative array/Iteration**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Associative_array/Iteration?action=history).*
