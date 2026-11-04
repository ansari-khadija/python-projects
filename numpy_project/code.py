
import numpy as np

# Student marks: rows = students, columns = subjects

marks = np.array([
    [80, 90, 75],
    [60, 70, 85],
    [95, 88, 92],
    [40, 55, 60],
    [75, 80, 85],
    [90, 95, 98]
])

student_ids = np.array([101, 102, 103, 104, 105, 106])

print("===== STUDENT REPORT =====")

# 1. Total marks per student
total = np.sum(marks, axis=1)
print("Student totals:", total)

# 2. Average marks per student
average = np.mean(marks, axis=1)
print("Student averages:", average)

# 3. Average per subject
subject_average = np.mean(marks, axis=0)
print("Subject averages:", subject_average)

# 4. Highest marks per subject
print("Subject highest:", np.max(marks, axis=0))

# 5. Combine IDs and totals
records = np.column_stack((student_ids, total))

print("\nStudent records:")
print(records)

# 6. Select students with average >= 80
top_students = records[average >= 80]

print("\nTop students:")
print(top_students)

# 7. Split students into two groups
groups = np.array_split(records, 2)

print("\nStudent groups:")

for i, group in enumerate(groups, start=1):
    print(f"Group {i}:")
    print(group)

print("\n===== REPORT COMPLETED =====")
