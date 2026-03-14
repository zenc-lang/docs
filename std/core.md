# std/core

The `std/core` module provides the most fundamental definitions and error handling primitives for Zen-C programs. It is implicitly required by most other standard libraries.

## Overview

- **Standard Headers**: Includes critical C headers like `stdlib.h`, `stdio.h`, and `stdbool.h`.
- **Panic Mechanism**: Provides the `panic` macro for unrecoverable error reporting.
- **Process Control**: Includes basic process control functions like `exit`.

## Methods

### Error Handling

| Method/Macro | Signature | Description |
| :--- | :--- | :--- |
| **panic** | `panic(msg: char*)` | Prints a formatted error message including file, line, and function, then terminates the process. |

### Process Control

| Method | Signature | Description |
| :--- | :--- | :--- |
| **exit** | `exit(code: int)` | Immediately terminates the process with the given return code. |
