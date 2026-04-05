+++
title = "Show the (decimal) value of a number of 1s appended with a 3, then squared"
+++

# Show the (decimal) value of a number of 1s appended with a 3, then squared

```zc
fn main() {
    let s: char[9];
    for n in 0..8 {
        if n > 0 { s[n - 1] = '1'; }
        s[n] = '3';
        s[n + 1] = '\0';
        let i: u64 = atoll(s);
        println "{s:9s} {i * i:15llu}";
    }
}
```

**Output:**

```
3               9
       13             169
      113           12769
     1113         1238769
    11113       123498769
   111113     12346098769
  1111113   1234572098769
 11111113 123456832098769
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Show the (decimal) value of a number of 1s appended with a 3, then squared**](https://rosettacode.org/wiki/Show_the_(decimal)_value_of_a_number_of_1s_appended_with_a_3,_then_squared) in Zen C.

*This article uses material from the Rosetta Code article **Show the (decimal) value of a number of 1s appended with a 3, then squared**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Show_the_(decimal)_value_of_a_number_of_1s_appended_with_a_3,_then_squared?action=history).*
