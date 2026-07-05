+++
title = "16. 診斷系統"
weight = 16
+++

# 16. 診斷系統


Zen C 提供了一個分類診斷系統，可以對編譯器警告進行粒度控制。這有助於在保持高程式碼品質標準的同時，減少與外部 C 程式碼交互時的摩擦。

#### 診斷類別

警告按邏輯類別分組。可以使用編譯器標誌全局啟用或禁用每個類別。

| 類別 | 描述 | 默認值 |
| :--- | :--- | :--- |
| **`INTEROP`** | 與導入 C 標頭檔和未定義的外部函數相關的警告。 | **OFF** |
| **`PEDANTIC`** | 針對潛在問題或程式碼品質的額外嚴格檢查。 | **OFF** |
| **`UNUSED`** | 對已定義但未使用的變數、參數或函數的警告。 | **ON** |
| **`SAFETY`** | 關鍵安全警告，如空指標存取或除以零。 | **ON** |
| **`LOGIC`** | 與邏輯相關的警告，如不可達程式碼或常量比較。 | **ON** |
| **`CONVERSION`** | 隱式或窄化型別轉換的警告。 | **ON** |
| **`STYLE`** | 編碼風格警告，如變數遮蔽 (shadowing)。 | **ON** |

#### 編譯器標誌

你可以使用 `-W`（啟用）和 `-Wno-`（禁用）標誌，後跟類別名稱或特定診斷 ID 來控制診斷。

##### 類別標誌

- `-Winterop`: 啟用所有與互操作性相關的警告。
- `-Wno-unused`: 特別靜音未使用變數/參數的警告。
- `-Wsafety`: 確保所有安全檢查都處於活動狀態。
- `-Wall`: 啟用所有主要的診斷類別。
- `-Wextra`: 啟用更嚴格的診斷（相當於 `-Wpedantic`）。

##### 使用範例

```bash
# 啟用 C 互操作性警告進行編譯
zc app.zc -Winterop

# 啟用除未使用程式碼外的所有警告進行編譯
zc app.zc -Wall -Wno-unused
```

#### C 互操作性摩擦

默认情况下，Zen C 會抑制可能屬於 C 標準庫的函數的“未定義函數”警告（`INTEROP` 類別為 **OFF**）。

如果你希望編譯器嚴格標記每個未定義的函數（例如，為了發現拼寫錯誤），請啟用 interop 類別：

```bash
zc main.zc -Winterop
```

啟用後，編譯器將為常見的 C 函數提供有用的建議：
```
warning: Undefined function 'abs'
  --> main.zc:5:13
   |
5  |     let x = abs(-5);
   |             ^ here
   |
   = note: If this is a C function, it might need to be whitelisted in 'zenc.json'
```

#### 白名單

如果你經常使用特定的 C 庫，並希望在啟用 `-Winterop` 的情況下不被特定函數干擾，可以在 `zenc.json` 配置檔案中的 `c_function_whitelist` 中添加它們。

---

## 標準庫

Zen C 包含一個涵蓋基本功能的標準庫 (`std`)。

[瀏覽標準庫文檔](../docs/std/README.md)

### 核心模塊

<details>
<summary>點擊查看所有標準庫模塊</summary>

| 模塊 | 描述 | 文檔 |
| :--- | :--- | :--- |
| **`std/bigfloat.zc`** | 任意精度浮點運算。 | [文檔](../docs/std/bigfloat.md) |
| **`std/bigint.zc`** | 任意精度整數 `BigInt`。 | [文檔](../docs/std/bigint.md) |
| **`std/bits.zc`** | 底層位運算操作 (`rotl`, `rotr` 等)。 | [文檔](../docs/std/bits.md) |
| **`std/complex.zc`** | 複數算術 `Complex`。 | [文檔](../docs/std/complex.md) |
| **`std/vec.zc`** | 可增長動態數組 `Vec<T>`。 | [文檔](../docs/std/vec.md) |
| **`std/string.zc`** | 堆分配的 `String` 類型，支持 UTF-8。 | [文檔](../docs/std/string.md) |
| **`std/queue.zc`** | 先進先出隊列 (環形緩衝區)。 | [文檔](../docs/std/queue.md) |
| **`std/map.zc`** | 泛型哈希表 `Map<V>`。 | [文檔](../docs/std/map.md) |
| **`std/fs.zc`** | 文件系統操作。 | [文檔](../docs/std/fs.md) |
| **`std/io.zc`** | 標準輸入/輸出 (`print`/`println`)。 | [文檔](../docs/std/io.md) |
| **`std/option.zc`** | 可選值 (`Some`/`None`)。 | [文檔](../docs/std/option.md) |
| **`std/result.zc`** | 錯誤處理 (`Ok`/`Err`)。 | [文檔](../docs/std/result.md) |
| **`std/path.zc`** | 跨平台路徑操作。 | [文檔](../docs/std/path.md) |
| **`std/env.zc`** | 進程環境變量。 | [文檔](../docs/std/env.md) |
| **`std/net/`** | TCP, UDP, HTTP, DNS, URL. | [文檔](../docs/std/net.md) |
| **`std/thread.zc`** | 線程與同步。 | [文檔](../docs/std/thread.md) |
| **`std/time.zc`** | 時間測量與睡眠。 | [文檔](../docs/std/time.md) |
| **`std/json.zc`** | JSON 解析與序列化。 | [文檔](../docs/std/json.md) |
| **`std/stack.zc`** | 後進先出棧 `Stack<T>`。 | [文檔](../docs/std/stack.md) |
| **`std/set.zc`** | 泛型哈希集合 `Set<T>`。 | [文檔](../docs/std/set.md) |
| **`std/process.zc`** | 進程執行與管理。 | [文檔](../docs/std/process.md) |
| **`std/regex.zc`** | 正則表達式 (基於 TRE)。 | [文檔](../docs/std/regex.md) |
| **`std/simd.zc`** | 原生 SIMD 向量類型。 | [文檔](../docs/std/simd.md) |

</details>

---

## Further Reading

- **Language Server**: 查看 [LSP 文件](../LSP.md) 了解編輯器整合。
- **MISRA Compliance**: 查看 [MISRA Rules](17-misra-rules) 取得完整規則參考。
- **Contributing**: 查看 [Contributing Guide](../README.md#contributing) 了解貢獻指南。
