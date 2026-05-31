+++
title = "Chaocipher"
+++

# Chaocipher

{{trans|C}}

```zc
enum CMode {
    ENCRYPT,
    DECRYPT
}

def L_ALPHABET = "HXUCZVAMDSLKPEFJRIGTWOBNYQ";
def R_ALPHABET = "PTLNBQDEOYSFAVZKGJRIHWXUMC";

fn chao(input: const char*, output: char*, mode: CMode, show_steps: bool) {
    let len = strlen(input);
    let left:  char[27];
    let right: char[27];
    let temp:  char[27];
    strcpy(left, L_ALPHABET);
    strcpy(right, R_ALPHABET);
    temp[26] = '\0';

    for i in 0..len {
        if show_steps { println "{left}  {right}"; }
        let index: int;
        if mode == CMode::ENCRYPT {
            index = strchr(right, input[i]) - right;
            output[i] = left[index];
        } else {
            index = strchr(left, input[i]) - left;
            output[i] = right[index];
        }
        if i == len - 1 { break; }
        let store: char;

        /* permute left */

        for let j = index; j < 26; ++j { temp[j - index] = left[j]; }
        for let j = 0; j < index; ++j  { temp[26 - index + j] = left[j]; }
        store = temp[1];
        for let j = 2; j < 14; ++j { temp[j - 1] = temp[j]; }
        temp[13] = store;
        strcpy(left, temp);

        /* permute right */

        for let j = index; j < 26; ++j { temp[j - index] = right[j]; }
        for let j = 0; j < index; ++j  { temp[26 - index + j] = right[j]; }
        store = temp[0];
        for let j = 1; j < 26; ++j { temp[j - 1] = temp[j]; }
        temp[25] = store;
        store = temp[2];
        for let j = 3; j < 14; ++j { temp[j - 1] = temp[j]; }
        temp[13] = store;
        strcpy(right, temp);
    }
}

fn main() {
    let plain_text = "WELLDONEISBETTERTHANWELLSAID";
    autofree let cipher_text = (char*)malloc(strlen(plain_text) + 1);
    autofree let plain_text2 = (char*)malloc(strlen(plain_text) + 1);
    println "The original plaintext is : {plain_text}";
    println "\nThe left and right alphabets after each permutation during encryption are :\n";
    chao(plain_text, cipher_text, CMode::ENCRYPT, true);
    println "\nThe ciphertext is : {cipher_text}";
    chao(cipher_text, plain_text2, CMode::DECRYPT, false);
    println "\nThe recovered plaintext is : {plain_text2}";
}
```

**Output:**

```
The original plaintext is : WELLDONEISBETTERTHANWELLSAID

The left and right alphabets after each permutation during encryption are :

HXUCZVAMDSLKPEFJRIGTWOBNYQ  PTLNBQDEOYSFAVZKGJRIHWXUMC
ONYQHXUCZVAMDBSLKPEFJRIGTW  XUCPTLNBQDEOYMSFAVZKGJRIHW
ADBSLKPEFJRIGMTWONYQHXUCZV  OYSFAVZKGJRIHMWXUCPTLNBQDE
HUCZVADBSLKPEXFJRIGMTWONYQ  NBDEOYSFAVZKGQJRIHMWXUCPTL
QUCZVADBSLKPEHXFJRIGMTWONY  NBEOYSFAVZKGQDJRIHMWXUCPTL
HFJRIGMTWONYQXUCZVADBSLKPE  JRHMWXUCPTLNBIEOYSFAVZKGQD
CVADBSLKPEHFJZRIGMTWONYQXU  YSAVZKGQDJRHMFWXUCPTLNBIEO
NQXUCVADBSLKPYEHFJZRIGMTWO  BIOYSAVZKGQDJERHMFWXUCPTLN
YHFJZRIGMTWONEQXUCVADBSLKP  RHFWXUCPTLNBIMOYSAVZKGQDJE
NQXUCVADBSLKPEYHFJZRIGMTWO  MOSAVZKGQDJERYHFWXUCPTLNBI
XCVADBSLKPEYHUFJZRIGMTWONQ  AVKGQDJERYHFWZXUCPTLNBIMOS
TONQXCVADBSLKWPEYHUFJZRIGM  IMSAVKGQDJERYOHFWZXUCPTLNB
SKWPEYHUFJZRILGMTONQXCVADB  RYHFWZXUCPTLNOBIMSAVKGQDJE
ZILGMTONQXCVARDBSKWPEYHUFJ  LNBIMSAVKGQDJOERYHFWZXUCPT
JILGMTONQXCVAZRDBSKWPEYHUF  LNIMSAVKGQDJOBERYHFWZXUCPT
RBSKWPEYHUFJIDLGMTONQXCVAZ  RYFWZXUCPTLNIHMSAVKGQDJOBE
RSKWPEYHUFJIDBLGMTONQXCVAZ  YFZXUCPTLNIHMWSAVKGQDJOBER
HFJIDBLGMTONQUXCVAZRSKWPEY  LNHMWSAVKGQDJIOBERYFZXUCPT
JDBLGMTONQUXCIVAZRSKWPEYHF  MWAVKGQDJIOBESRYFZXUCPTLNH
BGMTONQUXCIVALZRSKWPEYHFJD  VKQDJIOBESRYFGZXUCPTLNHMWA
YFJDBGMTONQUXHCIVALZRSKWPE  HMAVKQDJIOBESWRYFGZXUCPTLN
HIVALZRSKWPEYCFJDBGMTONQUX  RYGZXUCPTLNHMFAVKQDJIOBESW
QXHIVALZRSKWPUEYCFJDBGMTON  SWYGZXUCPTLNHRMFAVKQDJIOBE
KPUEYCFJDBGMTWONQXHIVALZRS  NHMFAVKQDJIOBRESWYGZXUCPTL
SPUEYCFJDBGMTKWONQXHIVALZR  NHFAVKQDJIOBRMESWYGZXUCPTL
OQXHIVALZRSPUNEYCFJDBGMTKW  WYZXUCPTLNHFAGVKQDJIOBRMES
UEYCFJDBGMTKWNOQXHIVALZRSP  GVQDJIOBRMESWKYZXUCPTLNHFA
JBGMTKWNOQXHIDVALZRSPUEYCF  OBMESWKYZXUCPRTLNHFAGVQDJI

The ciphertext is : OAHQHCNYNXTSZJRRHJBYHQKSOUJY

The recovered plaintext is : WELLDONEISBETTERTHANWELLSAID
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Chaocipher**](https://rosettacode.org/wiki/Chaocipher) in Zen C.

*This article uses material from the Rosetta Code article **Chaocipher**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Chaocipher?action=history).*
