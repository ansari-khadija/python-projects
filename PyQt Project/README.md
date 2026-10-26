Student Management System

A desktop-based Student Management System built using Python, PyQt5, and SQLite. This application allows users to add, view, search, update, and delete student records through a graphical user interface.

Features
Add Students: Save student name, email, and course.
View Students: Display all saved records in a table.
Search Students: Search for students by name.
Update Students: Edit existing student information.
Delete Students: Remove records with confirmation.
Data Persistence: Store records locally in an SQLite database.
Input Validation: Ensure required fields are filled in.
Error Handling: Display messages for database errors and invalid operations.
Technologies Used
Python 3
PyQt5
SQLite
sqlite3 Python module
Project Structure
text
StudentManagement/
├── main.py
├── README.md
└── students.db   # Created automatically when the application runs

Requirements
Python 3.8 or later recommended
PyQt5

SQLite is included with Python, so no separate database installation is required.

Installation
1. Clone the repository
bash
git clone <your-repository-url>


Replace <your-repository-url> with your actual Git repository URL.

2. Navigate to the project directory
bash
cd StudentManagement

3. Install dependencies
bash
python -m pip install PyQt5

4. Run the application
bash
python main.py


The application window will open, and the students.db database will be created automatically if it does not already exist.

How to Use
Launch the application.
Enter the student's name, email address, and course.
Click Add Student to save a new record.
View saved students in the table.
Enter a name in the search field to filter records.
Select a student row to load the student's details into the input fields.
Modify the details and click Update Student to save changes.
Select a student and click Delete Student to remove the record after confirmation.
Click Clear Fields to reset the form.
Database Structure

The application uses an SQLite table named students.

Column	Data Type	Description
id	INTEGER	Primary key generated automatically
name	TEXT	Student name
email	TEXT	Student email address
course	TEXT	Student course

The database stores records locally, so the information remains available after the application closes, provided the database file is retained.

CRUD Operations

The application supports the four basic database operations:

Create: Insert a new student record.
Read: Retrieve and display student records.
Update: Modify an existing student record.
Delete: Remove a student record.
Learning Objectives

This project demonstrates:

Building desktop GUIs with PyQt5.
Using layouts, buttons, labels, and text inputs.
Displaying tabular data with QTableWidget.
Connecting button signals to Python methods.
Connecting Python applications to SQLite.
Executing parameterized SQL queries.
Implementing CRUD operations.
Handling user input and database errors.
Future Enhancements
Email format validation.
Duplicate student checks.
Course selection with QComboBox.
Student profile photos using QPixmap.
CSV export and import.
Improved styling and responsive layouts.
User authentication and access control.
License

This project is intended for learning and educational purposes. Add a license file if you plan to distribute it publicly.

Author

KHADJIA__ANSARI

A Python GUI project demonstrating student record management using PyQt5 and SQLite.