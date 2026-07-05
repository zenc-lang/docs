+++
title = "7. 打印与字符串插值"
weight = 7
+++

# 7. 打印与字符串插值 {#7-da-yin-yu-zi-fu-chuan-cha-zhi}


Zen C 提供了多种控制台打印选项，包括关键字和简洁的简写形式。

#### 关键字

| 关键字 | 描述 |
|:---|:---|
| `print "text"` | 打印到 `stdout`，不带尾随换行符。 |
| `println "text"` | 打印到 `stdout`，带尾随换行符。 |
| `eprint "text"` | 打印到 `stderr`，不带尾随换行符。 |
| `eprintln "text"` | 打印到 `stderr`，带尾随换行符。 |

#### 简写形式

Zen C 允许直接将字符串字面量用作语句来进行快速打印：

| 语法 | 等效项 | 描述 |
|:---|:---|:---|
| `"Hello World"` | `println "Hello World"` | 隐式添加换行符。 |
| `"Hello World"..` | `print "Hello World"` | 不带尾随换行符。 |
| `!"Error"` | `eprintln "Error"` | 输出到 stderr。 |
| `!"Error"..` | `eprint "Error"` | 输出到 stderr，不带换行符。 |

#### 字符串插值 (String Interpolation)

你可以使用 `{}` 语法将表达式直接嵌入到字符串字面量中。这适用于所有打印方法和字符串简写。

Zen C 中的字符串插值是**隐式**的：如果你的字符串包含 `{...}`，它将自动被解析为插值字符串。你也可以显式地使用 `f` 作为前缀（例如 `f"..."`），以强制执行插值语义。

```zc
let x = 42;
let name = "Zen";
println "值: {x}, 名称: {name}";
"值: {x}, 名称: {name}"; // 简写形式的 println
```

**转义花括号**：使用 `{{` 输出字面量 `{`，使用 `}}` 输出字面量 `}`：

```zc
let json = "JSON: {{\"键\": \"值\"}}";
// 输出: JSON: {"键": "值"}
```

**原始字符串 (Raw Strings)**：若要定义完全忽略插值与转义序列的字符串，请在其前加上 `r`（例如 `r"..."`）：

```zc
let regex = r"\w+"; // 包含精确的 \ w +
let raw_json = r'{"key": "value"}'; // 不需要转义大括号
```

#### 多行字符串 (Multiline Strings)

Zen C 使用 `"""` 分隔符支持原始多行字符串块。这对于编写嵌入式语言（如 GLSL、HTML）或在 `comptime` 块生成 C 代码非常有用，此时无需手动转义换行符与内部引号。

与标准字符串一样，多行字符串支持**隐式插值**。您也可以显式地加上前缀：
- `f"""..."""`: 显式标记为插值字符串块。
- `r"""..."""`: 显式标记为原始字符串块（无插值，无转义序列）。

```zc
let prompt = """
  请输入您的名字：
  输入 "exit" 取消。
""";

let world = "world";
let script = """
  fn hello() {
      println "hello, {world}!";
  }
""";

let pure_raw = r"""
  这里的 {braces} 只是纯文本，而 \n 就只是斜线和 n。
""";
```

#### 输入提示 (`?`)

Zen C 支持使用 `?` 前缀进行用户输入提示的简写。

- `? "提示文本"`: 打印提示信息（不换行）并等待输入（读取一行）。
- `? "输入年龄: " (age)`: 打印提示并扫描输入到变量 `age` 中。
    - 格式说明符会根据变量类型自动推断。

```zc
let age: int;
? "你多大了？ " (age);
println "你 {age} 岁了。";
```
