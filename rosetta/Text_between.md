+++
title = "Text between"
+++

# Text between

```zc
import "std/string.zc"

fn text_between(str: string, start: string, end: string) -> String {
    if strlen(start) == 0 || strlen(end) == 0 {
        eprintln "Start and end must both be non-empty strings.";
    }
    if strlen(str) == 0 { return String::new(""); }
    let s: int;
    let t: int;
    if strcmp(start, "start") == 0 {
        s = 0;
        t = 0;
    } else {
        let u = strstr(str, start);
        if u {
            s = u - str;
            t = s + strlen(start);
        } else {
            return String::new("");
        }
    }
    let e: int;
    if strcmp(end, "end") == 0 {
        e = strlen(str);
    } else {
        let u = strstr(str + t, end);
        if u {
            e = u - str;
        } else {
            let ss = String::from(str);
            return ss.substring(t, ss.length() - t);
        }
    }
    let ss = String::from(str);
    return ss.substring(t, e - t);
}

fn main() {
    let texts = [
        "Hello Rosetta Code world",
        "Hello Rosetta Code world",
        "Hello Rosetta Code world",
        "</div><div style=\"chinese\">你好嗎</div>",
        "<text>Hello <span>Rosetta Code</span> world</text><table style=\"myTable\">",
        "<table style=\"myTable\"><tr><td>hello world</td></tr></table>",
        "The quick brown fox jumps over the lazy other fox",
        "One fish two fish red fish blue fish",
        "FooBarBazFooBuxQuux"
    ];

    let starts = [
        "Hello ", "start", "Hello ", "<div style=\"chinese\">",
        "<text>", "<table>", "quick ", "fish ", "Foo"
    ];

    let ends = [
        " world", " world", "end", "</div>", "<table>",
        "</table>", " fox", " red", "Foo"
    ];

    for i, text in texts {
        println "Text   : \"{text}\"";
        println "Start  : \"{starts[i]}\"";
        println "End    : \"{ends[i]}\"";
        let b = text_between(text, starts[i], ends[i]);
        println "Result : \"{b}\"\n"; 
    }
}
```

**Output:**

```
Text   : "Hello Rosetta Code world"
Start  : "Hello "
End    : " world"
Result : "Rosetta Code"

Text   : "Hello Rosetta Code world"
Start  : "start"
End    : " world"
Result : "Hello Rosetta Code"

Text   : "Hello Rosetta Code world"
Start  : "Hello "
End    : "end"
Result : "Rosetta Code world"

Text   : "</div><div style="chinese">你好嗎</div>"
Start  : "<div style="chinese">"
End    : "</div>"
Result : "你好嗎"

Text   : "<text>Hello <span>Rosetta Code</span> world</text><table style="myTable">"
Start  : "<text>"
End    : "<table>"
Result : "Hello <span>Rosetta Code</span> world</text><table style="myTable">"

Text   : "<table style="myTable"><tr><td>hello world</td></tr></table>"
Start  : "<table>"
End    : "</table>"
Result : ""

Text   : "The quick brown fox jumps over the lazy other fox"
Start  : "quick "
End    : " fox"
Result : "brown"

Text   : "One fish two fish red fish blue fish"
Start  : "fish "
End    : " red"
Result : "two fish"

Text   : "FooBarBazFooBuxQuux"
Start  : "Foo"
End    : "Foo"
Result : "BarBaz"
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Text between**](https://rosettacode.org/wiki/Text_between) in Zen C.

*This article uses material from the Rosetta Code article **Text between**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Text_between?action=history).*
