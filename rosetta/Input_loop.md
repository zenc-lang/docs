+++
title = "Input loop"
+++

# Input loop

```zc
import "std/io.zc"
import "std/string.zc"

fn main(argc: int, argv: char**) {
    // Check if the user passed the line-by-line flag
    let line_mode = argc > 1 && strcmp(argv[1], "-l") == 0;
    
    while true {
        // readln() dynamically allocates and returns NULL on EOF
        let line = readln();
        if line == NULL break;
        
        // Ensure the line buffer is freed at the end of the current scope
        defer free(line);
        
        if line_mode {
            println "Line: [{line}]";
        } else {
            let s = String::from(line);
            let words = s.split(' ');
            
            for word in words {
                if !word.is_empty() {
                    let w = word.c_str();
                    println "Word: [{w}]";
                }
            }
        }
    }
}
```

**Output:**

**Word-by-word processing (Default):**

```
$ echo "hello world from Zen C" | ./read_stream
Word: [hello]
Word: [world]
Word: [from]
Word: [Zen]
Word: [C]
```

**Line-by-line processing (with -l flag):**

```
$ printf "First line\nSecond line\n" | ./read_stream -l
Line: [First line]
Line: [Second line]
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Input loop**](https://rosettacode.org/wiki/Input_loop) in Zen C.

*This article uses material from the Rosetta Code article **Input loop**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Input_loop?action=history).*
