import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Define UI Elements
        self.file_path = ""
        self.editor_text = self.ui.textEdit
        self.status_bar = self.ui.statusbar

        # Connect Menu Bar Items To Respective Functions
        self.ui.actionOpenFile.triggered.connect(self.openFile)
        self.ui.actionNewFile.triggered.connect(self.newFile)
        self.ui.actionSaveFile.triggered.connect(self.saveFile)
        self.ui.actionExit.triggered.connect(self.exitApp)

        self.ui.actionUndo.triggered.connect(self.undoLast)
        self.ui.actionRedo.triggered.connect(self.redoLast)

        # Set Shortcuts For Menu Items
        self.ui.actionOpenFile.setShortcut("Ctrl+O")
        self.ui.actionNewFile.setShortcut("Ctrl+N")
        self.ui.actionSaveFile.setShortcut("Ctrl+S")
        self.ui.actionExit.setShortcut("Ctrl+Q")

        self.ui.actionUndo.setShortcut("Ctrl+Z")
        self.ui.actionRedo.setShortcut("Ctrl+Y")

    def show(self):
        self.main_win.show()

    def newFile(self):
        pass

    def openFile(self):
        # Open File Dialog
        path = QFileDialog.getOpenFileName(
            None, "Open File", os.getenv('HOME'))

        # Check If A Valid Path Is Provided
        if len(path[0]) == 0:
            path = ""
            self.file_path = ""

        else:
            self.file_path = path[0]
            path = path[0]

            # Open File + Display Contents
            file = open(path, "rt").read()

            if self.ui.actionFormatPlain.isChecked() == True:
                self.editor_text.setPlainText(file)

            elif self.ui.actionFormatMD.isChecked() == True:
                self.editor_text.setMarkdown(file)

            elif self.ui.actionFormatRich.isChecked() == True:
                self.editor_text.setHtml(file)

            else:
                self.editor_text.setPlainText(file)

            self.status_bar.showMessage(
                "Loaded: " + str(path) + " | " + str(len(file)) + " Characters")

    def saveFile(self):
        # Get Current File Path
        path = self.file_path
        if len(path) == 0:
            self.status_bar.showMessage("Nothing To Save | 0 Characters")

        else:
            # Get Text From Editor
            text = self.editor_text.toPlainText()

            # Open File + Write Contents
            file = open(path, "w")
            file.write(text)
            file.close()

            # Flash Status Bar Message
            self.status_bar.showMessage(
                "Saved: " + str(path) + " | " + str(len(text)) + " Characters")

    def undoLast(self):
        self.editor_text.undo()

    def redoLast(self):
        self.editor_text.redo()

    def exitApp(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
