+++
title = "12. 高級與元編程"
weight = 12
+++

# 12. 高級與元編程


### 元編程

#### Comptime
在編譯時運行程式碼以生成原始碼或列印訊息。
```zc
comptime {
    // 在編譯時生成程式碼(寫入 stdout)
    println "let build_date = \"2024-01-01\";";
}

println "Build Date: {build_date}";
```

**輔助函式**

`comptime` 區塊內可用的特殊函式:
- **`yield(str)`** - 明確輸出生成的程式碼(printf 的替代方案)
- **`compile_error(msg)`** - 以致命錯誤訊息停止編譯
- **`compile_warn(msg)`** - 發出編譯時警告(允許繼續編譯)

```zc
comptime {
    compile_warn("正在生成最佳化程式碼...");
    
    let ENABLE_FEATURE = 1;
    if (ENABLE_FEATURE == 0) {
        compile_error("必須啟用功能!");
    }
    
    println "let FEATURE_ENABLED = 1;";
}
```

**構建元數據**

在編譯時存取編譯器構建資訊:
- **`__COMPTIME_TARGET__`** - 平台字串: `"linux"`, `"windows"` 或 `"macos"`
- **`__COMPTIME_FILE__`** - 當前正在編譯的原始檔案名稱

```zc
comptime {
    // 平台特定的程式碼生成
    println "let PLATFORM = \"{__COMPTIME_TARGET__}\";";
}

println "運行於: {PLATFORM}";
```

{% alert(type="tip") %}
在 comptime 字串內使用 `{{` 和 `}}` 來轉義大括號。
{% end %}

#### Embed
將文件嵌入為指定類型。
```zc
// 默認 (Slice_char)
let data = embed "assets/logo.png";

// 類型化嵌入
let text = embed "shader.glsl" as string;    // 嵌入為 C-string
let rom  = embed "bios.bin" as u8[1024];     // 嵌入為固定數組
let wav  = embed "sound.wav" as u8[];        // 嵌入為 Slice_u8
```

#### 插件
導入編譯器插件以擴展語法。
```zc
import plugin "regex"
let re = regex! { ^[a-z]+$ };
```

#### 泛型 C 宏
將預處理器宏傳遞給 C。

{% alert(type="tip") %}
對於簡單的常量，請使用 `def`。當你需要 C 預處理器宏或條件編譯標誌時，請使用 `#define`。
{% end %}

```zc
#define MAX_BUFFER 1024
```

#### 條件編譯
使用 `@cfg()` 根據 `-D` 標誌有條件地包含或排除任何頂層聲明。

```zc
// 編譯: zc build app.zc -DUSE_OPENGL

@cfg(USE_OPENGL)
import "opengl_backend.zc";

@cfg(USE_VULKAN)
import "vulkan_backend.zc";

@cfg(not(USE_OPENGL))
@cfg(not(USE_VULKAN))
fn fallback_init() { println "未選擇後端"; }
```

| 形式 | 含義 |
|:---|:---|
| `@cfg(NAME)` | 如果設定了 `-DNAME` 則包含 |
| `@cfg(not(NAME))` | 如果未設定 `-DNAME` 則包含 |
| `@cfg(any(A, B, ...))` | 如果任意條件為真則包含 (OR) |
| `@cfg(all(A, B, ...))` | 如果所有條件為真則包含 (AND) |

一個聲明上的多個 `@cfg` 使用 AND 組合。`not()` 可以在 `any()` 和 `all()` 內部使用。適用於任何頂層聲明：`fn`、`struct`、`import`、`impl`、`raw`、`def`、`test` 等。

### 屬性

修飾函數和結構體以修改編譯器行為。

| 屬性 | 作用域 | 描述 |
|:---|:---|:---|
| `@required` | 函數 | 如果忽略返回值則發出警告。 |
| `@deprecated("msg")` | 函數/結構體 | 使用時發出帶有消息的警告。 |
| `@inline` | 函數 | 提示編譯器進行內聯。 |
| `@noinline` | 函數 | 防止內聯。 |
| `@packed` | 結構體 | 移除字段間的填充。 |
| `@align(N)` | 結構體 | 強制按 N 字节對齊。 |
| `@constructor` | 函數 | 在 main 之前運行。 |
| `@destructor` | 函數 | 在 main 退出後運行。 |
| `@unused` | 函數/變量 | 抑制未使用變量警告。 |
| `@weak` | 函數 | 弱符號鏈接。 |
| `@section("name")` | 函數 | 將代碼放置在特定段中。 |
| `@noreturn` | 函數 | 函數不會返回 (例如 exit)。 |
| `@pure` | 函數 | 函數無副作用 (優化提示)。 |
| `@cold` | 函數 | 函數不太可能被執行 (分支預測提示)。 |
| `@hot` | 函數 | 函數頻繁執行 (優化提示)。 |
| `@export` | 函數/結構體 | 導出符號 (默認可見性)。 |
| `@global` | 函數 | CUDA: 內核入口點 (`__global__`)。 |
| `@device` | 函數 | CUDA: 設備函數 (`__device__`)。 |
| `@host` | 函數 | CUDA: 主機函數 (`__host__`)。 |
| `@comptime` | 函數 | 用於編譯時執行的輔助函數。 |
| `@cfg(NAME)` | 任意 | 條件編譯：僅在傳遞 `-DNAME` 時包含。支援 `not()`、`any()`、`all()`。 |
| `@derive(...)` | 結構體 | 自動實現 Trait。支持 `Debug`, `Eq` (智能派生), `Copy`, `Clone`。 |
| `@ctype("type")` | 函數參數 | 覆蓋參數生成的 C 類型。 |
| `@<custom>` | 任意 | 將泛型屬性傳遞給 C (例如 `@flatten`, `@alias("name")`)。 |

