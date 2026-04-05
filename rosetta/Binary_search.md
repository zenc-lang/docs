+++
title = "Binary search"
+++

# Binary search

### Iterative

```zc
fn binary_search_iterative(arr: int*, value: int, low: int, high: int) -> int {
    let l = low;
    let h = high;
    
    while l <= h {
        let mid = l + (h - l) / 2;
        
        if arr[mid] > value {
            h = mid - 1;
        } else if arr[mid] < value {
            l = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
}

fn main() {
    let arr: int[10] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
    let n = 10;
    let targets: int[3] = [12, 5, 20];
    
    println "=> Iterative Binary Search";
    for target in targets {
        let index = binary_search_iterative(arr, target, 0, n - 1);
        if index != -1 {
            println "Value {target} found at index {index}.";
        } else {
            println "Value {target} not found.";
        }
    }
}
```

**Output:**

```
=> Iterative Binary Search
Value 12 found at index 5.
Value 5 not found.
Value 20 found at index 9.
```

### Recursive

```zc
fn binary_search_recursive(arr: int*, value: int, low: int, high: int) -> int {
    if high < low {
        return -1;
    }

    let mid = low + (high - low) / 2;
    
    if arr[mid] > value {
        return binary_search_recursive(arr, value, low, mid - 1);
    } else if arr[mid] < value {
        return binary_search_recursive(arr, value, mid + 1, high);
    } else {
        return mid;
    }
}

fn main() {
    let arr: int[10] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
    let n = 10;
    let targets: int[3] = [12, 5, 20];
    
    println "=> Recursive Binary Search";
    for target in targets {
        let index = binary_search_recursive(arr, target, 0, n - 1);
        if index != -1 {
            println "Value {target} found at index {index}.";
        } else {
            println "Value {target} not found.";
        }
    }
}
```

**Output:**

```
=> Recursive Binary Search
Value 12 found at index 5.
Value 5 not found.
Value 20 found at index 9.
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Binary search**](https://rosettacode.org/wiki/Binary_search) in Zen C.

*This article uses material from the Rosetta Code article **Binary search**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Binary_search?action=history).*
