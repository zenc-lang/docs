+++
title = "JSON vs Manual Parsing"
weight = 46
+++

# JSON vs Manual Parsing

Built-in JSON parsing vs C manual string parsing or third-party libraries.

## Zen C

```zc
import "std/json.zc"
import "std/io.zc"

fn main() {
    let data = r'{"name": "Zen", "value": 42}';
    let doc = json::parse(data);
    println "parsed ok";
}
```

## C

C has no built-in JSON support. The typical approach uses a library like cJSON:

```c
#include <stdio.h>
#include "cJSON.h"

int main(void) {
    const char* data = "{\"name\": \"C\", \"value\": 42}";
    cJSON* doc = cJSON_Parse(data);
    if (!doc) return 1;

    cJSON* name = cJSON_GetObjectItem(doc, "name");
    printf("parsed ok\n");
    cJSON_Delete(doc);
    return 0;
}
```

## Key Differences

- `json::parse(str)?` parses a JSON string, returning a DOM document
- Raw string `r"..."` avoids escape clutter for JSON literals
- `as_string()`, `as_int()`, `as_bool()`, `as_float()` for type-safe access
- C: no standard library JSON support, needs external library (cJSON, jansson)

## Output

parsed ok
