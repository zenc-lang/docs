+++
title = "Determine if a string is collapsible"
+++

# Determine if a string is collapsible

{{trans|Wren}}

```zc
import "std/string.zc"

fn collapse(s: string) {
    let ss = String::new(s);
    let c = ss.runes();
    let le = (int)c.length();
    println "original : length = {le:2d}, string = «««{s}»»»";
    if le >= 2 {
        for let i = le - 2; i >= 0; --i {
            if c[i] == c[i + 1] { c.remove(i); }
        }
        let cl = (int)c.length();
        let cs = String::from_runes_vec(c);
        println "collapsed: length = {cl:2d}, string = «««{cs}»»»\n";
    } else {
        println "collapsed: length = {le:2d}, string = «««{s}»»»\n";
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
    for s in strings { collapse(s); }
}
```

**Output:**

```
original : length =  0, string = «««»»»
collapsed: length =  0, string = «««»»»

original : length = 72, string = «««"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln »»»
collapsed: length = 70, string = «««"If I were two-faced, would I be wearing this one?" - Abraham Lincoln »»»

original : length = 72, string = «««..1111111111111111111111111111111111111111111111111111111111111117777888»»»
collapsed: length =  4, string = «««.178»»»

original : length = 72, string = «««I never give 'em hell, I just tell the truth, and they think it's hell. »»»
collapsed: length = 69, string = «««I never give 'em hel, I just tel the truth, and they think it's hel. »»»

original : length = 72, string = «««                                                   ---  Harry S Truman  »»»
collapsed: length = 17, string = ««« - Hary S Truman »»»

original : length = 80, string = «««The better the 4-wheel drive, the further you'll be from help when ya get stuck!»»»
collapsed: length = 77, string = «««The beter the 4-whel drive, the further you'l be from help when ya get stuck!»»»

original : length = 16, string = «««headmistressship»»»
collapsed: length = 14, string = «««headmistreship»»»

original : length =  8, string = «««aardvark»»»
collapsed: length =  7, string = «««ardvark»»»

original : length =  8, string = «««😍😀🙌💃😍😍😍🙌»»»
collapsed: length =  6, string = «««😍😀🙌💃😍🙌»»»
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Determine if a string is collapsible**](https://rosettacode.org/wiki/Determine_if_a_string_is_collapsible) in Zen C.

*This article uses material from the Rosetta Code article **Determine if a string is collapsible**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Determine_if_a_string_is_collapsible?action=history).*
