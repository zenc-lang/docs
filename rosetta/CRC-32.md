+++
title = "CRC-32"
+++

# CRC-32

A translation of the C code in the Wikipedia article.

```zc
let crc_table: [u32; 256];

fn crc32_init() {
    let crc: u32 = 1;
    for let i: u32 = 128; i; i >>= 1 {
        crc = (crc >> 1) ^ (crc & 1 ? 0xedb88320 : 0);
        for let j: u32 = 0; j < 256; j += 2 * i {
            crc_table[i + j] = crc ^ crc_table[j];
        }
    }
}
                
fn crc32(data: string) -> u32 {
    let data_length = strlen(data);
    let crc: u32 = 0xffffffff;
    if crc_table[255] == 0 { crc32_init(); }
    for let i: usize = 0; i < data_length; ++i {
        crc ^= data[i];
        crc = (crc >> 8) ^ crc_table[crc & 0xff];
    }
    crc ^= 0xffffffff;
    return crc;
}

fn main() {
    let crc = crc32("The quick brown fox jumps over the lazy dog");
    println "{crc:x}";
}
```

**Output:**

```
414fa339
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**CRC-32**](https://rosettacode.org/wiki/CRC-32) in Zen C.

*This article uses material from the Rosetta Code article **CRC-32**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/CRC-32?action=history).*
