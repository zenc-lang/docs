+++
title = "Execute a system command"
+++

# Execute a system command

```zc
import "std/sys/info.zc"
import "std/process.zc"

fn main() {
    let info = SysInfo::get_uname();
    let is_windows = strcmp(info.sysname.c_str(), "Windows") == 0;
    let cmd = is_windows ? "dir" : "ls";
    let exit_code = Command::new(cmd).status();
    if exit_code {
        println "Command failed with code {exit_code}";
    }
}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Execute a system command**](https://rosettacode.org/wiki/Execute_a_system_command) in Zen C.

*This article uses material from the Rosetta Code article **Execute a system command**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Execute_a_system_command?action=history).*
