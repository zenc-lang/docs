+++
title = "Determine if a string is squeezable"
+++

# Determine if a string is squeezable

{{trans|Wren}}

```zc
import "std/string.zc"

fn squeeze(s: string, r: rune) {
    let ss = String::new(s)
    let c = ss.runes();
    let le = (int)c.length();
    let ch = String::from_rune(r);
    println "Specified character = '{ch}'";
    println "original : length = {le:2d}, string = «««{s}»»»";
    if le >= 2 {
        for let i = le - 2; i >= 0; --i {
            if c[i] == r && c[i] == c[i + 1] { c.remove(i); }
        }
        let cl = (int)c.length();
        let cs = String::from_runes_vec(c);
        println "squeezed : length = {cl:2d}, string = «««{cs}»»»\n";
    } else {
        println "squeezed: length = {le:2d}, string = «««{s}»»»\n";
    }
}

fn main() {
    let strings = [
        "",
        "\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ",
        "..1111111111111111111111111111111111111111111111111111111111111117777888",
        "I never give 'em hell, I just tell the truth, and they think it's hell. ",
        "                                                   ---  Harry S Truman  ",
        "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
        "headmistressship",
        "aardvark",
        "😍😀🙌💃😍😍😍🙌"
    ];

    let spec = [ " ", "-", "7", ".", " -r", "e", "s", "a", "😍" ];

    for i in 0..strings.len {
        let s = String::new(spec[i]);
        for ch in s { squeeze(strings[i], ch); } 
    }
}
```

**Output:**

```
Specified character = ' '
original : length =  0, string = «««»»»
squeezed: length =  0, string = «««»»»

Specified character = '-'
original : length = 72, string = «««"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln »»»
squeezed : length = 70, string = «««"If I were two-faced, would I be wearing this one?" - Abraham Lincoln »»»

Specified character = '7'
original : length = 72, string = «««..1111111111111111111111111111111111111111111111111111111111111117777888»»»
squeezed : length = 69, string = «««..1111111111111111111111111111111111111111111111111111111111111117888»»»

Specified character = '.'
original : length = 72, string = «««I never give 'em hell, I just tell the truth, and they think it's hell. »»»
squeezed : length = 72, string = «««I never give 'em hell, I just tell the truth, and they think it's hell. »»»

Specified character = ' '
original : length = 72, string = «««                                                   ---  Harry S Truman  »»»
squeezed : length = 20, string = ««« --- Harry S Truman »»»

Specified character = '-'
original : length = 72, string = «««                                                   ---  Harry S Truman  »»»
squeezed : length = 70, string = «««                                                   -  Harry S Truman  »»»

Specified character = 'r'
original : length = 72, string = «««                                                   ---  Harry S Truman  »»»
squeezed : length = 71, string = «««                                                   ---  Hary S Truman  »»»

Specified character = 'e'
original : length = 80, string = «««The better the 4-wheel drive, the further you'll be from help when ya get stuck!»»»
squeezed : length = 79, string = «««The better the 4-whel drive, the further you'll be from help when ya get stuck!»»»

Specified character = 's'
original : length = 16, string = «««headmistressship»»»
squeezed : length = 14, string = «««headmistreship»»»

Specified character = 'a'
original : length =  8, string = «««aardvark»»»
squeezed : length =  7, string = «««ardvark»»»

Specified character = '😍'
original : length =  8, string = «««😍😀🙌💃😍😍😍🙌»»»
squeezed : length =  6, string = «««😍😀🙌💃😍🙌»»»
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Determine if a string is squeezable**](https://rosettacode.org/wiki/Determine_if_a_string_is_squeezable) in Zen C.

*This article uses material from the Rosetta Code article **Determine if a string is squeezable**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Determine_if_a_string_is_squeezable?action=history).*
