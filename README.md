# Konsolenanwendung mit PyQt5

Diese Python-Anwendung bietet eine grafische Benutzeroberfläche (GUI), die es Benutzern ermöglicht, Python-Code zu schreiben, auszuführen und eine ausführbare Datei (.exe) aus dem Code zu erstellen.

## Hauptmerkmale

- **Interaktive Konsole**: Führen Sie Python-Code direkt in der Anwendung aus und sehen Sie die Ergebnisse im integrierten Terminal.
- **EXE-Generator**: Erstellen Sie mit einem Klick eine ausführbare Datei aus Ihrem Python-Code.

## Voraussetzungen

Bevor Sie diese Anwendung verwenden, stellen Sie sicher, dass Sie die folgenden Komponenten installiert haben:

- Python 3.x
- PyQt5
- PyInstaller

## Installation

Klonen Sie das Repository oder laden Sie den Code herunter und führen Sie die Anwendung mit dem folgenden Befehl aus:

```bash
python main.py

Benutzung
Starten Sie die Anwendung.
Geben Sie Ihren Python-Code in das untere Textfeld ein.
Klicken Sie auf ‘run’, um den Code auszuführen.
Klicken Sie auf ‘Erstelle EXE’, um eine ausführbare Datei zu generieren.
Funktionen
run_script
Diese Funktion liest den im QPlainTextEdit-Widget eingegebenen Python-Code und führt ihn aus. Die Ausgabe wird im QTextEdit-Terminal angezeigt.

create_exe
Diese Funktion verwendet PyInstaller, um eine ausführbare Datei aus dem eingegebenen Python-Code zu erstellen.

Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die LICENSE.md Datei für Details.
