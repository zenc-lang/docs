+++
title = "Classes"
+++

# Classes

Zen C does not use a <code>class</code> keyword. Instead, it uses <code>struct</code> for data definitions and <code>impl</code> blocks to define methods. The <code>self</code> parameter is implicitly passed by reference, allowing for state mutation without explicit pointer syntax. It also supports a convenient <code>.field</code> shorthand inside methods as an alternative to <code>self.field</code>.

```zc
struct Point {
    x: int;
    y: int;
}

impl Point {
    // Constructor convention (static method returning Self)
    fn new(x: int, y: int) -> Self {
        return Point{x: x, y: y};
    }

    // Instance method
    fn print_coords(self) {
        // Using the .field shorthand for self.x and self.y
        println "Point coordinates: ({.x}, {.y})";
    }
    
    // Method that mutates state using 'self' directly
    fn move_by(self, dx: int, dy: int) {
        self.x += dx;
        self.y += dy;
    }
}

fn main() {
    // Instantiate using the constructor
    let p = Point::new(10, 20);
    p.print_coords();
    
    // Mutate state directly
    p.move_by(5, -5);
    
    print "After moving: ";
    p.print_coords();
}
```

**Output:**

```
Point coordinates: (10, 20)
After moving: Point coordinates: (15, 15)
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Classes**](https://rosettacode.org/wiki/Classes) in Zen C.

*This article uses material from the Rosetta Code article **Classes**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Classes?action=history).*
