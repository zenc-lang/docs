# std/crypto

Il modulo `std/crypto` fornisce primitive crittografiche e algoritmi di hashing.

## SHA1 (`std/crypto/sha1.zc`)

Implementazione dell'algoritmo di hashing SHA1.

### Utilizzo

```zc
import "std/crypto/sha1.zc"

fn main() {
    let data = "Hello";
    let digest = Sha1::hash((u8*)data, 5);
    // digest.bytes è u8[20]
}
```

### Metodi

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **hash** | `Sha1::hash(data: u8*, len: usize) -> Sha1` | Calcola l'hash SHA1 dei dati forniti. |

## SHA256 (`std/crypto/sha256.zc`)

Implementazione del moderno algoritmo di hashing SHA-256 (FIPS 180-4).

### Utilizzo

```zc
import "std/crypto/sha256.zc"

fn main() {
    let hash = Sha256::hash("hello world");
    // hash è una stringa esadecimale
}
```

### Metodi

| Metodo | Firma | Descrizione |
| :--- | :--- | :--- |
| **hash** | `Sha256::hash(data: char*) -> String` | Calcola l'hash SHA-256 della stringa fornita e lo restituisce come stringa esadecimale. |
