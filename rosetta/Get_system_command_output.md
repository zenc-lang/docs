+++
title = "Get system command output"
+++

# Get system command output

```zc
import "std/sys/info.zc"
import "std/process.zc"

fn main() {
    let info = SysInfo::get_uname();
    let is_windows = strcmp(info.sysname.c_str(), "Windows") == 0;
    let cmd = is_windows ? "dir" : "ls";
    let output = Command::new(cmd).output();
    if output.exit_code {
        println "Command failed with code {output.exit_code}";
    } else {
        println "Captured:\n{output.std_out}";
    }
}
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Get system command output**](https://rosettacode.org/wiki/Get_system_command_output) in Zen C.

*This article uses material from the Rosetta Code article **Get system command output**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Get_system_command_output?action=history).*
