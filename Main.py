import sys 
import io
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget, QPlainTextEdit
from PyQt5.QtCore import QProcess
from Layout import CustomPalette

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class Console(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        CustomPalette.set_dark_palette(self)  # Setzen Sie das benutzerdefinierte Farbschema

        self.process = QProcess(self)
        self.terminal = QTextEdit(self)
        self.terminal.setReadOnly(True)

        # Layout für Widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)

        # Erstellen Sie ein QPlainTextEdit-Widget
        self.command_line = QPlainTextEdit(self)

        # Fügen Sie das QPlainTextEdit-Widget zum Layout hinzu
        layout.addWidget(self.command_line)

        # Schaltfläche zum Ausführen Ihrer Funktion
        self.run_button = QPushButton('run')
        layout.addWidget(self.run_button)

        # Schaltfläche zum Erstellen einer ausführbaren Datei
        self.create_exe_button = QPushButton('Erstelle EXE')
        layout.addWidget(self.create_exe_button)

        # QWidget-Layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # QMainWindow-Eigenschaften
        self.setCentralWidget(main_widget)
        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle('Konsolenanwendung')

        # Verbinden Sie die Schaltfläche "Ausführen" mit der Funktion
        self.run_button.clicked.connect(self.run_script)

        # Verbinden Sie die Schaltfläche "Erstelle EXE" mit der Funktion
        self.create_exe_button.clicked.connect(self.create_exe)

        # QWidget-Layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # QMainWindow-Eigenschaften
        self.setCentralWidget(main_widget)
        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle('Konsolenanwendung')

        # Verbinden Sie die Schaltfläche "Ausführen" mit der Funktion
        self.run_button.clicked.connect(self.run_script)

        # Verbinden Sie die Schaltfläche "Erstelle EXE" mit der Funktion
        self.create_exe_button.clicked.connect(self.create_exe)



    def run_script(self):
        # Holen Sie den Befehl aus dem QPlainTextEdit-Widget
        command = self.command_line.toPlainText()

        # Speichern Sie den Befehl in einer Datei
        with open('PyhtonApp.py', 'a', encoding='utf-8') as f:
            f.write(command + '\n')

        # Führen Sie den Befehl aus
        try:
            self.process.start('python', ['-c', command])
        except FileNotFoundError:
            # Handle missing Python interpreter
            self.terminal.append("Python interpreter not found. Please install Python.")
            return

        # Löschen Sie den Text aus dem QPlainTextEdit-Widget
        self.command_line.clear()

        # Zeigen Sie die Ausgabe im Terminal an
        self.process.readyReadStandardOutput.connect(self.print_output)
        self.process.readyReadStandardError.connect(self.print_output)

    
    def create_exe(self):
        # Führen Sie den Befehl aus, um eine ausführbare Datei zu erstellen
        try:
            subprocess.Popen("start powershell -Command pyinstaller --onefile PyhtonApp.py", shell=True)
        except FileNotFoundError:
            # Handle missing pyinstaller
            self.terminal.append("pyinstaller not found. Please install it using 'pip install pyinstaller'.")

    def print_output(self):
        output = str(self.process.readAllStandardOutput().data(), encoding='utf-8')
        error = str(self.process.readAllStandardError().data(), encoding='utf-8')

        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(output)
            f.write(error)

        self.terminal.append(output)
        self.terminal.append(error)

    def closeEvent(self, event):
        # Löschen Sie den Inhalt der Datei 'log.txt' beim Beenden des Programms
        open('log.txt', 'w').close()

def main():
    app = QApplication(sys.argv)
    console = Console()
    console.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()