+++
title = "1. Variables and Constants"
weight = 1
+++

# 1. Variables and Constants {#1-variables-and-constants}


Zen C distinguishes between compile-time constants and runtime variables.

#### Manifest Constants (`def`)
Values that exist only at compile-time (folded into code). Use these for array sizes, fixed configuration, and magic numbers.

```zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // Valid array size
```

#### Variables (`let`)
Storage locations in memory. Can be mutable or read-only (`const`).

```zc
let x = 10;             // Mutable
x = 20;                 // OK

let y: const int = 10;  // Read-only (Type qualified)
// y = 20;              // Error: cannot assign to const
```

{% alert(type="tip") %}
**Type Inference**: Zen C automatically infers types for initialized variables. It compiles to C23 `auto` on supported compilers, or GCC's `__auto_type` extension otherwise.
{% end %}
