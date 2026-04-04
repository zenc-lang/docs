# std/complex

O módulo `std/complex` fornece suporte para aritmética de números complexos de dupla precisão.

## Uso

```zc
import "std/complex.zc"

fn main() {
    let z1 = Complex::new(1.0, 2.0); // 1 + 2i
    let z2 = Complex::new(3.0, 4.0); // 3 + 4i
    
    let sum = z1.add(z2); 
    println "Resultado: {sum.real} + {sum.imag}i";
}
```

## Definição da Estrutura

```zc
struct Complex {
    real: double;
    imag: double;
}
```

## Métodos

### Construção

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **new** | `Complex::new(re: double, im: double) -> Complex` | Cria um novo número complexo. |

### Operações Aritméticas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **add** | `add(self, other: Complex) -> Complex` | Adiciona dois números complexos. |
| **sub** | `sub(self, other: Complex) -> Complex` | Subtrai `other` de `self`. |
| **mul** | `mul(self, other: Complex) -> Complex` | Multiplica dois números complexos. |
| **div** | `div(self, other: Complex) -> Complex` | Divide `self` por `other`. |

### Funções Matemáticas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **abs** | `abs(self) -> double` | Calcula a magnitude (módulo) do número. |
| **arg** | `arg(self) -> double` | Calcula o argumento (fase). |
| **conj** | `conj(self) -> Complex` | Retorna o conjugado complexo. |
| **exp** | `exp(self) -> Complex` | Calcula o exponencial complexo. |
| **sqrt** | `sqrt(self) -> Complex` | Calcula a raiz quadrada complexa. |
走
