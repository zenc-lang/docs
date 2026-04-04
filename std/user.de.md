# std/sys/user

Das Modul `std/sys/user` bietet Zugriff auf Benutzer- und Gruppenidentifikations-Informationen und kapselt POSIX `unistd.h` ein.

## Überblick

- **Benutzeridentität**: Abrufen von realen und effektiven Benutzer-IDs (UID) und Gruppen-IDs (GID).
- **Prozesskontext**: Nützlich für die Überprüfung von Privilegien und die Berechtigungsverwaltung in Systemprogrammen.

## Verwendung

```zc
import "std/sys/user.zc"
import "std/io.zc"

fn main() {
    println "Aktuelle UID: {User::get_uid()}";
    println "Aktuelle GID: {User::get_gid()}";
    
    if (User::get_euid() == 0) {
        println "Wird mit Root-Privilegien ausgeführt.";
    }
}
```

## Struktur-Definition

```zc
struct User {}
```

## Methoden

### `User` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **get_uid** | `User::get_uid() -> u32` | Gibt die reale Benutzer-ID des aktuellen Prozesses zurück. |
| **get_gid** | `User::get_gid() -> u32` | Gibt die reale Gruppen-ID des aktuellen Prozesses zurück. |
| **get_euid** | `User::get_euid() -> u32` | Gibt die effektive Benutzer-ID zurück. |
| **get_egid** | `User::get_egid() -> u32` | Gibt die effektive Gruppen-ID zurück. |
