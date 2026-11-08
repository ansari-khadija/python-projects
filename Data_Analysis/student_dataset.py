
import pandas as pd
import numpy as np
import os

# Random data
np.random.seed(42)

# Total students
n = 1000

# Student details
genders = ["Male", "Female"]

students = [
    f"STU{i:04d}" for i in range(1, n + 1)
]

# Generate student dataset
df = pd.DataFrame({

    "Student_ID": students,

    "Gender": np.random.choice(
        genders, n
    ),

    "Math": np.random.randint(20, 101, n),

    "Science": np.random.randint(20, 101, n),

    "English": np.random.randint(20, 101, n),

    "Attendance": np.random.randint(40, 101, n)

})

# Calculate average marks
df["Average"] = df[
    ["Math", "Science", "English"]
].mean(axis=1).round(2)

# Calculate result
df["Result"] = np.where(
    df["Average"] >= 40,
    "Pass",
    "Fail"
)

# Save CSV in the same folder
folder = os.path.dirname(
    os.path.abspath(__file__)
)

file_path = os.path.join(
    folder,
    "student_performance.csv"
)

df.to_csv(file_path, index=False)

print("SUCCESS! Student Dataset Created.")

print("File Location:", file_path)

print("Total Students:", len(df))

print("\nDataset Preview:")

print(df.head())

print("\nDataset Information:")

print(df.info())
