+++
title = "Day of the week"
+++

# Day of the week

```zc
import "time.h"

@crepr("struct tm")
struct tm {
    tm_mday : c_int;
    tm_mon  : c_int;
    tm_year : c_int;
}

fn main() {
    let weekday: char[10];
    let t = tm{tm_mday: 25, tm_mon: 11};
    println "Years between 2008 and 2121 when 25th December falls on Sunday:";
    print "[";
    for let year = 2008; year <= 2121; ++year {
        t.tm_year = year - 1900;
        mktime(&t);
        strftime(weekday, 10, "%A", &t);
        if (strcmp(weekday, "Sunday") == 0) { printf("%d, ", year); }
    }
    println "\b\b]";
}
```

**Output:**

```
Years between 2008 and 2121 when 25th December falls on Sunday:
[2011, 2016, 2022, 2033, 2039, 2044, 2050, 2061, 2067, 2072, 2078, 2089, 2095, 2101, 2107, 2112, 2118]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Day of the week**](https://rosettacode.org/wiki/Day_of_the_week) in Zen C.

*This article uses material from the Rosetta Code article **Day of the week**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Day_of_the_week?action=history).*
