+++
title = "SHA-1"
+++

# SHA-1

```zc
import "std/crypto/sha1.zc"
import "std/encoding/hex.zc"

fn main() {
    let digest = Sha1::hash("Rosetta Code", 12);
    println "{Hex::encode(digest.bytes, 20)}";
}
```

**Output:**

```
48c98f7e5a6e736d790ab740dfc3f51a61abe2b5
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**SHA-1**](https://rosettacode.org/wiki/SHA-1) in Zen C.

*This article uses material from the Rosetta Code article **SHA-1**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/SHA-1?action=history).*
