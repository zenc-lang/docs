# std/process

The `std/process` module provides a high-level API for spawning child processes, executing system commands, and capturing their output.

## Overview

- **Builder Pattern**: The `Command` struct uses a fluid builder pattern for constructing command lines.
- **Output Capture**: Easily capture standard output and exit codes from finished processes.
- **RAII**: Both `Command` and `Output` implement the `Drop` trait for automatic cleanup of internal buffers.
- **Standard Interop**: Seamlessly wraps underlying system-level process manipulation.

## Usage

```zc
import "std/process.zc"

fn main() {
    // Basic command execution
    let output = Command::new("echo")
        .arg("hello world")
        .output();
        
    if (output.exit_code == 0) {
        println "Captured: {output.std_out}";
        // output.std_out is a String, freed automatically
    } else {
        println "Command failed with code {output.exit_code}";
    }
}
```

## Struct Definitions

### `Command`
A builder for configuring and spawning a process.
```zc
struct Command {
    program: String;
    args: Vec<String>;
}
```

### `Output`
The result of a completed process execution.
```zc
struct Output {
    std_out: String;
    exit_code: int;
}
```

## Methods

### `Command` Methods

| Method | Signature | Description |
| :--- | :--- | :--- |
| **new** | `Command::new(program: char*) -> Command` | Creates a new Command for the given program. |
| **arg** | `arg(self, arg: char*) -> Command*` | Adds an argument and returns a pointer to self for chaining. |
| **output** | `output(self) -> Output` | Executes the command and waits for completion, capturing stdout. |
| **status** | `status(self) -> int` | Executes the command and returns the exit status code. |

## Memory Management

| Method | Signature | Description |
| :--- | :--- | :--- |
| **free** | `free(self)` | Manually frees internal command buffers. |
| **Trait** | `impl Drop for Command` | Automatically cleans up command buffers. |
| **Trait** | `impl Drop for Output` | Automatically frees the captured output string. |
