+++
title = "1. 變量與常量"
weight = 1
+++

# 1. 變量與常量 {#1-bian-liang-yu-chang-liang}


Zen C 區分編譯時常量和運行時變量。

#### 清單常量 (`def`)
僅在編譯時存在的值（折疊到代碼中）。用於數組大小、固定配置和魔術數字。

```zc
def MAX_SIZE = 1024;
let buffer: char[MAX_SIZE]; // 有效的數組大小
```

#### 變量 (`let`)
內存中的存儲位置。可以是可變的或只讀的 (`const`)。

```zc
let x = 10;             // 可變
x = 20;                 // 允許

let y: const int = 10;  // 只讀 (類型修飾)
// y = 20;              // 錯誤：無法賦值給 const 變量
```

{% alert(type="tip") %}
**型別推導**：Zen C 自動推導初始化變數的型別。在支援的編譯器上編譯為 C23 的 `auto`，否則使用 GCC 的 `__auto_type` 擴充功能。
{% end %}
