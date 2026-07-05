+++
title = "14. C 互操作性"
weight = 14
+++

# 14. C 互操作性 {#14-c-hu-cao-zuo-xing}


Zen C 提供畫兩種與 C 程式碼交互的方式：**信任導入 (Trusted Imports)** (方便) 和 **顯式 FFI** (安全/精確)。

#### 方法 1: 信任導入 (方便)

你可以使用 `import` 關鍵字直接導入 `.h` 擴充功能的 C 標頭檔。這會將標頭檔視為一個模組，並假設通過它存取的所有符號都存在。

```zc
//> link: -lm
import "math.h" as c_math;

fn main() {
    // 編譯器不僅信任其正確性；還會直接生成 'cos(...)'
    let x = c_math::cos(3.14159);
}
```

{% alert(type="note") %}
零樣板程式碼。立即存取標頭檔中的所有內容。
**缺點**: Zen C 不提供型別安全 (錯誤將在稍後由 C 編譯器捕獲)。
{% end %}

#### 方法 2: 顯式 FFI (安全)

對於嚴格的型別檢查或當你不想包含標頭檔文字時，請使用 `extern fn`。

```zc
include <stdio.h> // 在生成的 C 程式碼中發出 #include <stdio.h>

// 定義嚴格的簽名
extern fn printf(fmt: char*, ...) -> c_int;

fn main() {
    printf("Hello FFI: %d\n", 42); // 由 Zen C 進行型別檢查
}
```

{% alert(type="note") %}
Zen C 確保型別匹配。
**缺點**: 需要手動聲明函數。
{% end %}

#### `import` vs `include`

- **`import "file.h"`**: 將標頭檔註冊為命名模組。啟用對符號的隱式存取 (例如 `file::function()`)。
- **`include <file.h>`**: 僅在生成的 C 程式碼中發出 `#include <file.h>`。不會向 Zen C 編譯器引入任何符號；你必須使用 `extern fn` 來存取它們。
