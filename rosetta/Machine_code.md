+++
title = "Machine code"
+++

# Machine code

This implementation targets the x86_64 architecture using the System V AMD64 ABI (where the first two arguments are passed in the `edi` and `esi` registers, and the return value is placed in `eax`). 

To comply with modern OS security features like Data Execution Prevention (DEP / W^X), this solution uses Zen C's memory management library to securely map a memory page as Read/Write, inject the opcodes, flip the page protection to Read/Execute, execute the function pointer, and finally unmap the memory.

**Assembly equivalent:**

```
89 F8    mov eax, edi
01 F0    add eax, esi
C3       ret
```

**Zen C Implementation:**

```zc
import "std/sys/mman.zc"
import "std/io.zc"

fn main() {
    let opcodes: byte[5];
    opcodes[0] = 0x89; // mov eax, edi
    opcodes[1] = 0xF8;
    opcodes[2] = 0x01; // add eax, esi
    opcodes[3] = 0xF0;
    opcodes[4] = 0xC3; // ret

    let size: usize = 4096; // Standard page size

    // Map memory as Read / Write
    let addr = Memory::mmap(size, Z_PROT_READ | Z_PROT_WRITE, Z_MAP_PRIVATE | Z_MAP_ANONYMOUS);
    
    if (isize)addr == Z_MAP_FAILED {
        eprintln "Failed to mmap memory";
        exit(1);
    }

    // Poke the opcodes into the allocated memory
    let ptr = (byte*)addr;
    for i in 0..5 {
        ptr[i] = opcodes[i];
    }

    // Change memory protection to Read / Execute (Preventing W^X violations)
    if !Memory::mprotect(addr, size, Z_PROT_READ | Z_PROT_EXEC) {
        eprintln "Failed to mprotect memory";
        Memory::munmap(addr, size);
        exit(1);
    }

    // Cast the executable memory address to a Zen C raw function pointer
    let add_func: fn* (int, int) -> int = (void*)addr;
    
    // Execute the machine code
    let a = 7;
    let b = 12;
    let result = add_func(a, b);

    println "Executing machine code (x86_64: mov eax, edi; add eax, esi; ret)";
    println "Arguments: {a}, {b}";
    println "Result: {result}";

    // Clean up
    Memory::munmap(addr, size);
    
    if result == 19 {
        println "Success!";
    } else {
        eprintln "Failure: expected 19, got {result}";
        exit(1);
    }
}
```

**Output:**

```
Executing machine code (x86_64: mov eax, edi; add eax, esi; ret)
Arguments: 7, 12
Result: 19
Success!
```

{{omit from|360 Assembly}}
{{omit from|8080 Assembly}}
{{omit from|8086 Assembly}}
{{omit from|AArch64 Assembly}}
{{omit from|ARM Assembly}}
{{omit from|Mathematica}}
{{omit from|MIPS Assembly}}
{{omit from|x86 Assembly}}

---
**Attribution:** This is a community solution for the Rosetta Code task [**Machine code**](https://rosettacode.org/wiki/Machine_code) in Zen C.

*This article uses material from the Rosetta Code article **Machine code**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Machine_code?action=history).*
