+++
title = "Two identical strings"
+++

# Two identical strings

```zc
fn batoi(s: string) -> int {
    let res = 0;
    for i in 0..strlen(s) {
        let d = s[i] - 48;
        res = res * 2 + d;
    }
    return res;
}

fn main() {
    let i = 1;
    let s: [char; 20];
    loop {
        let b2 = "{i:b}";
        strcat(s, b2);
        strcat(s, b2);
        let d = batoi(s);
        if d >= 1000 { break; }
        println "{d:3d} : {s}";
        i++;
        s[0] = '\0';
    }
    println "\nFound {i - 1} numbers.";
}
```

**Output:**

```
3 : 11
 10 : 1010
 15 : 1111
 36 : 100100
 45 : 101101
 54 : 110110
 63 : 111111
136 : 10001000
153 : 10011001
170 : 10101010
187 : 10111011
204 : 11001100
221 : 11011101
238 : 11101110
255 : 11111111
528 : 1000010000
561 : 1000110001
594 : 1001010010
627 : 1001110011
660 : 1010010100
693 : 1010110101
726 : 1011010110
759 : 1011110111
792 : 1100011000
825 : 1100111001
858 : 1101011010
891 : 1101111011
924 : 1110011100
957 : 1110111101
990 : 1111011110

Found 30 numbers.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Two identical strings**](https://rosettacode.org/wiki/Two_identical_strings) in Zen C.

*This article uses material from the Rosetta Code article **Two identical strings**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Two_identical_strings?action=history).*
