+++
title = "5. Control Flow"
weight = 5
+++

# 5. Control Flow {#5-control-flow}


#### Conditionals
```zc
if x > 10 {
    print "Large";
} else if x > 5 {
    print "Medium";
} else {
    print "Small";
}

// Ternary
let y = x > 10 ? 1 : 0;

// If-Expression (for complex conditions)
let category = if (x > 100) { "huge" } else if (x > 10) { "large" } else { "small" };
```

#### Pattern Matching
Powerful alternative to `switch`.
```zc
match val {
    1         => { print "One" },
    2 || 3    => { print "Two or Three" },    // OR with ||
    4 or 5    => { print "Four or Five" },    // OR with 'or'
    6, 7, 8   => { print "Six to Eight" },    // OR with comma
    10 .. 15  => { print "10 to 14" },        // Exclusive range (Legacy)
    10 ..< 15 => { print "10 to 14" },        // Exclusive range (Explicit)
    20 ..= 25 => { print "20 to 25" },        // Inclusive range
    _         => { print "Other" },
}

// Destructuring Enums
match shape {
    Shape::Circle(r)   => { println "Radius: {r}" },
    Shape::Rect(w, h)  => { println "Area: {w*h}" },
    Shape::Point       => { println "Point" },
}
```

#### Reference Binding
To inspect a value without taking ownership (moving it), use the `ref` keyword in the pattern. This is essential for types that implement Move Semantics (like `Option`, `Result`, non-Copy structs).

```zc
let opt = Some(NonCopyVal{...});
match opt {
    Some(ref x) => {
        // 'x' is a pointer to the value inside 'opt'
        // 'opt' is NOT moved/consumed here
        println "{x.field}"; 
    },
    None => {}
}
```

#### Loops
```zc
// Range
for i in 0..10 { ... }      // Exclusive (0 to 9)
for i in 0..<10 { ... }     // Exclusive (Explicit)
for i in 0..=10 { ... }     // Inclusive (0 to 10)
for i in 0..10 step 2 { ... }
for i in 10..0 step -1 { ... }  // Descending loop

// Iterator (Vec or custom Iterable)
for item in vec { ... }

// Enumerated: get index and value
for i, val in arr { ... }       // i = 0, 1, 2, ...
for i, val in 0..10 step 2 { ... } // i = 0, 1, 2, ...; val = 0, 2, 4, ...

// Iterate over fixed-size arrays directly
let arr: int[5] = [1, 2, 3, 4, 5];
for val in arr {
    // val is int
    println "{val}";
}

// While
while x < 10 { ... }

// Do-While
do { ... } while x < 10;

// Infinite with label
outer: loop {
    if done { break outer; }
}

// Repeat N times
for _ in 0..5 { ... }
```

#### Advanced Control
```zc
// Guard: Execute else and return if condition is false
guard ptr != NULL else { return; }

// Unless: If not true
unless is_valid { return; }
```
