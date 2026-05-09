+++
title = "16. MISRA Rules"
weight = 16
+++

# 16. MISRA Rules

Zen C includes a **MISRA C:2012 compliance mode** activated with the `--misra` flag.
In addition to standard MISRA checks, the compiler enforces several **Zen-specific rules**
that promote safer, more maintainable code.

## Enabling MISRA mode

```bash
zc build app.zc --misra
```

## Zen-Specific Rules

These rules are unique to Zen C and go beyond the standard MISRA C:2012 guidelines.

### Zen 1.1 — No raw blocks

Forbids `raw { }` blocks that bypass the transpiler.

```zc
// Violation:
fn main() {
    raw { int x = 10; }  // Zen 1.1
}
```

Fix: use Zen C constructs instead.

### Zen 1.2 — No plugin blocks

Forbids `plugin ... end` blocks that execute build-time code.

### Zen 1.3 — Exhaustive enum match

Requires all variants to be handled explicitly in `match` on enum types. The `_` wildcard
is forbidden for enums.

```zc
enum Color { Red; Green; Blue; }

fn describe(c: Color) {
    match c {
        Color::Red => { ... }
        Color::Green => { ... }
        // Missing Blue — Zen 1.3 violation
    }
}
```

### Zen 1.4 — No preprocessor directives

Forbids C preprocessor directives (`#define`, `#include`, `#if`, etc.).
Use Zen's `import` and `def` instead.

### Zen 1.5 — No `var` / `const` for declarations

Forbids the deprecated `var` and `const` keywords for variable/constant declarations.
Use `let` for variables and `def` for constants.

### Zen 1.8 — No identifier shadowing

Forbids declaring an identifier that shadows one from an outer scope.

### Zen 2.1 — No reserved identifiers

Forbids identifiers starting with `__`, `_[A-Z]`, or `_z_`, as these
are reserved for the compiler and C implementation.

### Zen 2.2 — Tuple size limit

Tuples with **3 or more fields** shall not be used as function return types or parameters.
Use a named struct instead.

```zc
// Violation:
fn stats() -> (int, int, int) { ... }  // Zen 2.2

// OK:
fn pair() -> (int, int) { ... }        // 2-tuples exempt
```

### Zen 2.3 — String comparison

`string == string` shall not be used. Use `strcmp()` instead.

```zc
// Violation:
if a == b { ... }  // Zen 2.3 (when a, b are string)

// OK:
if strcmp(a, b) == 0 { ... }
```

## Standard MISRA C:2012 Coverage

The compiler checks a broad set of standard MISRA C:2012 rules. These include:

| Chapter | Area | Rules |
|---------|------|-------|
| Dir 4 | Development process | 3 directives |
| 1 | Environment | 2 rules |
| 2 | Unused code | 7 rules |
| 5 | Identifiers | 9 rules |
| 6 | Types | 2 rules |
| 7 | Literals | 4 rules |
| 8 | Declarations | 14 rules |
| 9 | Initialization | 5 rules |
| 10 | Essential type model | 8 rules |
| 11 | Pointer conversions | 9 rules |
| 12 | Expressions | 4 rules |
| 13 | Side effects | 6 rules |
| 14 | Control flow | 4 rules |
| 15 | If/switch statements | 7 rules |
| 16 | Match/switch | 7 rules |
| 17 | Functions | 8 rules |
| 18 | Pointers/arrays | 8 rules |
| 19 | Overlapping storage | 2 rules |
| 20 | Preprocessor | 14 rules |
| 21 | Standard libraries | 13 rules |
| 22 | Resources | 6 rules |

For the complete rule text, refer to the official
[MISRA C:2012](https://www.misra.org.uk/) documentation.
