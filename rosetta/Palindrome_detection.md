+++
title = "Palindrome detection"
+++

# Palindrome detection

```zc
import "std/string.zc"

fn reverse_str(s: string) -> string {
    let s2 = String::from(s);
    let r = s2.runes();
    r.reverse();
    return String::from_runes_vec(r).c_str();
}

fn is_pal(s: string) -> bool {
    if strlen(s) > 0 { return s == reverse_str(s);}
    return true;
}

fn main() {
    println "Are the following palindromes?";
    let phrases = ["rotor", "rosetta", "step on no pets", "été", "zenc", "🦊😀🦊"];
    for phrase in phrases {
        println "  {phrase} => {is_pal(phrase)}";
    }
}
```

**Output:**

```
Are the following palindromes?
  rotor => true
  rosetta => false
  step on no pets => true
  été => true
  zenc => false
  🦊😀🦊 => true
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Palindrome detection**](https://rosettacode.org/wiki/Palindrome_detection) in Zen C.

*This article uses material from the Rosetta Code article **Palindrome detection**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Palindrome_detection?action=history).*
