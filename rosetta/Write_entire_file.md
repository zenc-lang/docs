+++
title = "Write entire file"
+++

# Write entire file

```zc
import "std/fs.zc"

fn main() {
    let filename = "output.txt";
    let content = "Hello, Zen C!";

    // Open the file in "write" mode (overwrites if it exists, creates if not)
    let res = File::open(filename, "wb");
    if res.is_err() {
        eprintln "Error opening file for writing: {res.err}";
        return 1;
    }

    let f = res.unwrap();
    let write_res = f.write_string(content);
    
    // Explicit error handling for the write operation
    if write_res.is_err() {
        eprintln "Error writing to file: {write_res.err}";
        f.close();
        return 1;
    }

    f.close();
    println "Successfully wrote to {filename}";
}
```

**Output:**

```
Successfully wrote to output.txt
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Write entire file**](https://rosettacode.org/wiki/Write_entire_file) in Zen C.

*This article uses material from the Rosetta Code article **Write entire file**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Write_entire_file?action=history).*
