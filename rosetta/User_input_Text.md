+++
title = "User input/Text"
+++

# User input/Text

Zen C features a built-in shorthand for prompting user input using the <code>?</code> prefix. Format specifiers are automatically inferred based on the variable's type. For the string, we define a fixed-size character array buffer to hold the input safely.

```zc
fn main() {
    let str_val: char[256];
    let int_val: int;
    
    // Prompt for the string (infers %s for the char array)
    ? "Enter a string: " (str_val);
    
    // Prompt for the integer (infers %d for the int)
    ? "Enter the integer 75000: " (int_val);
    
    println "\nYou entered the string: {str_val}";
    println "You entered the integer: {int_val}";
}
```

**Output:**

```
Enter a string: RosettaCode
Enter the integer 75000: 75000

You entered the string: RosettaCode
You entered the integer: 75000
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**User input/Text**](https://rosettacode.org/wiki/User_input/Text) in Zen C.

*This article uses material from the Rosetta Code article **User input/Text**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/User_input/Text?action=history).*
