+++
title = "15. Diagnostic System"
weight = 15
+++

# 15. Diagnostic System


Zen C features a categorized diagnostic system that provides granular control over compiler warnings. This allows you to maintain high code quality standards while reducing friction when interacting with external C code.

## Diagnostic Categories

Warnings are grouped into logical categories. Each category can be enabled or disabled globally using compiler flags.

| Category | Description | Default |
| :--- | :--- | :--- |
| **`INTEROP`** | Warnings related to C header imports and undefined external functions. | **OFF** |
| **`PEDANTIC`** | Extra strict checks for potential issues or code quality. | **OFF** |
| **`UNUSED`** | Warnings for defined but unused variables, parameters, or functions. | **ON** |
| **`SAFETY`** | Critical safety warnings such as null pointer access or division by zero. | **ON** |
| **`LOGIC`** | Logic-related warnings like unreachable code or constant comparisons. | **ON** |
| **`CONVERSION`** | Warnings for implicit or narrowing type conversions. | **ON** |
| **`STYLE`** | Coding style warnings such as variable shadowing. | **ON** |

## Compiler Flags

You can control diagnostics using the `-W` (enable) and `-Wno-` (disable) flags followed by a category name or specific diagnostic ID.

### Category Flags

- `-Winterop`: Enable all interop-related warnings.
- `-Wno-unused`: Specifically silence unused variable/parameter warnings.
- `-Wsafety`: Ensure all safety checks are active.
- `-Wall`: Enable all major diagnostic categories.
- `-Wextra`: Enable even more strict diagnostics (equivalant to `-Wpedantic`).

### Example Usage

```bash
# Compile with C interop warnings enabled
zc app.zc -Winterop

# Compile with all warnings enabled but no unused warnings
zc app.zc -Wall -Wno-unused
```

## C Interoperability Friction

By default, Zen C suppresses "Undefined function" warnings for functions that are likely to be found in C standard libraries (the `INTEROP` category is **OFF**). 

If you want the compiler to strictly report every undefined function (e.g., to catch typos), enable the interop category:

```bash
zc main.zc -Winterop
```

When enabled, the compiler will provide helpful hints for common C functions:
```text
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

## Whitelisting

If you use a specific C library frequently and want to keep `-Winterop` enabled without being bothered by specific functions, you can add them to the `c_function_whitelist` in your `zenc.json` configuration file.
