+++
title = "Rep-string"
+++

# Rep-string

```zc
fn substring(s: char*, ss: char*, index: int, len: usize) {
    strncpy(ss, s + index, len);
    ss[len] = '\0';
}

fn mul_string(s: char*, mul: char*, n: const int) {
    let len = strlen(s)
    let ptr = mul;
    for i in 1..=n {
        strcpy(ptr, s);
        ptr += len;
    }
    *ptr = '\0';
}

fn rep_string(s: char*) {
    let rep: char[10];
    rep[0] = '\0';
    let size = strlen(s);
    if size >= 2 {
        for i in 0..size {
            assert(s[i] == '0' || s[i] == '1', "Argument is not a binary string.");
        }
        for len in 1..=size / 2 {
            let t: char[10];
            substring(s, t, 0, len);
            let n = size / len;
            let r = size % len;
            let u: char[20];
            mul_string(t, u, n);
            strncat(u, t, r);
            if !strcmp(u, s) {
                strcpy(rep, t);
                rep[strlen(t)] = '\0';
            }
        }
    }
    print "{s:10s} -> ";
    if strlen(rep) > 0 {
        println "{rep}";
    } else {
        println "Not a rep-string";
    }
}

fn main() {
    println "The (longest) rep-strings are:\n";
    let strings: string[11] = [
        "1001110011",
        "1110111011",
        "0010010010",
        "1010101010",
        "1111111111",
        "0100101101",
        "0100100",
        "101",
        "11",
        "00",
        "1"
    ];
    for s in strings { rep_string(s); }
}
```

**Output:**

```
The (longest) rep-strings are:

1001110011 -> 10011
1110111011 -> 1110
0010010010 -> 001
1010101010 -> 1010
1111111111 -> 11111
0100101101 -> Not a rep-string
   0100100 -> 010
       101 -> Not a rep-string
        11 -> 1
        00 -> 0
         1 -> Not a rep-string
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Rep-string**](https://rosettacode.org/wiki/Rep-string) in Zen C.

*This article uses material from the Rosetta Code article **Rep-string**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Rep-string?action=history).*
