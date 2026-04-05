+++
title = "Vector products"
+++

# Vector products

```zc
struct Vector3 {
    x: double;
    y: double;
    z: double;
}

impl Vector3 {
    fn new(x: double, y: double, z: double) -> Vector3 {
        return Vector3 { x: x, y: y, z: z };
    }

    fn dot(self, other: Vector3) -> double {
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z);
    }

    fn cross(self, other: Vector3) -> Vector3 {
        return Vector3 {
            x: (self.y * other.z) - (self.z * other.y),
            y: (self.z * other.x) - (self.x * other.z),
            z: (self.x * other.y) - (self.y * other.x)
        };
    }

    // Scalar triple product: a • (b x c)
    fn scalar_triple(self, b: Vector3, c: Vector3) -> double {
        return self.dot(b.cross(c));
    }

    // Vector triple product: a x (b x c)
    fn vector_triple(self, b: Vector3, c: Vector3) -> Vector3 {
        return self.cross(b.cross(c));
    }

    // Implicitly called during string interpolation
    fn to_string(self) -> char* {
        let buf = (char*)malloc(128);
        sprintf(buf, "(%.1f, %.1f, %.1f)", self.x, self.y, self.z);
        return buf;
    }
}

fn main() {
    let a = Vector3::new(3.0, 4.0, 5.0);
    let b = Vector3::new(4.0, 3.0, 5.0);
    let c = Vector3::new(-5.0, -12.0, -13.0);

    println "Vectors:";
    println "a = {a}";
    println "b = {b}";
    println "c = {c}";
    println "";

    println "a . b       = {a.dot(b)}";
    println "a x b       = {a.cross(b)}";
    println "a . (b x c) = {a.scalar_triple(b, c)}";
    println "a x (b x c) = {a.vector_triple(b, c)}";
}
```

**Output:**

```
Vectors:
a = (3.0, 4.0, 5.0)
b = (4.0, 3.0, 5.0)
c = (-5.0, -12.0, -13.0)

a . b       = 49.000000
a x b       = (5.0, 5.0, -7.0)
a . (b x c) = 6.000000
a x (b x c) = (-267.0, 204.0, -3.0)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Vector products**](https://rosettacode.org/wiki/Vector_products) in Zen C.

*This article uses material from the Rosetta Code article **Vector products**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Vector_products?action=history).*
