+++
title = "Convert seconds to compound duration"
+++

# Convert seconds to compound duration

{{trans|Wren}}

```zc
fn ends_with(s1: char*, s2: char*) -> bool {
    let l1 = strlen(s1);
    let l2 = strlen(s2);
    if l2 > l1 { return false; }
    for i in 0..l2 {
        if s1[l1 - i - 1] != s2[l2 - i - 1] { return false; }
    }
    return true;
}

fn duration(s: int) {
    if s < 1 {
        println "0 sec";
        return;
    }
    let dur: char[30] = [0];
    let divs: int[5] = [7, 24, 60, 60, 1];
    let units: string[5] = ["wk", "d", "hr", "min", "sec"];
    let t = 1;
    for d in divs { t *= d; }
    for i in 0..5 {
        let u = s / t;
        if u > 0 {
            strcat(dur, "{u} {units[i]}, ");
            s %= t;
        }
        t /= divs[i];
    }
    if ends_with(dur, ", ") { dur[strlen(dur) - 2] = '\0'; }
    println "{dur}";
}

fn main() {
    let tests: int[3] = [7_259, 86_400, 6_000_000];
    for t in tests { duration(t); }
}
```

**Output:**

```
2 hr, 59 sec
1 d
9 wk, 6 d, 10 hr, 40 min
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Convert seconds to compound duration**](https://rosettacode.org/wiki/Convert_seconds_to_compound_duration) in Zen C.

*This article uses material from the Rosetta Code article **Convert seconds to compound duration**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Convert_seconds_to_compound_duration?action=history).*
