
import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QKeySequence, QTextCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QMessageBox, QStatusBar, QToolBar, QInputDialog, QLineEdit,
    QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)


class FindReplaceDialog(QDialog):
    def __init__(self, editor, parent=None):
        super().__init__(parent)
        self.editor = editor
        self.setWindowTitle("Find and Replace")
        self.setMinimumWidth(350)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Find:"))
        self.find_input = QLineEdit()
        layout.addWidget(self.find_input)

        layout.addWidget(QLabel("Replace with:"))
        self.replace_input = QLineEdit()
        layout.addWidget(self.replace_input)

        buttons = QHBoxLayout()

        find_btn = QPushButton("Find Next")
        replace_btn = QPushButton("Replace")
        replace_all_btn = QPushButton("Replace All")

        find_btn.clicked.connect(self.find_next)
        replace_btn.clicked.connect(self.replace_one)
        replace_all_btn.clicked.connect(self.replace_all)

        buttons.addWidget(find_btn)
        buttons.addWidget(replace_btn)
        buttons.addWidget(replace_all_btn)
        layout.addLayout(buttons)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

    def find_next(self):
        text = self.find_input.text()
        if not text:
            return

        if not self.editor.find(text):
            self.editor.moveCursor(QTextCursor.Start)
            if not self.editor.find(text):
                self.result_label.setText("Text not found.")
                return

        self.result_label.setText("Match found.")

    def replace_one(self):
        text = self.find_input.text()
        if not text:
            return

        cursor = self.editor.textCursor()

        if cursor.hasSelection() and cursor.selectedText() == text:
            cursor.insertText(self.replace_input.text())
        elif not self.editor.find(text):
            self.result_label.setText("Text not found.")
            return
        else:
            self.editor.insertPlainText(self.replace_input.text())
            self.result_label.setText("Text replaced.")
            return

        self.result_label.setText("Text replaced.")

    def replace_all(self):
        old = self.find_input.text()
        new = self.replace_input.text()

        if not old:
            return

        content = self.editor.toPlainText()
        count = content.count(old)

        if count:
            self.editor.setPlainText(content.replace(old, new))
            self.result_label.setText(f"Replaced {count} occurrence(s).")
        else:
            self.result_label.setText("Text not found.")


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_file = None
        self.dark_mode = False
        self._loading = False

        self.setWindowTitle("Modern Text Editor")
        self.resize(1000, 700)

        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
        self.text_edit.setFont(QFont("Consolas", 12))
        self.text_edit.setTabStopDistance(4 * self.text_edit.fontMetrics().horizontalAdvance(" "))

        self.setCentralWidget(self.text_edit)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.text_edit.document().modificationChanged.connect(
            self.update_title
        )
        self.text_edit.cursorPositionChanged.connect(
            self.update_status
        )
        self.text_edit.textChanged.connect(self.update_status)

        self.create_actions()
        self.create_menus()
        self.create_toolbar()
        self.apply_theme()
        self.update_status()
        self.update_title()

    def create_actions(self):
        self.new_action = self.make_action(
            "New", self.new_file, QKeySequence.New
        )
        self.open_action = self.make_action(
            "Open...", self.open_file, QKeySequence.Open
        )
        self.save_action = self.make_action(
            "Save", self.save_file, QKeySequence.Save
        )
        self.save_as_action = self.make_action(
            "Save As...", self.save_file_as, "Ctrl+Shift+S"
        )
        self.exit_action = self.make_action(
            "Exit", self.close, "Ctrl+Q"
        )

        self.undo_action = self.make_action(
            "Undo", self.text_edit.undo, QKeySequence.Undo
        )
        self.redo_action = self.make_action(
            "Redo", self.text_edit.redo, QKeySequence.Redo
        )
        self.cut_action = self.make_action(
            "Cut", self.text_edit.cut, QKeySequence.Cut
        )
        self.copy_action = self.make_action(
            "Copy", self.text_edit.copy, QKeySequence.Copy
        )
        self.paste_action = self.make_action(
            "Paste", self.text_edit.paste, QKeySequence.Paste
        )
        self.select_all_action = self.make_action(
            "Select All", self.text_edit.selectAll, QKeySequence.SelectAll
        )
        self.find_action = self.make_action(
            "Find / Replace...", self.show_find, "Ctrl+H"
        )
        self.dark_action = self.make_action(
            "Toggle Dark Mode", self.toggle_theme, "Ctrl+D"
        )
        self.dark_action.setCheckable(True)

        self.text_edit.copyAvailable.connect(
            self.cut_action.setEnabled
        )
        self.text_edit.copyAvailable.connect(
            self.copy_action.setEnabled
        )
        self.text_edit.undoAvailable.connect(
            self.undo_action.setEnabled
        )
        self.text_edit.redoAvailable.connect(
            self.redo_action.setEnabled
        )

    def make_action(self, text, callback, shortcut=None):
        action = QAction(text, self)
        action.triggered.connect(callback)

        if shortcut:
            action.setShortcut(shortcut)

        return action

    def create_menus(self):
        bar = self.menuBar()

        file_menu = bar.addMenu("&File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addSeparator()
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu = bar.addMenu("&Edit")
        for action in (
            self.undo_action, self.redo_action
        ):
            edit_menu.addAction(action)

        edit_menu.addSeparator()

        for action in (
            self.cut_action, self.copy_action,
            self.paste_action, self.select_all_action
        ):
            edit_menu.addAction(action)

        edit_menu.addSeparator()
        edit_menu.addAction(self.find_action)

        view_menu = bar.addMenu("&View")
        view_menu.addAction(self.dark_action)

    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        for action in (
            self.new_action, self.open_action,
            self.save_action, self.save_as_action
        ):
            toolbar.addAction(action)

        toolbar.addSeparator()

        for action in (
            self.undo_action, self.redo_action,
            self.find_action
        ):
            toolbar.addAction(action)

    def update_title(self, *args):
        name = (
            Path(self.current_file).name
            if self.current_file else "Untitled"
        )
        marker = "*" if self.text_edit.document().isModified() else ""
        self.setWindowTitle(f"{marker}{name} - Modern Text Editor")

    def update_status(self, *args):
        cursor = self.text_edit.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.positionInBlock() + 1

        text = self.text_edit.toPlainText()
        words = len(text.split())

        self.status.showMessage(
            f"Line: {line}  |  Column: {column}  |  Words: {words}"
        )

    def confirm_discard(self):
        if not self.text_edit.document().isModified():
            return True

        answer = QMessageBox.question(
            self,
            "Unsaved Changes",
            "Save changes before continuing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Save
        )

        if answer == QMessageBox.Save:
            return self.save_file()
        if answer == QMessageBox.Discard:
            return True

        return False

    def new_file(self):
        if not self.confirm_discard():
            return

        self.current_file = None
        self.text_edit.clear()
        self.text_edit.document().setModified(False)
        self.update_title()

    def open_file(self):
        if not self.confirm_discard():
            return

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt *.py *.md *.json *.csv);;All Files (*)"
        )

        if not file_name:
            return

        try:
            content = Path(file_name).read_text(encoding="utf-8-sig")
            self.text_edit.setPlainText(content)
            self.current_file = file_name
            self.text_edit.document().setModified(False)
            self.update_title()
        except (OSError, UnicodeError) as error:
            QMessageBox.critical(
                self, "Open Error", f"Could not open file:\n{error}"
            )

    def save_file(self):
        if not self.current_file:
            return self.save_file_as()

        return self.write_file(self.current_file)

    def save_file_as(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            self.current_file or "untitled.txt",
            "Text Files (*.txt);;Python Files (*.py);;"
            "Markdown Files (*.md);;All Files (*)"
        )

        if not file_name:
            return False

        return self.write_file(file_name)

    def write_file(self, file_name):
        try:
            Path(file_name).write_text(
                self.text_edit.toPlainText(),
                encoding="utf-8",
                newline=""
            )
            self.current_file = file_name
            self.text_edit.document().setModified(False)
            self.update_title()
            self.status.showMessage(f"Saved: {file_name}", 3000)
            return True

        except (OSError, UnicodeError) as error:
            QMessageBox.critical(
                self, "Save Error", f"Could not save file:\n{error}"
            )
            return False

    def show_find(self):
        dialog = FindReplaceDialog(self.text_edit, self)
        dialog.exec_()

    def toggle_theme(self, checked=None):
        self.dark_mode = (
            not self.dark_mode if checked is None else checked
        )
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QMainWindow, QMenuBar, QMenu, QToolBar, QStatusBar {
                    background: #252526;
                    color: #eeeeee;
                }
                QTextEdit {
                    background: #1e1e1e;
                    color: #d4d4d4;
                    selection-background-color: #264f78;
                    border: none;
                    padding: 10px;
                }
                QMenu::item:selected {
                    background: #094771;
                }
                QToolBar {
                    spacing: 6px;
                    padding: 5px;
                    border: none;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow, QMenuBar, QMenu, QToolBar, QStatusBar {
                    background: #f4f5f7;
                    color: #202124;
                }
                QTextEdit {
                    background: #ffffff;
                    color: #202124;
                    selection-background-color: #b7d7ff;
                    border: none;
                    padding: 10px;
                }
                QMenu::item:selected {
                    background: #dceaff;
                }
                QToolBar {
                    spacing: 6px;
                    padding: 5px;
                    border: none;
                }
            """)

    def closeEvent(self, event):
        if self.confirm_discard():
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    editor = TextEditor()
    editor.show()

    sys.exit(app.exec_())
