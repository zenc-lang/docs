+++
title = "Arrays"
weight = 4
+++

# Arrays

Fixed-size arrays with value semantics, zero-initialization, and
bounds-checked access.

## Zen C

```zc
import "std/io.zc"

def SIZE = 5;

fn main() {
    let arr1: int[SIZE];
    let arr2: int[SIZE] = [1, 2, 3, 4, 5];
    let matrix: int[2][3] = [[1, 2, 3], [4, 5, 6]];

    arr1[0] = 10;
    arr1[1] = 20;

    println "arr1[0]: {arr1[0]}, arr1[1]: {arr1[1]}";
    println "arr2 sum: {arr2[0] + arr2[1] + arr2[2] + arr2[3] + arr2[4]}";
    println "matrix[1][2]: {matrix[1][2]}";
}
```

## C

```c
#include <stdio.h>

#define SIZE 5

int main(void) {
    int arr1[SIZE] = {0};
    int arr2[SIZE] = {1, 2, 3, 4, 5};
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};

    arr1[0] = 10;
    arr1[1] = 20;

    printf("arr1[0]: %d, arr1[1]: %d\n", arr1[0], arr1[1]);
    printf("arr2 sum: %d\n",
        arr2[0] + arr2[1] + arr2[2] + arr2[3] + arr2[4]);
    printf("matrix[1][2]: %d\n", matrix[1][2]);
    return 0;
}
```

## Key Differences

- Zen C array syntax: `type[SIZE]` vs C's `type arr[SIZE]`
- `let arr: int[SIZE]` zero-initializes automatically
- C requires `= {0}` for zero-init
- Arrays in Zen C have value semantics (copied on assignment)
- Bounds checking is available in Zen C
- Multi-dimensional array syntax: `int[2][3]` vs C's `int arr[2][3]`

## Output

arr1[0]: 10, arr1[1]: 20
arr2 sum: 15
matrix[1][2]: 6
