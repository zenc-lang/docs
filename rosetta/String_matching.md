+++
title = "String matching"
+++

# String matching

```zc
import "std/string.zc"

fn main() {
    let text = String::from("The quick brown fox jumps over the lazy dog. The fox is quick.");
    let target = "fox";

    println "Text: {text}";
    println "Target: {target}";

    // Starts with
    if (text.starts_with("The quick")) {
        println "The text starts with 'The quick'.";
    }

    // Contains (and Optional Requirements)
    if (text.contains_str(target)) {
        println "The text contains '{target}'.";
        
        // Optional: Print the location of the match
        let first_match = text.find_str(target);
        if (first_match.is_some()) {
            println "First match at index: {first_match.unwrap()}";
        }

        // Optional: Handle multiple occurrences
        let all_matches = text.find_all_str(target);
        print "All match indices: ";
        for idx in all_matches {
            print "{idx} ";
        }
        println "";
    }

    // Ends with
    if (text.ends_with("quick.")) {
        println "The text ends with 'quick.'.";
    }
}
```

**Output:**

```
Text: The quick brown fox jumps over the lazy dog. The fox is quick.
Target: fox
The text starts with 'The quick'.
The text contains 'fox'.
First match at index: 16
All match indices: 16 49 
The text ends with 'quick.'.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**String matching**](https://rosettacode.org/wiki/String_matching) in Zen C.

*This article uses material from the Rosetta Code article **String matching**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/String_matching?action=history).*
