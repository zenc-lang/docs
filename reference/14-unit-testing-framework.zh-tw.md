+++
title = "14. 單元測試框架"
weight = 14
+++

# 14. 單元測試框架


Zen C 内置了測試框架，允許你使用 `test` 關鍵字直接在源文件中編寫單元測試。

#### 語法
`test` 塊包含一個描述性名稱和要執行的代碼體。測試不需要 `main` 函數即可運行。

```zc
test "unittest1" {
    "這是一個單元測試";

    let a = 3;
    assert(a > 0, "a 應該是一個正整數");

    "unittest1 通過。";
}
```

#### 運行測試
要運行文件中的所有測試，請使用 `run` 命令。編譯器將自動檢測並執行所有頂層 `test` 塊。

```bash
zc run my_file.zc
```

#### 斷言
使用內置的 `assert(condition, message)` 函數來驗證預期。如果條件為假，測試將失敗並打印提供的消息。

---

## 貢獻

我們歡迎各類貢獻！無論是修復 Bug、完善文檔，還是提出新功能建議。

請參閱 [CONTRIBUTING_ZH_TW.md](CONTRIBUTING_ZH_TW.md) 了解有關如何貢獻、運行測試和提交拉取請求的詳細指南。

---

## 安全

關於安全漏洞報告的說明，請參閱 [SECURITY_ZH_TW.md](SECURITY_ZH_TW.md)。

---

## 致謝與歸属

本項目使用了第三方庫。完整許可證文本可在 `LICENSES/` 目錄中找到。

*   **[cJSON](https://github.com/DaveGamble/cJSON)** (MIT 許可證)：用於語言服務器中的 JSON 解析和生成。
*   **[zc-ape](https://github.com/OEvgeny/zc-ape)** (MIT 許可證)：由 [Eugene Olonov](https://github.com/OEvgeny) 開發的原版 Zen-C 實際上便攜的可執行文件 (APE) 端口。
*   **[Cosmopolitan Libc](https://github.com/jart/cosmopolitan)** (ISC 許可證)：使 APE 成為可能納基礎庫。
*   **[TRE](https://github.com/laurikari/tre)** (BSD 許可證)：用於標準庫中的正則表達式引擎。
*   **[zenc.vim](https://github.com/zenc-lang/zenc.vim)** (MIT 許可證)：官方 Vim/Neovim 插件，主要作者為 **[davidscholberg](https://github.com/davidscholberg)**。

---

<div align="center">
  <p>
    Copyright © 2026 Zen C 編程語言。<br>
    今天就開始你的旅程。
  </p>
  <p>
    <a href="https://discord.com/invite/q6wEsCmkJP">Discord</a> •
    <a href="https://github.com/zenc-lang/zenc">GitHub</a> •
    <a href="https://github.com/zenc-lang/docs">文檔</a> •
    <a href="https://github.com/zenc-lang/awesome-zenc">範例</a> •
    <a href="https://github.com/zenc-lang/rfcs">RFC</a> •
    <a href="CONTRIBUTING_ZH_TW.md">貢獻</a>
  </p>
</div>
