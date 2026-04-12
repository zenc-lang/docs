+++
title = "Integer overflow"
+++

# Integer overflow

Although not shown there are compiler overflow warnings for all of the signed cases and some of the unsigned cases.

```zc
fn main() {
    let int32s: i32[5] = [
        -(-2147483647-1),
        2000000000 + 2000000000,
        -2147483647 - 2147483647,
        46341 * 46341,
        (-2147483647-1) / -1
    ];
    println "Signed 32-bit:";
    for i in int32s { println "{i}" }

    let int64s: i64[5] = [
        -(-9223372036854775807-1),
        5000000000000000000+5000000000000000000,
        -9223372036854775807 - 9223372036854775807,
        3037000500 * 3037000500,
        (-9223372036854775807-1) / -1
    ];
    println "\nSigned 64-bit:";
    for i in int64s { println "{i}" }

    let uint32s: u32[4] = [
        -4294967295,
        3000000000 + 3000000000,
        2147483647 - 4294967295,
        65537 * 65537
    ];
    println "\nUnsigned 32-bit:";
    for i in uint32s { println "{i}" }

    let uint64s: u64[4] = [
        -18446744073709551615,
        10000000000000000000 + 10000000000000000000,
        9223372036854775807 - 18446744073709551615,
        4294967296 * 4294967296
    ];
    println "\nUnsigned 64-bit:";
    for i in uint64s { println "{i}" }
}
```

**Output:**

```
Signed 32-bit:
-2147483648
-294967296
2
-2147479015
-2147483648

Signed 64-bit:
-9223372036854775808
-8446744073709551616
2
-9223372036709301616
-9223372036854775808

Unsigned 32-bit:
1
1705032704
2147483648
131073

Unsigned 64-bit:
1
1553255926290448384
9223372036854775808
0
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Integer overflow**](https://rosettacode.org/wiki/Integer_overflow) in Zen C.

*This article uses material from the Rosetta Code article **Integer overflow**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Integer_overflow?action=history).*
