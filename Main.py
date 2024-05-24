import sys
import io
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget, QPlainTextEdit, QSplitter, QHBoxLayout, QMenuBar, QAction
from PyQt5.QtCore import QProcess, Qt
from Layout import CustomPalette

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

class Console(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        CustomPalette.set_dark_palette(self)  # Setzen Sie das benutzerdefinierte Farbschema

        self.process = QProcess(self)
        self.terminal = QTextEdit(self)
        self.terminal.setReadOnly(True)

        # Erstellen Sie ein QSplitter-Widget
        self.splitter = QSplitter(Qt.Horizontal, self)

        # Fügen Sie die Widgets zum QSplitter hinzu
        self.splitter.addWidget(self.terminal)

        # Erstellen Sie ein QPlainTextEdit-Widget
        self.command_line = QPlainTextEdit(self)
        self.splitter.addWidget(self.command_line)

        # Layout für QSplitter
        layout = QVBoxLayout(self)
        layout.addWidget(self.splitter)

        # Menüleiste erstellen
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
       
        # In Ihrer Hauptklasse, nachdem Sie die Menüleiste erstellt haben:
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("QMenuBar { background-color: #353535; color: #FFFFFF; }")
        # Menüpunkte erstellen
        run_menu = menu_bar.addMenu('Run')
        create_exe_menu = menu_bar.addMenu('Create EXE')
        clear_output_menu = menu_bar.addMenu('Clear Output')  # Neuer Menüpunkt

       # Aktionen für Menüpunkte erstellen
        run_action = QAction('Run Script', self)
        create_exe_action = QAction('Create EXE', self)
        clear_output_action = QAction('Clear Output', self)  # Neuer Menüpunkt

        # Aktionen zu Menüpunkten hinzufügen
        run_menu.addAction(run_action)
        create_exe_menu.addAction(create_exe_action)
        clear_output_menu.addAction(clear_output_action)  # Neuer Menüpunkt
        # QWidget-Layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # QMainWindow-Eigenschaften
        self.setCentralWidget(main_widget)
        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle('Konsolenanwendung')

       # Verbinden Sie die Aktionen mit den Funktionen
        run_action.triggered.connect(self.run_script)
        create_exe_action.triggered.connect(self.create_exe)
        clear_output_action.triggered.connect(self.clear_output)  # Neuer Menüpunk



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

        # Zeigen Sie die Ausgabe im Terminal an
        self.process.readyReadStandardOutput.connect(self.print_output)
        self.process.readyReadStandardError.connect(self.print_output)


    
    def create_exe(self):
        # Führen Sie den Befehl aus, um eine ausführbare Datei zu erstellen
        try:
            subprocess.Popen("start powershell -Command pyinstaller --onefile --windowed PyhtonApp.py", shell=True)
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

    def clear_output(self):
        # Löschen Sie den Inhalt der Konsolenausgabe
        self.terminal.clear()

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