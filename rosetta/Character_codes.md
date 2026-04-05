+++
title = "Character codes"
+++

# Character codes

Zen C supports standard ASCII character conversions using traditional C-style casting between <code>char</code> and integer types. Additionally, it natively supports full Unicode code points via the <code>rune</code> type, which safely casts to and from 32-bit integers (<code>uint32_t</code>).

```zc
import "std/io.zc"

fn main() {
    // Character to Code (ASCII)
    let c = 'a';
    println "The character '{c}' has a code of {(int)c} in ASCII/Unicode.";

    // Code to Character (ASCII)
    let code = 97;
    println "The code {code} corresponds to the character '{(char)code}'.";

    // Multibyte Character (Rune) to Code
    let r: rune = '🚀';
    println "The rune '{r}' has a code of {(uint32_t)r} in Unicode.";

    // Code to Multibyte Character (Rune)
    let r_code: uint32_t = 128640;
    println "The code {r_code} corresponds to the rune '{(rune)r_code}'.";
    
    // Using Unicode Escapes for conversion clarity and Hex formatting
    let r_esc: rune = '\u{2764}';
    println "The rune '{r_esc}' has code {(uint32_t)r_esc} (0x{(uint32_t)r_esc : X})";
}
```

**Output:**

```
The character 'a' has a code of 97 in ASCII/Unicode.
The code 97 corresponds to the character 'a'.
The rune '🚀' has a code of 128640 in Unicode.
The code 128640 corresponds to the rune '🚀'.
The rune '❤' has code 10084 (0x2764)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Character codes**](https://rosettacode.org/wiki/Character_codes) in Zen C.

*This article uses material from the Rosetta Code article **Character codes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Character_codes?action=history).*
