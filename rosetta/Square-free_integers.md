+++
title = "Square-free integers"
+++

# Square-free integers

```zc
fn is_square_free(n: u64) -> bool {
    let i: u64 = 2;
    let s: u64;
    while (s = i * i) <= n {
        if n % s == 0 { return false; }
        i += (i > 2) ? 2 : 1;
    }
    return true;
}

fn main() {
    let count = 0;
    println "The square-free integers between 1 and 145 inclusive are:";
    for let i: u64 = 1; i <= 145; ++i {
        if is_square_free(i) {
            print "{i:3lu} ";
            if !(++count % 20) { println ""; }
        }
    }

    count = 0;
    println "\n\nThe square-free integers between 1000000000000 and 1000000000145 inclusive are:";
    for let i: u64 = 1000000000000; i <= 1000000000145; ++i {
        if is_square_free(i) {
            print "{i:3lu} ";
            if !(++count % 5) { println ""; }
        }
    }

    count = 0;
    let pow: u64 = 100;
    println "\n\nCounts of square-free integers:";
    for let i: u64 = 1; i <= 1000000; ++i {
        if is_square_free(i) { count++; }
        if i == pow {
             println "  from 1 to {pow:-7lu} = {count}";
             pow *= 10;
        }
    }
}
```

**Output:**

```
The square-free integers between 1 and 145 inclusive are:
  1   2   3   5   6   7  10  11  13  14  15  17  19  21  22  23  26  29  30  31 
 33  34  35  37  38  39  41  42  43  46  47  51  53  55  57  58  59  61  62  65 
 66  67  69  70  71  73  74  77  78  79  82  83  85  86  87  89  91  93  94  95 
 97 101 102 103 105 106 107 109 110 111 113 114 115 118 119 122 123 127 129 130 
131 133 134 137 138 139 141 142 143 145 

The square-free integers between 1000000000000 and 1000000000145 inclusive are:
1000000000001 1000000000002 1000000000003 1000000000005 1000000000006 
1000000000007 1000000000009 1000000000011 1000000000013 1000000000014 
1000000000015 1000000000018 1000000000019 1000000000021 1000000000022 
1000000000023 1000000000027 1000000000029 1000000000030 1000000000031 
1000000000033 1000000000037 1000000000038 1000000000039 1000000000041 
1000000000042 1000000000043 1000000000045 1000000000046 1000000000047 
1000000000049 1000000000051 1000000000054 1000000000055 1000000000057 
1000000000058 1000000000059 1000000000061 1000000000063 1000000000065 
1000000000066 1000000000067 1000000000069 1000000000070 1000000000073 
1000000000074 1000000000077 1000000000078 1000000000079 1000000000081 
1000000000082 1000000000085 1000000000086 1000000000087 1000000000090 
1000000000091 1000000000093 1000000000094 1000000000095 1000000000097 
1000000000099 1000000000101 1000000000102 1000000000103 1000000000105 
1000000000106 1000000000109 1000000000111 1000000000113 1000000000114 
1000000000115 1000000000117 1000000000118 1000000000119 1000000000121 
1000000000122 1000000000123 1000000000126 1000000000127 1000000000129 
1000000000130 1000000000133 1000000000135 1000000000137 1000000000138 
1000000000139 1000000000141 1000000000142 1000000000145 

Counts of square-free integers:
  from 1 to 100     = 61
  from 1 to 1000    = 608
  from 1 to 10000   = 6083
  from 1 to 100000  = 60794
  from 1 to 1000000 = 607926
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Square-free integers**](https://rosettacode.org/wiki/Square-free_integers) in Zen C.

*This article uses material from the Rosetta Code article **Square-free integers**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Square-free_integers?action=history).*
