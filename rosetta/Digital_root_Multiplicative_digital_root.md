+++
title = "Digital root/Multiplicative digital root"
+++

# Digital root/Multiplicative digital root

{{trans|Wren}}

```zc
import "std/vec.zc"

fn mult(n: u64, base: int) -> u64 {
    let m: u64 = 1;
    while m > 0 && n > 0 {
        let div = n / base;
        let rem = n % base;
        m *= rem;
        n = div;
    }
    return m;
}

// Only valid for n >= 0 && base >= 2.
fn mult_digital_root(n: u64, base: int) -> (int, int) {
    let mp = 0;
    while n >= base {
        n = mult(n, base);
        mp++;
    }
    return (mp, (int)n);
}

fn main() {
    def BASE = 10;
    def SIZE = 5;
    let tests: u64[7] = [
        123321, 7739, 893, 899998, 18446743999999999999, 3778888999, 277777788888899
    ];
    printf("%20s %3s %3s\n", "Number", "MDR", "MP");
    for n in tests {
        let (mp, dr) = mult_digital_root(n, BASE);
        printf("%20lu %3d %3d\n", n, dr, mp);
    }

    let list: Vec<u64>[BASE];
    for i in 0..BASE { list[i] = Vec<u64>::new(); }
    let cnt = SIZE * BASE;
    for let n: u64 = 0; cnt > 0; ++n {
        let (_, mdr) = mult_digital_root(n, BASE);
        if list[mdr].length() < SIZE {
            list[mdr] << n;
            cnt--;
        }
    }
    printf("\n%3s: %s\n", "MDR", "First");
    for i in 0..BASE {
        print "{i:3d}: [";
        for v in list[i] { print "{v}, "; }
        println "\b\b]";
    }
    for i in 0..BASE { list[i].free(); }
}
```

**Output:**

```
Number MDR  MP
              123321   8   3
                7739   8   3
                 893   2   3
              899998   0   2
18446743999999999999   0   2
          3778888999   0  10
     277777788888899   0  11

MDR: First
  0: [0, 10, 20, 25, 30] 
  1: [1, 11, 111, 1111, 11111] 
  2: [2, 12, 21, 26, 34] 
  3: [3, 13, 31, 113, 131] 
  4: [4, 14, 22, 27, 39] 
  5: [5, 15, 35, 51, 53] 
  6: [6, 16, 23, 28, 32] 
  7: [7, 17, 71, 117, 171] 
  8: [8, 18, 24, 29, 36] 
  9: [9, 19, 33, 91, 119]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Digital root/Multiplicative digital root**](https://rosettacode.org/wiki/Digital_root/Multiplicative_digital_root) in Zen C.

*This article uses material from the Rosetta Code article **Digital root/Multiplicative digital root**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Digital_root/Multiplicative_digital_root?action=history).*
