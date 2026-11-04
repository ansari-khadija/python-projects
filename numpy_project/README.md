NumPy Student Performance Analyzer

A beginner-to-intermediate Python project built using NumPy to analyze student marks, calculate performance statistics, identify top-performing students, and divide students into groups.

📌 Project Overview

The NumPy Student Performance Analyzer processes student marks across multiple subjects using NumPy arrays.

It demonstrates how NumPy can perform numerical calculations, data filtering, array manipulation, and statistical analysis efficiently.

🚀 Features
Store student marks using NumPy arrays.
Calculate total marks for each student.
Calculate average marks for each student.
Calculate average marks for each subject.
Find the highest marks in each subject.
Combine student IDs and marks using column_stack().
Identify top-performing students using Boolean indexing.
Divide student records into groups using array_split().
🛠️ Technologies Used
Python 3
NumPy
📂 Project Structure
text
numpy-student-analyzer/
│
├── main.py
├── README.md
└── requirements.txt

⚙️ Installation
1. Clone the repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate into the project
bash
cd numpy-student-analyzer

3. Install NumPy
bash
pip install numpy


Or install dependencies using:

bash
pip install -r requirements.txt

▶️ Run the Project
bash
python main.py

📊 Example Dataset

The project uses six students and three subjects.

Student ID	Subject 1	Subject 2	Subject 3
101	80	90	75
102	60	70	85
103	95	88	92
104	40	55	60
105	75	80	85
106	90	95	98
🧠 NumPy Concepts Practiced
NumPy Concept	Function
Array creation	np.array()
Sum	np.sum()
Average	np.mean()
Maximum	np.max()
Array joining	np.column_stack()
Array splitting	np.array_split()
Boolean filtering	records[condition]
Axis operations	axis=0, axis=1
📈 Example Output
text
===== STUDENT REPORT =====

Student totals: [245 215 275 155 240 283]

Student averages:
[81.67 71.67 91.67 51.67 80.00 94.33]

Subject averages:
[73.33 79.67 82.50]

Subject highest:
[95 95 98]

Top students:
[[103 275]
 [106 283]]

===== REPORT COMPLETED =====

🎯 Learning Objectives

Through this project, I practised:

Working with multidimensional NumPy arrays.
Performing mathematical and statistical operations.
Understanding row-wise and column-wise calculations.
Filtering records using Boolean indexing.
Combining and splitting numerical datasets.
Applying NumPy concepts to a practical problem.
🔮 Future Improvements
Add student names.
Add subject names.
Calculate grades automatically.
Identify the overall class topper.
Export student reports to CSV.
Build a REST API using FastAPI.
Connect the application to PostgreSQL.
👨‍💻 Author

Python & Full-Stack Development Learner

This project is part of my journey to learn Python, NumPy, backend development, and full-stack programming.

📄 License

This project is open-source and available for educational purposes.