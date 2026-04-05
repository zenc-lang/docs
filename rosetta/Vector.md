+++
title = "Vector"
+++

# Vector

```zc
import "std/core.zc"
import "std/math.zc"

struct Vector {
    x: double;
    y: double;
}

impl Vector {
    // Standard initialization
    fn new(x: double, y: double) -> Vector {
        return Vector { x: x, y: y };
    }

    // Initialize from start and end points
    fn from_points(x1: double, y1: double, x2: double, y2: double) -> Vector {
        return Vector { x: x2 - x1, y: y2 - y1 };
    }

    // Initialize from angle and length
    fn from_polar(angle: double, length: double) -> Vector {
        return Vector {
            x: length * Math::cos(angle),
            y: length * Math::sin(angle)
        };
    }

    // Maps to the '+' operator
    fn add(self, other: Vector) -> Vector {
        return Vector { x: self.x + other.x, y: self.y + other.y };
    }

    // Maps to the '-' operator
    fn sub(self, other: Vector) -> Vector {
        return Vector { x: self.x - other.x, y: self.y - other.y };
    }

    // Maps to the '*' operator
    fn mul(self, scalar: double) -> Vector {
        return Vector { x: self.x * scalar, y: self.y * scalar };
    }

    // Maps to the '/' operator
    fn div(self, scalar: double) -> Vector {
        if (scalar == 0.0) {
            println "Warning: Division by zero vector scalar!";
            return *self;
        }
        return Vector { x: self.x / scalar, y: self.y / scalar };
    }

    // Implicitly called during string interpolation
    fn to_string(self) -> char* {
        let buf = (char*)malloc(64);
        sprintf(buf, "Vector(x: %.2f, y: %.2f)", self.x, self.y);
        return buf;
    }

    fn show(self) {
        let s = self.to_string();
        println "{s}";
        free(s);
    }
}

fn main() {
    // Initialization
    let v1 = Vector::new(3.0, 4.0);
    println "v1 (new): {v1}";

    let v2 = Vector::from_points(0.0, 0.0, -1.0, 2.0);
    println "v2 (from_points): {v2}";

    println "v_polar (from_polar): {Vector::from_polar(Math::PI() / 4.0, 5.0)}";

    println "";

    // Operations
    println "v1 + v2: {v1 + v2}";
    println "v1 - v2: {v1 - v2}";
    println "v1 * 2.5: {v1 * 2.5}";
    println "v1 / 2.0: {v1 / 2.0}";
}
```

**Output:**

```
v1 (new): Vector(x: 3.00, y: 4.00)
v2 (from_points): Vector(x: -1.00, y: 2.00)
v_polar (from_polar): Vector(x: 3.54, y: 3.54)

v1 + v2: Vector(x: 2.00, y: 6.00)
v1 - v2: Vector(x: 4.00, y: 2.00)
v1 * 2.5: Vector(x: 7.50, y: 10.00)
v1 / 2.0: Vector(x: 1.50, y: 2.00)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Vector**](https://rosettacode.org/wiki/Vector) in Zen C.

*This article uses material from the Rosetta Code article **Vector**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Vector?action=history).*
