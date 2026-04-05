+++
title = "Count occurrences of a substring"
+++

# Count occurrences of a substring

```zc
fn str_occurs(s: string, t: string) -> int {
    let ptr = s;
    let count = 0;
    let l = strlen(t);
    if l == 0 { return -1; }
    loop {
        ptr = strstr(ptr, t);
        if ptr {
            count++;
            ptr += l;
        } else {
            break;
        }
    }
    return count;
}

fn str_quote(s: string, q: char*) {
    sprintf(q, "'%s'", s);
}

fn main() {
    let t1 = ["the three truths", "th"];
    let t2 = ["ababababab", "abab"];
    let t3 = ["abaabba*bbaba*bbab", "a*b"];
    let t4 = ["aaaaaaaaaaaaaa", "aa"];
    let t5 = ["aaaaaaaaaaaaaa", "b"];
    let ts: string*[5] = [t1, t2, t3, t4, t5];
    let q: char[10];
    for i in 0..5 {
        let t = ts[i];
        let count = str_occurs(t[0], t[1]);
        str_quote(t[1], q);
        println "{q:6s} occurs {count} times in '{t[0]}'";
    }
}
```

**Output:**

```
'th' occurs 3 times in 'the three truths'
'abab' occurs 2 times in 'ababababab'
 'a*b' occurs 2 times in 'abaabba*bbaba*bbab'
  'aa' occurs 7 times in 'aaaaaaaaaaaaaa'
   'b' occurs 0 times in 'aaaaaaaaaaaaaa'
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Count occurrences of a substring**](https://rosettacode.org/wiki/Count_occurrences_of_a_substring) in Zen C.

*This article uses material from the Rosetta Code article **Count occurrences of a substring**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Count_occurrences_of_a_substring?action=history).*
