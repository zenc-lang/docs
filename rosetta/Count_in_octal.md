+++
title = "Count in octal"
+++

# Count in octal

Using the U8 type for the counter variable so we don't go on too long, stopping at 0o377 :)

```zc
fn main() {
    println "0";
    for let i: u8 = 1; i > 0; ++i {
        println "{i:o}";
    }
}
```

**Output:**

```
0
1
2
3
4
5
6
7
10
11
12
13
14
15
16
17
20
..
367
370
371
372
373
374
375
376
377
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Count in octal**](https://rosettacode.org/wiki/Count_in_octal) in Zen C.

*This article uses material from the Rosetta Code article **Count in octal**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Count_in_octal?action=history).*
