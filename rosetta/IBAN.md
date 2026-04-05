+++
title = "IBAN"
+++

# IBAN

```zc
import "std/string.zc"
import "std/vec.zc"

fn main() {
    let iban = "GB82 WEST 1234 5698 7654 32";
    let s = Vec<char>::new();
    
    // Clean and normalize using for-in and match
    for c in String::from(iban).chars() {
        match c {
            'a'..='z' => s.push((char)((int)c - 32)),
            'A'..='Z', '0'..='9' => s.push((char)c),
            _ => {}
        }
    }

    // Modulo 97 calculation
    let rem = 0;
    let n = s.len;
    for let i = 0; i < n; i += 1 {
        let c = s.get((i + 4) % n);
        match c {
            '0'..='9' => rem = (rem * 10 + (int)(c - '0')) % 97,
            'A'..='Z' => rem = (rem * 100 + (int)(c - 'A' + 10)) % 97,
            _ => {}
        }
    }
    
    println "IBAN: {iban}";
    if rem == 1 {
        println "Valid: Yes";
    } else {
        println "Valid: No";
    }
}
```

**Output:**

```
IBAN: GB82 WEST 1234 5698 7654 32
Valid: Yes
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**IBAN**](https://rosettacode.org/wiki/IBAN) in Zen C.

*This article uses material from the Rosetta Code article **IBAN**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/IBAN?action=history).*
