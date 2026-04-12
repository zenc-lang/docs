+++
title = "Rainbow"
+++

# Rainbow

{{trans|Wren}}

```zc
fn main() {
    let colors: (int, int, int)[7] = [
        (255,   0,   0), // red
        (255, 128,   0), // orange
        (255, 255,   0), // yellow
        (  0, 255,   0), // green
        (  0,   0, 255), // blue
        ( 75,   0, 130), // indigo
        (128,   0, 255)  // violet
    ];
    let s = "RAINBOW";
    for i in 0..7 {
        let fore = "\e[38;2;{colors[i].0};{colors[i].1};{colors[i].2}m";
        print "{fore}{s[i]:c}";
    }
    println "";
}
```

**Output:**

<div style="background-color:#F6F6F6;padding:1em;">
<font color="#FF0000">R</font><font color="#FF8000">A</font><font color="#FFFF00">I</font><font color="#00FF00">N</font><font color="#0000FF">B</font><font color="#4B0082">O</font><font color="#8000FF">W</font><br></div>

---
**Attribution:** This is a community solution for the Rosetta Code task [**Rainbow**](https://rosettacode.org/wiki/Rainbow) in Zen C.

*This article uses material from the Rosetta Code article **Rainbow**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Rainbow?action=history).*
