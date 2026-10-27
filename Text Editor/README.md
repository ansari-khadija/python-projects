Modern Text Editor

A simple, modern desktop text editor built with Python and PyQt5. It provides an easy-to-use graphical interface for creating, opening, editing, and saving text files, along with useful editing tools and a dark mode.

Features
File Management
Create new documents
Open existing files
Save files and use Save As
Support for .txt, .py, .md, .json, and .csv files
UTF-8 text encoding support
Editing Tools
Undo and redo
Cut, copy, and paste
Select all text
Find and replace text
User Interface
Modern graphical interface
Light and dark themes
Toolbar and menu bar
Status bar displaying the current line, column, and word count
Keyboard Shortcuts
Convenient shortcuts for common operations
Unsaved Changes Protection
Prompts users to save, discard, or cancel before closing or replacing modified documents
Technologies Used
Python 3
PyQt5
pathlib for file handling
Qt Widgets for the graphical user interface
Requirements
Python 3.8 or newer recommended
PyQt5
Installation
1. Clone the repository
bash
git clone https://github.com/your-username/modern-text-editor.git


Replace your-username and modern-text-editor with your actual GitHub username and repository name.

2. Navigate to the project directory
bash
cd modern-text-editor

3. Install dependencies
bash
python -m pip install PyQt5

4. Run the application
bash
python text_editor.py

Keyboard Shortcuts
Shortcut	Description
Ctrl + N	Create a new document
Ctrl + O	Open a file
Ctrl + S	Save the current file
Ctrl + Shift + S	Save As
Ctrl + Z	Undo
Ctrl + Y	Redo
Ctrl + X	Cut selected text
Ctrl + C	Copy selected text
Ctrl + V	Paste text
Ctrl + A	Select all text
Ctrl + H	Open Find and Replace
Ctrl + D	Toggle dark mode
Ctrl + Q	Exit the application
Project Structure
text
modern-text-editor/
├── text_editor.py
├── README.md
└── requirements.txt


Create a requirements.txt file containing:

text
PyQt5

Usage
Launch the application.
Select File → New to create a document or File → Open to load an existing file.
Type and edit text in the main editor.
Use the Edit menu or keyboard shortcuts to modify text.
Open Edit → Find / Replace to search for and replace text.
Select View → Toggle Dark Mode to switch the editor theme.
Save your work using File → Save or File → Save As.
Error Handling

The application displays error messages when files cannot be opened or saved. It also warns users about unsaved changes before closing the application or opening another document.

Future Improvements

Potential enhancements include:

Line numbers
Python syntax highlighting
Multiple document tabs
Auto-save functionality
Recent files menu
Customizable fonts and font sizes
Word wrap controls
Export to PDF
Find next and find previous navigation
Contributing

Contributions, suggestions, and bug reports are welcome.

Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request.
License

This project is available under the MIT License. If you choose this license, add a LICENSE file containing the MIT License text.

Author
KHADIJA__ANSARI

GitHub: ansari-khadija

Built with ❤️ using Python and PyQt5.