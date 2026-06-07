+++
title = "Compound data type"
+++

# Compound data type

```zc
import "std/string.zc"
import "std/math.zc"

struct Point {
    x: int;
    y: int;
}

impl Point {
    // instance method
    fn to_string(self) -> String {
        let s = "({self.x}, {self.y})";
        return String::from(s);
    }

    // static method
    fn distance(p1: Point, p2: Point) -> f64 {
        let dx = p1.x - p2.x;
        let dy = p1.y - p2.y;
        return Math::sqrt((f64)(dx * dx + dy * dy));
    }
}

fn main() {
    let p1 = Point{x: 0, y: 0};
    let p2 = Point{x: 3, y: 4};
    println "Point 1 : {p1.to_string()}";
    println "Point 2 : {p2.to_string()}";
    let dist = Point::distance(p1, p2);
    println "Distance: {dist:g}";
}
```

**Output:**

```
Point 1 : (0, 0)
Point 2 : (3, 4)
Distance: 5
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Compound data type**](https://rosettacode.org/wiki/Compound_data_type) in Zen C.

*This article uses material from the Rosetta Code article **Compound data type**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Compound_data_type?action=history).*
