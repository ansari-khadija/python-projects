
# ==========================================
# STUDENT PERFORMANCE ANALYSIS PROJECT
# ==========================================

# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")

# 2. Get Current Folder

folder = os.path.dirname(os.path.abspath(__file__))

# 3. Load Dataset

file_path = os.path.join(
    folder,
    "student_performance.csv"
)

df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")

print(df.head())

# 4. Data Cleaning

df.drop_duplicates(inplace=True)

subjects = ["Math", "Science", "English"]

df[subjects] = df[subjects].fillna(
    df[subjects].mean()
)

df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

# 5. Calculate Average Marks

df["Average"] = df[subjects].mean(axis=1)

# 6. Calculate Result

df["Result"] = np.where(
    df["Average"] >= 40,
    "Pass",
    "Fail"
)

# 7. Calculate KPIs

total_students = len(df)

average_marks = df["Average"].mean()

highest_marks = df["Average"].max()

total_pass = (df["Result"] == "Pass").sum()

total_fail = (df["Result"] == "Fail").sum()

pass_percentage = (
    total_pass / total_students
) * 100

# 8. Display KPI Cards

print("\n========== STUDENT KPIs ==========")

print("Total Students:", total_students)

print("Average Marks:", round(average_marks, 2))

print("Highest Marks:", highest_marks)

print("Total Pass:", total_pass)

print("Total Fail:", total_fail)

print("Pass Percentage:", round(pass_percentage, 2), "%")

# 9. Create Output Folder

output_folder = os.path.join(folder, "output")

os.makedirs(output_folder, exist_ok=True)

# 10. Create Dashboard

fig, ax = plt.subplots(4, 2, figsize=(16, 22))

# Chart 1: Subject-wise Bar Chart

subject_avg = df[subjects].mean()

sns.barplot(
    x=subject_avg.index,
    y=subject_avg.values,
    color="skyblue",
    ax=ax[0, 0]
)

ax[0, 0].set_title("Subject-wise Average Marks")

ax[0, 0].set_xlabel("Subjects")

ax[0, 0].set_ylabel("Average Marks")

# Chart 2: Student Ranking Chart

top_students = df.sort_values(
    by="Average",
    ascending=False
).head(10)

sns.barplot(
    data=top_students,
    x="Average",
    y="Student_ID",
    color="green",
    ax=ax[0, 1]
)

ax[0, 1].set_title("Top 10 Student Ranking")

# Chart 3: Marks Distribution Histogram

sns.histplot(
    df["Average"],
    bins=15,
    kde=True,
    color="orange",
    ax=ax[1, 0]
)

ax[1, 0].set_title("Marks Distribution")

ax[1, 0].set_xlabel("Average Marks")

# Chart 4: Subject Correlation Heatmap

correlation = df[subjects].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    ax=ax[1, 1]
)

ax[1, 1].set_title("Subject Correlation Heatmap")

# Chart 5: Gender-wise Performance

sns.barplot(
    data=df,
    x="Gender",
    y="Average",
    hue="Gender",
    palette="pastel",
    legend=False,
    ax=ax[2, 0]
)

ax[2, 0].set_title("Gender-wise Performance")

# Chart 6: Attendance vs Marks Scatter Plot

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Average",
    hue="Gender",
    alpha=0.7,
    ax=ax[2, 1]
)

ax[2, 1].set_title("Attendance vs Marks")

ax[2, 1].set_xlabel("Attendance (%)")

ax[2, 1].set_ylabel("Average Marks")

# Chart 7: Pass vs Fail Donut Chart

result_count = df["Result"].value_counts()

ax[3, 0].pie(
    result_count,
    labels=result_count.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["green", "red"],
    wedgeprops={"width": 0.4}
)

ax[3, 0].set_title("Pass vs Fail Distribution")

# Chart 8: Subject-wise Box Plot

sns.boxplot(
    data=df[subjects],
    palette="Set2",
    ax=ax[3, 1]
)

ax[3, 1].set_title("Subject-wise Box Plot")

ax[3, 1].set_ylabel("Marks")

# 11. Dashboard Title

plt.suptitle(
    "STUDENT PERFORMANCE ANALYTICS DASHBOARD",
    fontsize=20,
    fontweight="bold"
)

plt.tight_layout()

# 12. Save Dashboard

dashboard_path = os.path.join(
    output_folder,
    "student_dashboard.png"
)

plt.savefig(
    dashboard_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# 13. Top 10 Students

print("\n========== TOP 10 STUDENTS ==========")

print(
    top_students[
        ["Student_ID", "Gender", "Average", "Result"]
    ]
)

# 14. Subject Performance

print("\n========== SUBJECT PERFORMANCE ==========")

print(subject_avg)

print(
    "Best Subject:",
    subject_avg.idxmax()
)

print(
    "Lowest Performing Subject:",
    subject_avg.idxmin()
)

# 15. Gender Performance

print("\n========== GENDER PERFORMANCE ==========")

print(
    df.groupby("Gender")["Average"].mean()
)

# 16. Attendance Analysis

print("\n========== ATTENDANCE ANALYSIS ==========")

print(
    "Average Attendance:",
    round(df["Attendance"].mean(), 2), "%"
)

# 17. Save Cleaned Dataset

cleaned_path = os.path.join(
    output_folder,
    "cleaned_student_data.csv"
)

df.to_csv(cleaned_path, index=False)

# 18. Final Message

print("\n====================================")

print("STUDENT PERFORMANCE PROJECT COMPLETED!")

print("Dashboard Saved:", dashboard_path)

print("Cleaned Dataset Saved:", cleaned_path)

print("====================================")
