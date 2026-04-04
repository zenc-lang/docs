# std/crypto

Das Modul `std/crypto` bietet kryptographische Primitiven und Hashing-Algorithmen.

## SHA1 (`std/crypto/sha1.zc`)

Implementierung des SHA1-Hashing-Algorithmus.

### Verwendung

```zc
import "std/crypto/sha1.zc"

fn main() {
    let data = "Hello";
    let digest = Sha1::hash((u8*)data, 5);
    // digest.bytes ist u8[20]
}
```

### Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **hash** | `Sha1::hash(data: u8*, len: usize) -> Sha1` | Berechnet den SHA1-Hash der angegebenen Daten. |

## SHA256 (`std/crypto/sha256.zc`)

Implementierung des modernen SHA-256-Hashing-Algorithmus (FIPS 180-4).

### Verwendung

```zc
import "std/crypto/sha256.zc"

fn main() {
    let hash = Sha256::hash("hello world");
    // hash ist ein Hexadezimal-String
}
```

### Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **hash** | `Sha256::hash(data: char*) -> String` | Berechnet den SHA-256-Hash des angegebenen Strings und gibt ihn als Hex-String zurück. |
