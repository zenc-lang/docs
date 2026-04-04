# std/math

O módulo `std/math` fornece funções matemáticas comuns e constantes para aritmética de vírgula flutuante (f32 e f64), envolvendo a biblioteca matemática padrão de C (`math.h`).

## Uso

```zc
import "std/math.zc"

fn main() {
    let v = 16.0;
    let res = Math::sqrt(v); // 4.0
    
    let angulo = Math::PI / 2.0;
    let s = Math::sin(angulo); // 1.0
}
```

## Constantes

| Constante | Valor aproximado | Descrição |
| :--- | :--- | :--- |
| **Math::PI** | `3.14159265` | Rácio entre o perímetro e o diâmetro de um círculo. |
| **Math::E** | `2.71828182` | Base dos logaritmos naturais (número de Euler). |

## Funções Básicas

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **abs** | `Math::abs(v: double) -> double` | Retorna o valor absoluto. |
| **sqrt** | `Math::sqrt(v: double) -> double` | Calcula a raiz quadrada. |
| **pow** | `Math::pow(base: double, exp: double) -> double` | Eleva a base ao expoente fornecido. |
| **ceil** | `Math::ceil(v: double) -> double` | Arredonda para cima (teto). |
| **floor** | `Math::floor(v: double) -> double` | Arredonda para baixo (chão). |
| **round** | `Math::round(v: double) -> double` | Arredonda para o inteiro mais próximo. |

## Trigonometria

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **sin** | `Math::sin(v: double) -> double` | Calcula o seno (em radianos). |
| **cos** | `Math::cos(v: double) -> double` | Calcula o cosseno. |
| **tan** | `Math::tan(v: double) -> double` | Calcula a tangente. |
| **asin** | `Math::asin(v: double) -> double` | Calcula o arco-seno. |
| **acos** | `Math::acos(v: double) -> double` | Calcula o arco-cosseno. |
| **atan** | `Math::atan(v: double) -> double` | Calcula o arco-tangente. |

## Logaritmos e Exponenciais

| Método | Assinatura | Descrição |
| :--- | :--- | :--- |
| **log** | `Math::log(v: double) -> double` | Logaritmo natural (base e). |
| **log10** | `Math::log10(v: double) -> double` | Logaritmo decimal (base 10). |
| **exp** | `Math::exp(v: double) -> double` | Exponencial (e^v). |
走
