+++
title = "Variables"
+++

# Variables

Zen C distinguishes between compile-time manifest constants and runtime variables. It features automatic type inference for initialized variables, standard C-style block scoping, and explicit pointers for referencing. It also provides advanced variable facilities like tuple destructuring and <code>autofree</code> scope-bound memory management.

```zc
// Other variable related facilities: Manifest Constants (compile-time only)
def GLOBAL_LIMIT = 1024;

fn main() {
    /* Declaration & Initialization (Type inferred automatically) */
    let a = 10;
    
    /* Assignment */
    a = 20;
    
    /* Datatypes (Explicit type annotations) */
    let my_int: int = 42;               // Standard 32-bit integer
    let my_float: f32 = 3.14;           // Floating point
    let my_bool: bool = true;           // Boolean
    let my_string: string = "Rosetta";  // Null-terminated C-string
    let my_u8: u8 = 255;                // Fixed-width unsigned 8-bit integer
    let my_c_long: c_long = 10000;      // C interop type (size varies by platform)
    
    // Read-only variables use the `const` type qualifier
    let max_retries: const int = 3;
    // max_retries = 5; // This would cause a compiler error
    
    /* Scope */
    {
        // Block scope: shadows the outer variable 'a'
        let a = 50;
        println "Inner scope 'a': {a}";
        
        // Other facilities: `autofree` automatically frees resources when scope exits
        // autofree let buffer = malloc(GLOBAL_LIMIT);
    }
    println "Outer scope 'a' remains: {a}";
    
    /* Referencing */
    // Zen C uses explicit pointers for referencing
    let ref_a: int* = &a; 
    *ref_a = 30; // Dereferencing to mutate the original variable
    println "Mutated 'a' via reference: {a}";
    
    /* Other facilities: Tuples and Destructuring */
    // Variables can be grouped and destructured in a single line
    let pair = (1, "Apple");
    let (id, name) = pair;
    
    println "Destructured Tuple - ID: {id}, Name: {name}";
}
```

**Output:**

```
Inner scope 'a': 50
Outer scope 'a' remains: 20
Mutated 'a' via reference: 30
Destructured Tuple - ID: 1, Name: Apple
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Variables**](https://rosettacode.org/wiki/Variables) in Zen C.

*This article uses material from the Rosetta Code article **Variables**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Variables?action=history).*
