# std/process

Das Modul `std/process` bietet eine High-Level-API zum Erzeugen von Kindprozessen, Ausführen von Systembefehlen und Erfassen ihrer Ausgabe.

## Überblick

- **Builder-Pattern**: Die Struktur `Command` verwendet ein flüssiges Builder-Pattern zum Aufbau von Befehlszeilen.
- **Ausgabeerfassung**: Einfaches Erfassen von Standardausgabe und Exit-Codes abgeschlossener Prozesse.
- **RAII**: Sowohl `Command` als auch `Output` implementieren das `Drop`-Trait für die automatische Bereinigung interner Puffer.
- **Standard-Interop**: Kapselt nahtlos die zugrunde liegende Prozessmanipulation auf Systemebene ein.

## Verwendung

```zc
import "std/process.zc"

fn main() {
    // Grundlegende Befehlsausführung
    let output = Command::new("echo")
        .arg("hello world")
        .output();
        
    if (output.exit_code == 0) {
        println "Erfasst: {output.std_out}";
        // output.std_out ist ein String, wird automatisch freigegeben
    } else {
        println "Befehl fehlgeschlagen mit Code {output.exit_code}";
    }
}
```

## Struktur-Definitionen

### `Command`
Ein Builder zum Konfigurieren und Starten eines Prozesses.
```zc
struct Command {
    program: String;
    args: Vec<String>;
}
```

### `Output`
Das Ergebnis einer abgeschlossenen Befehlsausführung.
```zc
struct Output {
    std_out: String;
    exit_code: int;
}
```

## Methoden

### `Command` Methoden

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **new** | `Command::new(program: char*) -> Command` | Erstellt ein neues Command für das angegebene Programm. |
| **arg** | `arg(self, arg: char*) -> Command*` | Fügt ein Argument hinzu und gibt einen Zeiger auf sich selbst für Chaining zurück. |
| **output** | `output(self) -> Output` | Führt den Befehl aus und wartet auf dessen Abschluss, wobei stdout erfasst wird. |
| **status** | `status(self) -> int` | Führt den Befehl aus und gibt den Exit-Statuscode zurück. |

## Speicherverwaltung

| Methode | Signatur | Beschreibung |
| :--- | :--- | :--- |
| **free** | `free(self)` | Gibt interne Befehlspuffer manuell frei. |
| **Trait** | `impl Drop for Command` | Bereinigt Befehlspuffer automatisch. |
| **Trait** | `impl Drop for Output` | Gibt den erfassten Ausgabe-String automatisch frei. |
