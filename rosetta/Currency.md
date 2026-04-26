+++
title = "Currency"
+++

# Currency

{{libheader|GMP}}

```zc
//> link: -lgmp

import "gmp.h"

fn main() {
    let hamburgers: mpf_t;
    let milkshakes: mpf_t;
    let price1: mpf_t;
    let price2: mpf_t;
    let tax_pc: mpf_t;
    let total_pre_tax: mpf_t;
    let total_tax: mpf_t;
    let total_after_tax: mpf_t;
    let temp: mpf_t;

    mpf_init_set_ui(hamburgers, (c_ulong)4000000000000000);
    mpf_init_set_ui(milkshakes, (c_ulong)2);
    mpf_init_set_str(price1, "5.5", 10);
    mpf_init_set_str(price2, "2.86", 10);
    mpf_init_set_str(tax_pc, "0.0765", 10);
    mpf_inits(total_pre_tax, total_tax, total_after_tax, temp, NULL);

    mpf_mul(total_pre_tax, hamburgers, price1);
    mpf_mul(temp, milkshakes, price2);
    mpf_add(total_pre_tax, total_pre_tax, temp);
    mpf_mul(total_tax, total_pre_tax, tax_pc);
    mpf_add(total_after_tax, total_pre_tax, total_tax);
    gmp_printf("Total price before tax : $ %20.2Ff\n", total_pre_tax);
	gmp_printf("Total tax              : $ %20.2Ff\n", total_tax);
    gmp_printf("Total price after tax  : $ %20.2Ff\n", total_after_tax);
    mpf_clears(hamburgers, milkshakes, price1, price2, tax_pc,
               total_pre_tax, total_tax, total_after_tax, temp, NULL);
}
```

**Output:**

```
Total price before tax : $ 22000000000000005.72
Total tax              : $  1683000000000000.44
Total price after tax  : $ 23683000000000006.16
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Currency**](https://rosettacode.org/wiki/Currency) in Zen C.

*This article uses material from the Rosetta Code article **Currency**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Currency?action=history).*
