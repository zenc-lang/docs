# std/crypto

El módulo `std/crypto` proporciona primitivas criptográficas y algoritmos de hashing.

## SHA1 (`std/crypto/sha1.zc`)

Implementación del algoritmo de hashing SHA1.

### Uso

```zc
import "std/crypto/sha1.zc"

fn main() {
    let data = "Hola";
    let digest = Sha1::hash((u8*)data, 5);
    // digest.bytes es u8[20]
}
```

### Métodos

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **hash** | `Sha1::hash(data: u8*, len: usize) -> Sha1` | Calcula el hash SHA1 de los datos proporcionados. |

## SHA256 (`std/crypto/sha256.zc`)

Implementación del algoritmo de hashing moderno SHA-256 (FIPS 180-4).

### Uso

```zc
import "std/crypto/sha256.zc"

fn main() {
    let hash = Sha256::hash("hola mundo");
    // hash es una cadena hexadecimal
}
```

### Métodos

| Método | Firma | Descripción |
| :--- | :--- | :--- |
| **hash** | `Sha256::hash(data: char*) -> String` | Calcula el hash SHA-256 de la cadena dada y lo devuelve como una cadena Hex. |
