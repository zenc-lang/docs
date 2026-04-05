+++
title = "Create a file"
+++

# Create a file

This implementation utilizes Zen C's standard filesystem library (<code>std/fs.zc</code>) to handle file and directory creation. It demonstrates Zen C's <code>Result</code> type for error handling, gracefully catching the expected permission errors when attempting to write to the filesystem root (this example assumes UNIX hierarchical, tree-like structure).

```zc
import "std/fs.zc"

fn try_create_file(path: char*) {
    println "Creating file: {path}";
    let res = File::open(path, "w");
    if res.is_ok() {
        println "Success: {path} created.";
        res.unwrap().close();
    } else {
        println "Error: {res.err}";
    }
}

fn try_create_dir(path: char*) {
    println "Creating directory: {path}";
    let res = File::create_dir(path);
    if res.is_ok() {
        println "Success: {path} created.";
    } else {
        println "Error: {res.err}";
    }
}

fn main() {
    // Current directory
    try_create_file("output.txt");
    try_create_dir("docs");

    // Filesystem root
    try_create_file("/output.txt");
    try_create_dir("/docs");
}
```

**Output:**

```
Creating file: output.txt
Success: output.txt created.
Creating directory: docs
Error: Failed to create directory
Creating file: /output.txt
Error: Failed to open file
Creating directory: /docs
Error: Failed to create directory
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Create a file**](https://rosettacode.org/wiki/Create_a_file) in Zen C.

*This article uses material from the Rosetta Code article **Create a file**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Create_a_file?action=history).*
