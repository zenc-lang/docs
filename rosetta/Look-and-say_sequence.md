+++
title = "Look-and-say sequence"
+++

# Look-and-say sequence

{{trans|Wren}}

```zc
import "std/string.zc"

fn look_and_say(s: string) -> string {
    let res = String::from("");
    let digit = s[0];
    let count = 1;
    for i in 1..strlen(s) {
        if s[i] == digit {
            count++;
        } else {
            res.append_c("{count}{digit:c}");
            digit = s[i];
            count = 1;
        }
    }
    res.append_c("{count}{digit:c}");
    return res.c_str();
}

fn main() {
    let las = "1";
    for i in 1..=15 {
        println "{las}";
        las = look_and_say(las);
    }
}
```

**Output:**

```
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
11131221133112132113212221
3113112221232112111312211312113211
1321132132111213122112311311222113111221131221
11131221131211131231121113112221121321132132211331222113112211
311311222113111231131112132112311321322112111312211312111322212311322113212221
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Look-and-say sequence**](https://rosettacode.org/wiki/Look-and-say_sequence) in Zen C.

*This article uses material from the Rosetta Code article **Look-and-say sequence**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Look-and-say_sequence?action=history).*
