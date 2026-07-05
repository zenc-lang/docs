+++
title = "Sorting algorithms/Cycle sort"
+++

# Sorting algorithms/Cycle sort

A translation of the Python code in the Wikipedia article. 

```zc
fn cycle_sort(a: int*, len: const usize) -> int {
    let writes = 0;
    for cs in 0..(len - 1) {
        let item = a[cs];
        let pos = cs;
        for i in (cs + 1)..len {
            if a[i] < item { pos++; }
        }
        if pos != cs {
            while item == a[pos] { pos++; }
            let t = a[pos];
            a[pos] = item;
            item = t;
            while pos != cs {
                pos = cs;
                for i in (cs + 1)..len {
                    if a[i] < item { pos++; }
                }
                while item == a[pos] { pos++; }
                let u = a[pos];
                a[pos] = item;
                item = u;
                writes++;
            }
        }
    }
    return writes;
}

fn main() {
    let a1 = [4, 65, 2, -31, 0, 99, 2, 83, 782, 1];
    let a2 = [7, 5, 2, 6, 1, 4, 2, 6, 3];
    let aa: int*[2] = [a1, a2];
    let lens = [a1.len, a2.len];
    for i in 0..aa.len {
        print "Before: [";
        for j in 0..lens[i] { print "{aa[i][j]}, "; }
        println "\b\b]";
        let w = cycle_sort(aa[i], lens[i]);
        print "After : [";
        for j in 0..lens[i] { print "{aa[i][j]}, "; }
        println "\b\b] ";
        println "Writes : {w}\n";
    }
}
```

**Output:**

```
Before: [4, 65, 2, -31, 0, 99, 2, 83, 782, 1] 
After : [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782] 
Writes : 7

Before: [7, 5, 2, 6, 1, 4, 2, 6, 3] 
After : [1, 2, 2, 3, 4, 5, 6, 6, 7] 
Writes : 6
```

## {{Header|Zig}}

```zc
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    const io: std.Io = init.io;
    var stdouter_buf: [512]u8 = undefined;
    var stdouter = std.Io.File.stdout().writer(io, &stdouter_buf);

    var array = [_]i32{ 1, 4, 65, 2, -31, 0, 99, 2, 83, 782, 1 };
    for (0..array.len) |i| try stdouter.interface.print("{d},", .{array[i]});
    try stdouter.interface.print("\n", .{});
    cyclesort(&array);
    for (0..array.len) |i| try stdouter.interface.print("{d},", .{array[i]});
    try stdouter.flush();
}

fn cyclesort(arr: []i32) void {
    for (0..arr.len - 1) |start| {
        var j: i32 = arr[start];
        var first: bool = true;
        while (true) {
            var count: usize = start;
            var tmp: i32 = undefined;
            for (start + 1..arr.len) |k| {
                count += if (j > arr[k]) 1 else 0;
            }
            if (first and count == start) break;
            while (j == arr[count] and count + 1 < arr.len) count += 1;
            tmp = arr[count];
            arr[count] = j;
            j = tmp;
            if (count == start) break;
            first = false;
        }
    }
}
```

**Output:**

```
1,4,65,2,-31,0,99,2,83,782,1,
-31,0,1,1,2,2,4,65,83,99,782,
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Sorting algorithms/Cycle sort**](https://rosettacode.org/wiki/Sorting_algorithms/Cycle_sort) in Zen C.

*This article uses material from the Rosetta Code article **Sorting algorithms/Cycle sort**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Sorting_algorithms/Cycle_sort?action=history).*
