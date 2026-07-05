+++
title = "7. 打印與字符串插值"
weight = 7
+++

# 7. 打印與字符串插值 {#7-da-yin-yu-zi-fu-chuan-cha-zhi}


Zen C 提供了多種控制台打印選項，包括關鍵字和簡潔的簡寫形式。

#### 關鍵字

| 關鍵字 | 描述 |
|:---|:---|
| `print "text"` | 打印到 `stdout`，不帶尾隨換行符。 |
| `println "text"` | 打印到 `stdout`，帶尾隨換行符。 |
| `eprint "text"` | 打印到 `stderr`，不帶尾隨換行符。 |
| `eprintln "text"` | 打印到 `stderr`，帶尾隨換行符。 |

#### 簡寫形式

Zen C 允許直接將字符串字面量用作語句來進行快速打印：

| 語法 | 等效項 | 描述 |
|:---|:---|:---|
| `"Hello World"` | `println "Hello World"` | 隱式添加換行符。 |
| `"Hello World"..` | `print "Hello World"` | 不帶尾隨換行符。 |
| `!"Error"` | `eprintln "Error"` | 輸出到 stderr。 |
| `!"Error"..` | `eprint "Error"` | 輸出到 stderr，不帶換行符。 |

#### 字符串插值 (String Interpolation)

你可以使用 `{}` 語法將表達式直接嵌入到字串字面量中。這適用於所有列印方法和字串簡寫。

Zen C 中的字串插值是**隱式**的：如果你的字串包含 `{...}`，它將自動被解析為插值字串。你也可以顯式地使用 `f` 作為前綴（例如 `f"..."`），以強制執行插值語義。

```zc
let x = 42;
let name = "Zen";
println "值: {x}, 名稱: {name}";
"值: {x}, 名稱: {name}"; // 簡寫形式的 println
```

**轉義花括號**：使用 `{{` 輸出字面量 `{`，使用 `}}` 輸出字面量 `}`：

```zc
let json = "JSON: {{\"鍵\": \"值\"}}";
// 輸出: JSON: {"鍵": "值"}
```

**原始字串 (Raw Strings)**：若要定義完全忽略插值與轉義序列的字串，請在其前加上 `r`（例如 `r"..."`）：

```zc
let regex = r"\w+"; // 包含精確的 \ w +
let raw_json = r'{"key": "value"}'; // 不需要跳脫大括號
```

#### 多行字串 (Multiline Strings)

Zen C 使用 `"""` 分隔符支持原始多行字串區塊。這對於編寫嵌入式語言（如 GLSL、HTML）或在 `comptime` 區塊生成 C 程式碼非常有用，你無需手動轉義換行符與內部引號。

與標準字串一樣，多行字串支持**隱式插值**。您也可以顯式地加上前綴：
- `f"""..."""`: 顯式標記為插值字串塊。
- `r"""..."""`: 顯式標記為原始字串塊（無插值，無轉義序列）。

```zc
let prompt = """
　請輸入您的名字：
　輸入 "exit" 取消。
""";

let world = "world";
let script = """
  fn hello() {
      println "hello, {world}!";
  }
""";

let pure_raw = r"""
  這裡的 {braces} 只是純文本，而 \n 就只是斜線和 n。
""";
```

#### 輸入提示 (`?`)

Zen C 支持使用 `?` 前綴進行用戶輸入提示的簡寫。

- `? "提示文本"`: 打印提示信息（不換行）並等待輸入（讀取一行）。
- `? "輸入年齡: " (age)`: 打印提示並掃描輸入到變量 `age` 中。
    - 格式說明符會根據變量類型自動推斷。

```zc
let age: int;
? "你多大了？ " (age);
println "你 {age} 歲了。";
```
