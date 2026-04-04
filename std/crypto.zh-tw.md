# std/crypto

`std/crypto` 模組提供加密函數、哈希算法和安全隨機數生成器。

## 使用

```zc
import "std/crypto.zc"

fn main() {
    // 生成一個安全的隨機數
    let key = Crypto::rand_u64();
    println "隨機密鑰: {key}";
}
```

## 功能

### 隨機數 (Secure Random)

與 `std/random` 不同，此模組使用系統級別的熵源（如 `/dev/urandom`）。

| 方法 | 簽名 | 描述 |
| :--- | :--- | :--- |
| **rand_u64**| `Crypto::rand_u64() -> u64` | 返回一個加密安全的 64 位整數。 |
| **fill_rand**| `Crypto::fill_rand(buf: u8*, n: usize)` | 用安全隨機字節填充緩衝區。 |

### 哈希算法 (Hashing)

該模組包含如下算法的實現：
- **SHA-256**: `std/crypto/sha256.zc`
- **MD5**: `std/crypto/md5.zc` (僅用於兼容性)
走
