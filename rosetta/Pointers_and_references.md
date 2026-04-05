+++
title = "Pointers and references"
+++

# Pointers and references

Zen C embraces explicit pointers for low-level memory manipulation, using the familiar <code>&</code> (address-of) and <code>*</code> (dereference) operators from standard C. 

However, it introduces several ergonomic improvements. For example, when accessing struct fields through a pointer, Zen C automatically dereferences the pointer, allowing developers to use the standard dot syntax (<code>d_ptr.active</code>) instead of requiring a separate arrow operator (<code>-&gt;</code>) like in C.

```zc
struct Data {
    id: int;
    active: bool;
}

fn increment(ptr: int*) {
    // Dereference to modify the value in the caller's scope
    *ptr = *ptr + 1;
}

fn main() {
    println "STACK POINTERS";
    let x = 42;
    let x_ptr = &x; // Take the address of a stack variable

    println "Value of x: {x}";
    println "Address of x: {(usize)x_ptr}";
    println "Value via x_ptr: {*x_ptr}";

    // Modifying via pointer
    *x_ptr = 100;
    println "New value of x: {x}";

    // Pass by reference
    increment(&x);
    println "Value after increment(ptr): {x}";

    println "\nSTRUCT POINTERS & AUTO-DEREF";
    let d = Data { id: 1, active: true };
    let d_ptr = &d;

    // Zen C supports auto-dereferencing for struct fields
    println "id via d_ptr.id: {d_ptr.id}";
    d_ptr.active = false;
    println "Active via d.active: {d.active}";

    // Manual dereferencing for clarity or specific cases
    println "id via (*d_ptr).id: {(*d_ptr).id}";

    println "\nHEAP POINTERS";
    // Allocate memory for an integer on the heap
    let h_ptr: int* = malloc(sizeof(int));
    
    if ((usize)h_ptr == 0) {
        println "Failed to allocate memory!";
        return 0;
    }

    *h_ptr = 500;
    println "Value on heap: {*h_ptr}";

    // Always free heap memory
    free(h_ptr);
    println "Heap memory freed.";

    println "\nNULL POINTERS";
    let null_ptr: int* = 0;
    if ((usize)null_ptr == 0) {
        println "null_ptr is indeed null (0).";
    }
}
```

**Output:**

```
STACK POINTERS
Value of x: 42
Address of x: 140734141454332
Value via x_ptr: 42
New value of x: 100
Value after increment(ptr): 101

STRUCT POINTERS & AUTO-DEREF
id via d_ptr.id: 1
Active via d.active: false
id via (*d_ptr).id: 1

HEAP POINTERS
Value on heap: 500
Heap memory freed.

NULL POINTERS
null_ptr is indeed null (0).
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Pointers and references**](https://rosettacode.org/wiki/Pointers_and_references) in Zen C.

*This article uses material from the Rosetta Code article **Pointers and references**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Pointers_and_references?action=history).*
