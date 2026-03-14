# std/time

The `std/time` module provides utilities for high-precision time measurement and thread suspension.

## Overview

- **Millisecond Precision**: `Time::now()` returns current system time in milliseconds.
- **Duration Type**: The `Duration` struct allows for intuitive time span calculations.
- **Simple Sleeping**: Easy-to-use functions for suspending execution.
- **Lightweight**: Minimal overhead, wrapping standard system-level time functions.

## Usage

```zc
import "std/time.zc"

fn main() {
    let start = Time::now();
    
    // Sleep for 1.5 seconds
    Time::sleep(Duration::from_ms(1500));
    
    let end = Time::now();
    println "Elapsed: {end - start} ms";
}
```

## Struct Definitions

### `Duration`
Represents a span of time.
```zc
struct Duration {
    millis: U64;
}
```

### `Time`
Static utility struct for system time operations.
```zc
struct Time {}
```

## Methods

### `Duration` Methods

| Method | Signature | Description |
| :--- | :--- | :--- |
| **from_ms** | `Duration::from_ms(ms: U64) -> Duration` | Creates a `Duration` from a count of milliseconds. |
| **from_secs** | `Duration::from_secs(s: U64) -> Duration` | Creates a `Duration` from a count of seconds. |

### `Time` Static Methods

| Method | Signature | Description |
| :--- | :--- | :--- |
| **now** | `Time::now() -> U64` | Returns current system time in milliseconds since the epoch. |
| **sleep** | `Time::sleep(d: Duration)` | Suspends the current thread for the specified `Duration`. |
| **sleep_ms** | `Time::sleep_ms(ms: U64)` | Suspends the current thread for the specified count of milliseconds. |
