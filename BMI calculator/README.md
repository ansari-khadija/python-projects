🧮 BMI Calculator with Ideal Weight Recommendation
📌 About the Project

The BMI Calculator with Ideal Weight Recommendation is a beginner-friendly Python project that calculates a person's Body Mass Index (BMI) using their weight and height.

The application also estimates a healthy weight range based on standard adult BMI guidelines and compares the user's current weight with that range.

✨ Features
⚖️ Calculates Body Mass Index (BMI).
📏 Accepts weight in kilograms and height in centimeters.
📊 Displays the BMI category.
🎯 Estimates a healthy weight range based on height.
🔍 Compares current weight with the estimated range.
✅ Handles invalid input and non-positive measurements.
💻 Simple, interactive command-line interface.
🛠️ Technologies Used
Python 3
Functions
Conditional statements (if, elif, else)
Exception handling (try and except)
Mathematical calculations and formatted output
📂 Project Structure
BMI-Calculator/
├── bmi_calculator.py
└── README.md

🚀 How to Run
Install Python 3 on your computer.
Download or clone this repository.
Open a terminal in the project folder.
Run the following command:
python bmi_calculator.py

Enter your weight in kilograms and height in centimeters.
View your BMI result, category, and estimated healthy weight range.
🧮 BMI Formula

Body Mass Index is calculated using the following formula:

BMI = Weight (kg) / Height (m)²

Example

Suppose a person weighs 65 kg and is 170 cm tall.

Weight: 65 kg
Height: 1.70 m
BMI: 65 / (1.70 × 1.70) = 22.49
📊 Adult BMI Categories
BMI Range	Category
Below 18.5	Underweight
18.5 to below 25	Healthy weight
25 to below 30	Overweight
30 and above	Obesity

These are general adult screening categories, not a diagnosis.

🎯 Ideal Weight Recommendation

Instead of recommending one exact ideal weight, this project calculates an estimated healthy weight range using the adult BMI range of 18.5 to 24.9.

Lower end of range:

18.5 × height (m)²

Upper end of range:

24.9 × height (m)²

For a height of 170 cm, the estimated range is approximately 53.5 kg to 72.0 kg.

The appropriate weight for an individual may vary depending on age, muscle mass, body composition, and other factors. These estimates are intended for adults.

💻 Example Output
========================================
      BMI & IDEAL WEIGHT CALCULATOR
========================================
Enter your weight in kg: 65
Enter your height in cm: 170

--------- YOUR RESULTS ---------
Your weight       : 65.0 kg
Your height       : 170.0 cm
Your BMI          : 22.49
BMI category      : Healthy weight

--- ESTIMATED HEALTHY WEIGHT RANGE ---
Lower end         : 53.5 kg
Upper end         : 72.0 kg
Estimated range   : 53.5 - 72.0 kg

Your weight is within the general adult BMI range.

📚 What I Learned
Writing and using Python functions.
Taking input from users.
Converting centimeters into meters.
Performing mathematical calculations.
Using conditional statements.
Handling invalid inputs with exception handling.
Formatting output using f-strings.
Applying basic programming concepts to a practical problem.
🔮 Future Improvements
Add support for pounds, feet, and inches.
Create a graphical user interface using Tkinter.
Display BMI results using charts.
Save previous BMI calculations.
Add a BMI history feature.
Generate downloadable result reports.
🏷️ Hashtags

#Python #BMICalculator #IdealWeight #PythonProjects #BeginnerProject #LearnPython #Coding #Programming #HealthCalculator

📄 License

This project is available for educational and personal use.