+++
title = "Bernoulli's triangle"
+++

# Bernoulli's triangle

```zc
fn main() {
    let rows = 15;
    let triangle: uint[15][15];

    for n in 0..rows {

        triangle[n][0] = 1;
 
        for k in 1..n {
            triangle[n][k] = triangle[n-1][k] + triangle[n-1][k-1];
        }
 
        if n > 0 {
            triangle[n][n] = 2 * triangle[n-1][n-1];
        }
    }

    // Print the triangle
    for n in 0..rows {
        for k in 0..=n {
            print "{triangle[n][k]} ";
        }
        println "";
    }
}
```

**Output:**

```
1 
1 2 
1 3 4 
1 4 7 8 
1 5 11 15 16 
1 6 16 26 31 32 
1 7 22 42 57 63 64 
1 8 29 64 99 120 127 128 
1 9 37 93 163 219 247 255 256 
1 10 46 130 256 382 466 502 511 512 
1 11 56 176 386 638 848 968 1013 1023 1024 
1 12 67 232 562 1024 1486 1816 1981 2036 2047 2048 
1 13 79 299 794 1586 2510 3302 3797 4017 4083 4095 4096 
1 14 92 378 1093 2380 4096 5812 7099 7814 8100 8178 8191 8192 
1 15 106 470 1471 3473 6476 9908 12911 14913 15914 16278 16369 16383 16384
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Bernoulli's triangle**](https://rosettacode.org/wiki/Bernoulli's_triangle) in Zen C.

*This article uses material from the Rosetta Code article **Bernoulli's triangle**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Bernoulli's_triangle?action=history).*
