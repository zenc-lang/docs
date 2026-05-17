+++
title = "Soundex"
+++

# Soundex

{{trans|Kotlin}}

```zc
import "std/string.zc"
import "ctype.h"

fn get_code(c: char) -> char {
    match c {
        'B', 'F', 'P', 'V' => { return '1'; },
        'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z' => { return '2'; },
        'D', 'T' => { return '3'},
        'L' => { return '4'; },
        'M', 'N' =>  { return '5'; },
        'R' => { return '6'; },
        'H', 'W' => { return '-'; },
        _ => { return ' '; }
    }
}

fn soundex(s: string) -> String {
    let len = strlen(s);
    let sb = String::new("");
    if len == 0 { return sb; }
    sb.push_rune(toupper(s[0]));
    let prev = get_code(toupper(s[0]));
    for i in 1..len {
        let curr = get_code(toupper(s[i]));
        if curr != ' ' && curr != '-' && curr != prev { sb.push_rune(curr); }
        if curr != '-' { prev = curr; }
    }
    let sb2 = sb.pad_right(4, '0');
    return sb2.substring(0, 4);
}

fn main() {
    let pairs: (string, string)[16] =  [
        ("Ashcraft",  "A261"),
        ("Ashcroft",  "A261"),
        ("Gauss",     "G200"),
        ("Ghosh",     "G200"),
        ("Hilbert",   "H416"),
        ("Heilbronn", "H416"),
        ("Lee",       "L000"),
        ("Lloyd",     "L300"),
        ("Moses",     "M220"),
        ("Pfister",   "P236"),
        ("Robert",    "R163"),
        ("Rupert",    "R163"),
        ("Rubin",     "R150"),
        ("Tymczak",   "T522"),
        ("Soundex",   "S532"),
        ("Example",   "E251")
    ];

    for i in 0..pairs.len {
        let (p1, p2) = pairs[i];
        let s = soundex(p1);
        let ps = String::from(p2);
        println "{p1:-9s} -> {p2} -> {s == &ps}";
    }
}
```

**Output:**

```
Ashcraft  -> A261 -> true
Ashcroft  -> A261 -> true
Gauss     -> G200 -> true
Ghosh     -> G200 -> true
Hilbert   -> H416 -> true
Heilbronn -> H416 -> true
Lee       -> L000 -> true
Lloyd     -> L300 -> true
Moses     -> M220 -> true
Pfister   -> P236 -> true
Robert    -> R163 -> true
Rupert    -> R163 -> true
Rubin     -> R150 -> true
Tymczak   -> T522 -> true
Soundex   -> S532 -> true
Example   -> E251 -> true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Soundex**](https://rosettacode.org/wiki/Soundex) in Zen C.

*This article uses material from the Rosetta Code article **Soundex**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Soundex?action=history).*
