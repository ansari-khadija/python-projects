
import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)


class StudentManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Management System")
        self.setMinimumSize(850, 600)

        # Connect to SQLite database
        self.connection = sqlite3.connect("students.db")
        self.cursor = self.connection.cursor()

        self.create_table()
        self.selected_student_id = None

        self.create_ui()
        self.load_students()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                course TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Heading
        title = QLabel("Student Management System")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 12px;
        """)

        # Input fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter student name")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter email address")

        self.course_input = QLineEdit()
        self.course_input.setPlaceholderText("Enter course name")

        form = QFormLayout()
        form.addRow("Name:", self.name_input)
        form.addRow("Email:", self.email_input)
        form.addRow("Course:", self.course_input)

        # Action buttons
        self.add_button = QPushButton("Add Student")
        self.update_button = QPushButton("Update Student")
        self.delete_button = QPushButton("Delete Student")
        self.clear_button = QPushButton("Clear Fields")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.clear_button)

        # Search field
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search students by name..."
        )

        # Student table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Email", "Course"
        ])
        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )
        self.table.setSelectionMode(
            QTableWidget.SingleSelection
        )
        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addLayout(form)
        layout.addLayout(button_layout)
        layout.addWidget(QLabel("Search Students:"))
        layout.addWidget(self.search_input)
        layout.addWidget(self.table)

        central_widget.setLayout(layout)

        # Connect buttons to methods
        self.add_button.clicked.connect(self.add_student)
        self.update_button.clicked.connect(self.update_student)
        self.delete_button.clicked.connect(self.delete_student)
        self.clear_button.clicked.connect(self.clear_fields)

        self.search_input.textChanged.connect(
            self.search_students
        )
        self.table.itemSelectionChanged.connect(
            self.select_student
        )

    def add_student(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        course = self.course_input.text().strip()

        if not name or not email or not course:
            QMessageBox.warning(
                self,
                "Missing Information",
                "Please fill in all fields."
            )
            return

        try:
            self.cursor.execute("""
                INSERT INTO students (name, email, course)
                VALUES (?, ?, ?)
            """, (name, email, course))

            self.connection.commit()

            QMessageBox.information(
                self, "Success",
                "Student added successfully."
            )

            self.clear_fields()
            self.load_students()

        except sqlite3.Error as error:
            QMessageBox.critical(
                self, "Database Error", str(error)
            )

    def load_students(self, search_text=""):
        try:
            if search_text:
                self.cursor.execute("""
                    SELECT id, name, email, course
                    FROM students
                    WHERE name LIKE ?
                    ORDER BY id DESC
                """, (f"%{search_text}%",))
            else:
                self.cursor.execute("""
                    SELECT id, name, email, course
                    FROM students
                    ORDER BY id DESC
                """)

            records = self.cursor.fetchall()

            self.table.setRowCount(0)

            for record in records:
                row = self.table.rowCount()
                self.table.insertRow(row)

                for column, value in enumerate(record):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row, column, item)

        except sqlite3.Error as error:
            QMessageBox.critical(
                self, "Database Error", str(error)
            )

    def search_students(self, text):
        self.load_students(text.strip())

    def select_student(self):
        row = self.table.currentRow()

        if row < 0:
            return

        id_item = self.table.item(row, 0)
        name_item = self.table.item(row, 1)
        email_item = self.table.item(row, 2)
        course_item = self.table.item(row, 3)

        if not all([
            id_item, name_item, email_item, course_item
        ]):
            return

        self.selected_student_id = int(id_item.text())
        self.name_input.setText(name_item.text())
        self.email_input.setText(email_item.text())
        self.course_input.setText(course_item.text())

    def update_student(self):
        if self.selected_student_id is None:
            QMessageBox.warning(
                self, "No Selection",
                "Select a student from the table first."
            )
            return

        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        course = self.course_input.text().strip()

        if not name or not email or not course:
            QMessageBox.warning(
                self, "Missing Information",
                "Please fill in all fields."
            )
            return

        try:
            self.cursor.execute("""
                UPDATE students
                SET name = ?, email = ?, course = ?
                WHERE id = ?
            """, (
                name, email, course,
                self.selected_student_id
            ))

            self.connection.commit()

            QMessageBox.information(
                self, "Success",
                "Student updated successfully."
            )

            self.clear_fields()
            self.load_students()

        except sqlite3.Error as error:
            QMessageBox.critical(
                self, "Database Error", str(error)
            )

    def delete_student(self):
        if self.selected_student_id is None:
            QMessageBox.warning(
                self, "No Selection",
                "Select a student to delete."
            )
            return

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this student?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        try:
            self.cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (self.selected_student_id,)
            )
            self.connection.commit()

            QMessageBox.information(
                self, "Deleted",
                "Student deleted successfully."
            )

            self.clear_fields()
            self.load_students()

        except sqlite3.Error as error:
            QMessageBox.critical(
                self, "Database Error", str(error)
            )

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.course_input.clear()

        self.selected_student_id = None
        self.table.clearSelection()

    def closeEvent(self, event):
        self.connection.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = StudentManagementSystem()
    window.show()

    sys.exit(app.exec_())
