👤 Personal Profile Checker

A simple, interactive Python project that collects user information, validates inputs, and generates a personalized profile summary. This project demonstrates essential Python concepts, including variables, data types, collections, conditional statements, and error handling.

✨ Features
📝 User Input — Collects name, age, city, hobbies, and newsletter preferences.
✅ Input Validation — Checks age limits and validates user responses.
🎂 Age Eligibility — Determines whether the user is an adult and meets the minimum driving age.
🎨 Hobby Management — Stores hobbies in a list and identifies unique hobbies using a set.
📍 Location Tracking — Groups city and age into a tuple.
📚 Profile Storage — Organizes user information in a dictionary.
🔍 Data Type Inspection — Displays the Python data type of each profile field.
🖥️ Formatted Output — Presents a clear and organized profile summary.
🛠️ Technologies Used
Language: Python 3
Concepts: Variables, strings, integers, booleans, lists, tuples, sets, dictionaries, loops, conditionals, and exception handling.
🚀 Getting Started
Prerequisites

Install Python 3 on your computer.

Installation
Clone the repository:
   git clone https://github.com/ansari-khadija/personal-profile-checker.git

Navigate to the project folder:
   cd personal-profile-checker

Run the program:
   python main.py


If your system uses Python 3 through python3, run:

   python3 main.py


Replace main.py with your actual Python filename if necessary.

💻 Example Output
========================================
   PERSONAL PROFILE CHECKER
========================================
Enter your name: Alex
Enter your city: Mumbai
Enter your age: 22
Subscribe to newsletter? (yes/no): yes
Enter your hobbies separated by commas: coding, music, reading, coding

========================================
         PROFILE SUMMARY
========================================
Name: Alex
Age: 22
City: Mumbai
Adult: True
Driving age eligible: True
Newsletter: True
Hobbies: ['coding', 'music', 'reading', 'coding']
Unique hobbies: {'coding', 'music', 'reading'}
Location tuple: ('Mumbai', 22)

--- Data Types ---
name : str
age : int
city : str
newsletter : bool
hobbies : list

Profile created successfully!


Note: The order of items in the unique hobbies set may vary.

🧠 Python Concepts Demonstrated
Concept	Purpose
String (str)	Stores the user's name and city
Integer (int)	Stores the user's age
Boolean (bool)	Represents newsletter subscription and eligibility
List (list)	Stores the user's hobbies
Tuple (tuple)	Groups the city and age
Set (set)	Identifies unique hobbies
Dictionary (dict)	Organizes profile information using key-value pairs
if statements	Validates inputs and checks eligibility
try-except	Handles invalid age input
for loop	Displays the data types of profile fields
🎯 Project Goals

This project is designed to help beginners:

Understand Python's fundamental data types.
Practice collecting and processing user input.
Learn basic input validation and error handling.
Work with Python's built-in collection types.
Build confidence by creating a practical, interactive application.
🔮 Future Improvements
📧 Add email address validation.
💾 Save profile information to a file or database.
🎨 Improve the terminal interface with colors.
🔄 Allow users to edit their profiles.
🧪 Add automated tests for input validation.
🖼️ Build a graphical user interface.
🤝 Contributing

Contributions, suggestions, and improvements are welcome!

Fork this repository.
Create a new branch.
Make your changes.
Submit a pull request.
📄 License

This project is open source. You may add an MIT License to the repository if you want others to use and modify it under those terms.

⭐ If you find this project helpful, consider giving the repository a star!

Made with ❤️ and Python 🐍