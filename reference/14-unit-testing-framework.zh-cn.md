+++
title = "14. 单元测试框架"
weight = 14
+++

# 14. 单元测试框架


Zen C 内置了测试框架，允许你使用 `test` 关键字直接在源文件中编写单元测试。

#### 语法
`test` 块包含一个描述性名称和要执行的代码体。测试不需要 `main` 函数即可运行。

```zc
test "unittest1" {
    "这是一个单元测试";

    let a = 3;
    assert(a > 0, "a 应该是一个正整数");

    "unittest1 通过。";
}
```

#### 运行测试
要运行文件中的所有测试，请使用 `run` 命令。编译器将自动检测并执行所有顶层 `test` 块。

```bash
zc run my_file.zc
```

#### 断言
使用内置的 `assert(condition, message)` 函数来验证预期。如果条件为假，测试将失败并打印提供的消息。

---

## 贡献

我们欢迎各类贡献！无论是修复 Bug、完善文档，还是提出新功能建议。

请参阅 [CONTRIBUTING_ZH_CN.md](CONTRIBUTING_ZH_CN.md) 了解有关如何贡献、运行测试和提交拉取请求的详细指南。

---

## 安全

关于安全漏洞报告的说明，请参阅 [SECURITY_ZH_CN.md](SECURITY_ZH_CN.md)。

---

## 致谢与归属

本项目使用了第三方库。完整许可证文本可在 `LICENSES/` 目录中找到。

*   **[cJSON](https://github.com/DaveGamble/cJSON)** (MIT 许可证)：用于语言服务器中的 JSON 解析和生成。
*   **[zc-ape](https://github.com/OEvgeny/zc-ape)** (MIT 许可证)：由 [Eugene Olonov](https://github.com/OEvgeny) 开发的原版 Zen-C 实际上便携的可执行文件 (APE) 端口。
*   **[Cosmopolitan Libc](https://github.com/jart/cosmopolitan)** (ISC 许可证)：使 APE 成为可能的基础库。
*   **[TRE](https://github.com/laurikari/tre)** (BSD 许可证): 用于标准库中的正则表达式引擎。
*   **[zenc.vim](https://github.com/zenc-lang/zenc.vim)** (MIT 许可证): 官方 Vim/Neovim 插件，主要作者为 **[davidscholberg](https://github.com/davidscholberg)**。

---

<div align="center">
  <p>
    Copyright © 2026 Zen C 编程语言。<br>
    今天就开始你的旅程。
  </p>
  <p>
    <a href="https://discord.com/invite/q6wEsCmkJP">Discord</a> •
    <a href="https://github.com/zenc-lang/zenc">GitHub</a> •
    <a href="https://github.com/zenc-lang/docs">文档</a> •
    <a href="https://github.com/zenc-lang/awesome-zenc">示例</a> •
    <a href="https://github.com/zenc-lang/rfcs">RFC</a> •
    <a href="CONTRIBUTING_ZH_CN.md">贡献</a>
  </p>
</div>
