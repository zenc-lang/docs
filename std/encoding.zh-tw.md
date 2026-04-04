# std/encoding

`std/encoding` 模組包含用於在不同數據格式和編碼（如 Base64）之間進行轉換的工具。

## 使用

```zc
import "std/encoding/base64.zc"

fn main() {
    let original = "Zen-C";
    
    // 編碼為 Base64
    let encoded = Base64::encode(original);
    println "編碼後: {encoded}";
    
    // 解碼
    let decoded = Base64::decode(encoded);
    println "解碼後: {decoded}";
}
```

## 支持的編碼

### Base64

| 方法 | 簽名 | 描述 |
| :--- | :--- | :--- |
| **encode** | `Base64::encode(data: char*) -> String` | 將字符串或字節轉換為 Base64。 |
| **decode** | `Base64::decode(data: char*) -> String` | 將 Base64 字符串恢復為其原始形式。 |

### Hex (十六進制)

| 方法 | 簽名 | 描述 |
| :--- | :--- | :--- |
| **encode** | `Hex::encode(data: u8*, n: usize) -> String` | 將字節數組轉換為十六進制字符串。 |
| **decode** | `Hex::decode(s: char*) -> Vec<u8>` | 將十六進制字符串解碼為字節。 |

走
