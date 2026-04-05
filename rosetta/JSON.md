+++
title = "JSON"
+++

# JSON

```zc
import "std/json.zc"

fn main() {
    // Load a JSON string into a data structure
    // Double braces {{ }} are used to escape Zen C's string interpolation
    let input = "{{\"user\": \"zuhaitz\", \"version\": 4.2, \"active\": true}}";
    let json = JsonValue::parse_val(input).expect("failed to parse json");
    
    let user = json.get_string("user").unwrap();
    let active = json.get_bool("active").unwrap();
    println "Loaded User: {user} (Active: {active})";

    // Create a new data structure and serialize it into JSON
    let res = JsonValue::object(); 
    res.set("status", JsonValue::string("ok"));
    res.set("timestamp", JsonValue::number(1710422672));
    
    let tags = JsonValue::array();
    tags.push(JsonValue::string("zen-c"));
    tags.push(JsonValue::string("fast"));
    res.set("tags", tags);

    println "Serialized: {res.to_string().c_str()}";
}
```

**Output:**

```
Loaded User: zuhaitz (Active: true)
Serialized: {"tags":["zen-c","fast"],"timestamp":1710422672,"status":"ok"}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**JSON**](https://rosettacode.org/wiki/JSON) in Zen C.

*This article uses material from the Rosetta Code article **JSON**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/JSON?action=history).*