#### 自定義屬性

Zen C 支持強大的 **自定義屬性** 系統，允許你在代碼中直接使用任何 GCC/Clang 的 `__attribute__`。任何不被 Zen C 編譯器顯式識別的屬性都會被視為泛型屬性並傳遞給生成的 C 代碼。

這提供了對高級編譯器特性、優化和鏈接器指令的訪問，而無需在語言核心中提供顯式支持。

#### 語法映射
Zen C 屬性直接映射到 C 屬性：
- `@name` → `__attribute__((name))`
- `@name(args)` → `__attribute__((name(args)))`
- `@name("string")` → `__attribute__((name("string")))`

#### 智能派生

Zen C 提供了尊重移動語義的 "智能派生"：

- **`@derive(Eq)`**：生成一個通過引用獲取參數的相等性方法 (`fn eq(self, other: T*)`)。
    - 當比較兩個非 Copy 結構體 (`a == b`) 時，編譯器會自動通過引用傳遞 `b` (`&b`) 以避免移動它。
    - 字段上的遞歸相等性檢查也會優先使用指針訪問，以防止所有權轉移。

### 內聯匯編

Zen C 為內聯匯編提供了一流支持，直接轉譯為 GCC 風格的擴展 `asm`。

#### 基本用法
在 `asm` 塊內編寫原始匯編。字符串會自動拼接。
```zc
asm {
    "nop"
    "mfence"
}
```

#### Volatile
防止編譯器優化掉具有副作用的匯編代碼。
```zc
asm volatile {
    "rdtsc"
}
```

#### 命名約束
Zen C 通過命名綁定簡化了複雜的 GCC 約束語法。

```zc
// 語法: : out(變量) : in(變量) : clobber(寄存器)
// 使用 {變量} 佔位符語法以提高可讀性

fn add_five(x: int) -> int {
    let result: int;
    asm {
        "mov {x}, {result}"
        "add $5, {result}"
        : out(result)
        : in(x)
        : clobber("cc")
    }
    return result;
}
```

| 類型 | 語法 | GCC 等效項 |
|:---|:---|:---|
| **輸出** | `: out(variable)` | `"=r"(variable)` |
| **輸入** | `: in(variable)` | `"r"(variable)` |
| **破壞** | `: clobber("rax")` | `"rax"` |
| **內存** | `: clobber("memory")` | `"memory"` |

{% alert(type="note") %}
使用 Intel 語法時（通過 `-masm=intel`），必須確保你的構建配置正確（例如，`//> cflags: -masm=intel`）。TCC 不支持 Intel 語法的匯編。
{% end %}

### 構建指令

Zen C 支持在源文件頂部使用特殊註釋來配置構建過程，無需複雜的構建系統或 Makefile。

| 指令 | 參數 | 描述 |
|:---|:---|:---|
| `//> link:` | `-lfoo` 或 `path/to/lib.a` | 鏈接庫或對象文件。 |
| `//> lib:` | `path/to/libs` | 添加庫搜索路徑 (`-L`)。 |
| `//> include:` | `path/to/headers` | 添加包含頭文件搜索路徑 (`-I`)。 |
| `//> framework:` | `Cocoa` | 鏈接 macOS Framework。 |
| `//> cflags:` | `-Wall -O3` | 向 C 編譯器傳遞任意標誌。 |
| `//> define:` | `MACRO` 或 `KEY=VAL` | 定義預處理器宏 (`-D`)。 |
| `//> pkg-config:` | `gtk+-3.0` | 運行 `pkg-config` 並追加 `--cflags` 和 `--libs`。 |
| `//> shell:` | `command` | 在構建期間執行 shell 命令。 |
| `//> get:` | `http://url/file` | 如果特定文件不存在，則下載該文件。 |

#### 特性

**1. 操作系統守護 (OS Guarding)**
在指令前加上操作系統名稱，以使其僅在特定平台上應用。
受支持的前綴：`linux:`, `windows:`, `macos:` (或 `darwin:`)。

```zc
//> linux: link: -lm
//> windows: link: -lws2_32
//> macos: framework: Cocoa
```

**2. 環境變量展開**
使用 `${VAR}` 語法在指令中展開環境變量。

```zc
//> include: ${HOME}/mylib/include
//> lib: ${ZC_ROOT}/std
```

#### 示例

```zc
//> include: ./include
//> lib: ./libs
//> link: -lraylib -lm
//> cflags: -Ofast
//> pkg-config: gtk+-3.0

import "raylib.h"

fn main() { ... }
```

### 關鍵字

以下關鍵字在 Zen C 中是保留的。

#### 聲明
`alias`, `def`, `enum`, `fn`, `impl`, `import`, `let`, `module`, `opaque`, `struct`, `trait`, `union`, `use`

#### 控制流
`async`, `await`, `break`, `catch`, `continue`, `defer`, `do`, `else`, `for`, `goto`, `guard`, `if`, `loop`, `match`, `return`, `try`, `unless`, `while`

#### 特殊
`asm`, `assert`, `autofree`, `comptime`, `const`, `embed`, `launch`, `ref`, `sizeof`, `static`, `test`, `volatile`

#### 常量
`true`, `false`, `null`

#### C 保留字
以下標識符是保留的，因為它們是 C11 中的關鍵字：
`auto`, `case`, `char`, `default`, `double`, `extern`, `float`, `inline`, `int`, `long`, `register`, `restrict`, `short`, `signed`, `switch`, `typedef`, `unsigned`, `void`, `_Atomic`, `_Bool`, `_Complex`, `_Generic`, `_Imaginary`, `_Noreturn`, `_Static_assert`, `_Thread_local`

#### 運算符
`and`, `or`
