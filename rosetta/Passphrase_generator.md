+++
title = "Passphrase generator"
+++

# Passphrase generator

{{trans|Wren}}

```zc
import "std/fs.zc"
import "std/vec.zc"
import "std/string.zc"
import "std/random.zc"
import "ctype.h"

let candidates: Vec<String>;
let nc: usize;
let rng: Random;

// Get all words in unixdict.txt between 4 and 9 letters long.
fn get_candidates() {
    candidates = File::read_lines("unixdict.txt").unwrap();
    for (let i: isize = candidates.length() - 1; i >= 0; --i) {
        let len = candidates[i].length();
        if len < 4 || len > 9 {
            let c = candidates.remove(i);
            c.free();
        }
    }
    nc = candidates.length();
}

fn passphrase(n: int) -> String {
    assert(n > 2 && n < 8, "There should be between 3 and 7 words.");
    let rci = Vec<int>::new();
    let rns = Vec<int>::new();
    let pp  = String::new("");

    // Get 'n' random candidate indices.
    while rci.length() < n {
        let rn = rng.next_int_range(0, (int)nc - 1);
        if !rci.contains(rn) { rci.push(rn); }
    }

    // Get 'n' random numbers between 10 and 99.
    while rns.length() < n {
        let rn = rng.next_int_range(10, 99);
        if !rns.contains(rn) { rns.push(rn); }
    }

    // Construct and return the passphrase.
    for i in 0..n {
        let word  = candidates.get_ref(rci[i]);
        let first = (*word).vec.get_ref(0);
        *first = toupper(*first);
        word.append_c("{rns[i]}");
        if i < n - 1 { word.append_c("-"); }
        pp.append_c(word.c_str());
    }
    return pp;
}

fn main() {
    get_candidates();
    rng = Random::new();
    // Generate and print 5 passphrases for n = 5.
    for _ in 0..5 {
        let pp = passphrase(5);
        println "{pp}";
    }
    for c in candidates { c.free(); }
    candidates.free();
}
```

**Output:**

Sample output:

```
Resistor27-Explicit10-Ferocity76-Convolute38-Wild58
Hutch85-Ordnance59-Jackie44-Intuition77-Festive26
Smirk30-Checklist71-Potomac23-Flowery29-Hotrod25
Assent10-Wrangle37-Twitch44-Discreet76-Weber27
Farmhouse91-Ginsberg32-Obviate52-Elect35-Fireproof61
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Passphrase generator**](https://rosettacode.org/wiki/Passphrase_generator) in Zen C.

*This article uses material from the Rosetta Code article **Passphrase generator**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Passphrase_generator?action=history).*
