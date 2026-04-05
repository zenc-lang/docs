+++
title = "String comparison"
+++

# String comparison

```zc
import "std/string.zc"

fn main() {
    let s1 = String::from("apple");
    let s2 = String::from("banana");
    let s3 = String::from("apple");
    let s4 = String::from("APPLE");

    println "BASIC EQUALITY & INEQUALITY.";
    // Zen C supports operator overloading (==, !=) mapping to eq() and neq()
    println "s1 ('{s1}') == s3 ('{s3}'): {s1 == &s3}"; 
    println "s1 ('{s1}') != s2 ('{s2}'): {s1 != &s2}";

    println "\nLEXICAL ORDERING (CASE-SENSITIVE).";
    // Operators <, >, <=, >= map to lt(), gt(), le(), ge()
    println "s1 < s2  ('apple' < 'banana'): {s1 < &s2}";
    println "s2 > s1  ('banana' > 'apple'): {s2 > &s1}";
    println "s1 >= s3 ('apple' >= 'apple'): {s1 >= &s3}";

    println "\nCASE-SENSITIVITY.";
    println "s1 == s4 ('apple' == 'APPLE'): {s1 == &s4} (Case-sensitive)";
    println "s1.eq_ignore_case(s4): {s1.eq_ignore_case(&s4)} (Case-insensitive)";

    println "\nNUMERIC STRING COMPARISON (LEXICAL).";
    let n1 = String::from("10");
    let n2 = String::from("2");
    // '1' comes before '2', so "10" < "2"
    println "n1 < n2 ('10' < '2'): {n1 < &n2}"; 
    
    println "\nTYPE SYSTEM REFLECTION";
    let i1 = 10;
    let i2 = 2;
    println "Integer comparison: i1 < i2 (10 < 2): {i1 < i2}"; // false (numerical)
    
    // Zen C doesn't implicitly coerce/allomorphically convert strings to numbers
    // during comparison. If you want numerical comparison for strings, 
    // you must explicitly convert them.
    
    println "\nCOMPARISON METHOD (RESULT-BASED)";
    let cmp_res = s1.compare(&s2);
    if cmp_res < 0 {
        println "'{s1}' comes before '{s2}'";
    } else if cmp_res > 0 {
        println "'{s1}' comes after '{s2}'";
    } else {
        println "Strings are equal";
    }
}
```

**Output:**

```
BASIC EQUALITY & INEQUALITY.
s1 ('apple') == s3 ('apple'): true
s1 ('apple') != s2 ('banana'): true

LEXICAL ORDERING (CASE-SENSITIVE).
s1 < s2  ('apple' < 'banana'): true
s2 > s1  ('banana' > 'apple'): true
s1 >= s3 ('apple' >= 'apple'): true

CASE-SENSITIVITY.
s1 == s4 ('apple' == 'APPLE'): false (Case-sensitive)
s1.eq_ignore_case(s4): true (Case-insensitive)

NUMERIC STRING COMPARISON (LEXICAL).
n1 < n2 ('10' < '2'): true

TYPE SYSTEM REFLECTION
Integer comparison: i1 < i2 (10 < 2): 0

COMPARISON METHOD (RESULT-BASED)
'apple' comes before 'banana'
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**String comparison**](https://rosettacode.org/wiki/String_comparison) in Zen C.

*This article uses material from the Rosetta Code article **String comparison**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/String_comparison?action=history).*
