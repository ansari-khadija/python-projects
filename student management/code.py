
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ==========================================
# 1. COLORS
# ==========================================
BG = "#F7F3FF"
CARD = "#FFFFFF"
PURPLE = "#6C4AB6"
DARK_PURPLE = "#39245F"
LIGHT_PURPLE = "#E9E3F5"
TEXT = "#33264D"
MUTED = "#756A8A"
BORDER = "#D8CDEE"
RED = "#B85C79"
GREEN = "#478568"

# ==========================================
# 2. DATABASE
# ==========================================
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
""")
conn.commit()


# ==========================================
# 3. MAIN WINDOW
# ==========================================
root = Tk()
root.title("Student Management System")
root.geometry("1000x720")
root.minsize(850, 650)
root.configure(bg=BG)


# ==========================================
# 4. FUNCTIONS
# ==========================================
def clear_fields():
    student_id.delete(0, END)
    student_name.delete(0, END)
    student_age.delete(0, END)
    student_course.delete(0, END)

    student_id.config(state="normal")
    student_id.focus_set()

    for item in tree.selection():
        tree.selection_remove(item)


def validate_fields():
    sid = student_id.get().strip()
    name = student_name.get().strip()
    age = student_age.get().strip()
    course = student_course.get().strip()

    if not sid or not name or not age or not course:
        messagebox.showwarning(
            "Missing Information",
            "Please fill in all student details."
        )
        return None

    if not age.isdigit() or not 1 <= int(age) <= 120:
        messagebox.showwarning(
            "Invalid Age",
            "Please enter an age between 1 and 120."
        )
        return None

    return sid, name, int(age), course


def load_students(search_text=""):
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("""
        SELECT student_id, name, age, course
        FROM students
        WHERE student_id LIKE ?
           OR name LIKE ?
           OR course LIKE ?
        ORDER BY student_id
    """, (
        f"%{search_text}%",
        f"%{search_text}%",
        f"%{search_text}%"
    ))

    for row in cursor.fetchall():
        tree.insert("", END, values=row)

    total_label.config(
        text=f"Total Students: {get_total_students()}"
    )


def get_total_students():
    cursor.execute("SELECT COUNT(*) FROM students")
    return cursor.fetchone()[0]


def add_student():
    data = validate_fields()
    if not data:
        return

    try:
        cursor.execute("""
            INSERT INTO students (student_id, name, age, course)
            VALUES (?, ?, ?, ?)
        """, data)

        conn.commit()
        load_students()
        clear_fields()

        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Duplicate ID",
            "This Student ID already exists."
        )


def select_student(event=None):
    selected = tree.selection()

    if not selected:
        return

    values = tree.item(selected[0], "values")

    clear_fields()

    student_id.insert(0, values[0])
    student_name.insert(0, values[1])
    student_age.insert(0, values[2])
    student_course.insert(0, values[3])


def update_student():
    data = validate_fields()
    if not data:
        return

    sid, name, age, course = data

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (sid,)
    )

    if not cursor.fetchone():
        messagebox.showwarning(
            "Not Found",
            "Select an existing student to update."
        )
        return

    if not messagebox.askyesno(
        "Confirm Update",
        "Are you sure you want to update this student?"
    ):
        return

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, course = ?
        WHERE student_id = ?
    """, (name, age, course, sid))

    conn.commit()
    load_students()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Student updated successfully!"
    )


def delete_student():
    sid = student_id.get().strip()

    if not sid:
        messagebox.showwarning(
            "Selection Required",
            "Select a student from the table first."
        )
        return

    cursor.execute(
        "SELECT student_id FROM students WHERE student_id = ?",
        (sid,)
    )

    if not cursor.fetchone():
        messagebox.showwarning(
            "Not Found",
            "This Student ID does not exist."
        )
        return

    if messagebox.askyesno(
        "Confirm Delete",
        f"Delete student with ID {sid}?"
    ):
        cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (sid,)
        )
        conn.commit()
        load_students()
        clear_fields()

        messagebox.showinfo(
            "Success",
            "Student deleted successfully!"
        )


def search_student():
    query = search_entry.get().strip()
    load_students(query)


def show_all_students():
    search_entry.delete(0, END)
    load_students()


def close_application():
    conn.close()
    root.destroy()


# ==========================================
# 5. HEADER
# ==========================================
header = Frame(root, bg=DARK_PURPLE, height=100)
header.pack(fill="x")
header.pack_propagate(False)

Label(
    header,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold"),
    bg=DARK_PURPLE,
    fg="white"
).pack(pady=(16, 4))

Label(
    header,
    text="Manage your student records easily",
    font=("Arial", 11),
    bg=DARK_PURPLE,
    fg="#DED3F7"
).pack()


# ==========================================
# 6. MAIN CONTENT
# ==========================================
main = Frame(root, bg=BG)
main.pack(fill="both", expand=True, padx=22, pady=12)


# ==========================================
# 7. STUDENT DETAILS
# ==========================================
details_frame = LabelFrame(
    main,
    text=" STUDENT DETAILS ",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=PURPLE,
    padx=12,
    pady=10
)
details_frame.pack(fill="x", pady=(0, 10))


def create_field(parent, label_text, row, column):
    Label(
        parent,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg=CARD,
        fg=TEXT
    ).grid(
        row=row * 2,
        column=column,
        sticky="w",
        padx=8,
        pady=(4, 3)
    )

    entry = Entry(
        parent,
        font=("Arial", 11),
        bg="#FCFAFF",
        fg=TEXT,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground=BORDER,
        highlightcolor=PURPLE
    )

    entry.grid(
        row=row * 2 + 1,
        column=column,
        sticky="ew",
        padx=8,
        ipady=5,
        pady=(0, 5)
    )

    return entry


student_id = create_field(
    details_frame, "Student ID", 0, 0
)
student_name = create_field(
    details_frame, "Full Name", 0, 1
)
student_age = create_field(
    details_frame, "Age", 1, 0
)
student_course = create_field(
    details_frame, "Course", 1, 1
)

details_frame.grid_columnconfigure(0, weight=1)
details_frame.grid_columnconfigure(1, weight=1)


# ==========================================
# 8. BUTTONS
# ==========================================
button_frame = Frame(main, bg=BG)
button_frame.pack(fill="x", pady=(0, 12))


def create_button(parent, text, command, color):
    return Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg=color,
        fg="white",
        activebackground=DARK_PURPLE,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=14,
        pady=8
    )


create_button(
    button_frame, "Add Student", add_student, PURPLE
).pack(side="left", padx=(0, 8))

create_button(
    button_frame, "Update", update_student, GREEN
).pack(side="left", padx=(0, 8))

create_button(
    button_frame, "Delete", delete_student, RED
).pack(side="left", padx=(0, 8))

create_button(
    button_frame, "Clear", clear_fields, MUTED
).pack(side="left")


# ==========================================
# 9. SEARCH BAR
# ==========================================
search_frame = Frame(main, bg=BG)
search_frame.pack(fill="x", pady=(0, 10))

Label(
    search_frame,
    text="Search:",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg=TEXT
).pack(side="left", padx=(0, 8))

search_entry = Entry(
    search_frame,
    font=("Arial", 11),
    bg=CARD,
    fg=TEXT,
    relief="solid",
    bd=1
)
search_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=5,
    padx=(0, 8)
)

create_button(
    search_frame, "Search", search_student, PURPLE
).pack(side="left", padx=(0, 8))

create_button(
    search_frame, "Show All", show_all_students, MUTED
).pack(side="left")

search_entry.bind("<Return>", lambda event: search_student())


# ==========================================
# 10. STUDENT TABLE
# ==========================================
table_frame = Frame(
    main,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)
table_frame.pack(fill="both", expand=True)

columns = ("student_id", "name", "age", "course")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    selectmode="browse"
)

tree.heading("student_id", text="Student ID")
tree.heading("name", text="Full Name")
tree.heading("age", text="Age")
tree.heading("course", text="Course")

tree.column("student_id", width=140, anchor="center")
tree.column("name", width=280, anchor="w")
tree.column("age", width=90, anchor="center")
tree.column("course", width=220, anchor="w")

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(6, 0),
    pady=6
)
scrollbar.pack(side="right", fill="y", pady=6, padx=(0, 6))


# ==========================================
# 11. TABLE STYLE
# ==========================================
style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background=CARD,
    foreground=TEXT,
    fieldbackground=CARD,
    rowheight=30,
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    background=LIGHT_PURPLE,
    foreground=DARK_PURPLE,
    font=("Arial", 10, "bold"),
    padding=8
)

style.map(
    "Treeview",
    background=[("selected", PURPLE)],
    foreground=[("selected", "white")]
)

tree.bind("<<TreeviewSelect>>", select_student)


# ==========================================
# 12. FOOTER
# ==========================================
footer = Frame(main, bg=BG)
footer.pack(fill="x", pady=(8, 0))

total_label = Label(
    footer,
    text="Total Students: 0",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=PURPLE
)
total_label.pack(side="left")

Label(
    footer,
    text="Student Records Database",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
).pack(side="right")


# ==========================================
# 13. START APPLICATION
# ==========================================
load_students()
student_id.focus_set()

root.protocol("WM_DELETE_WINDOW", close_application)
root.mainloop()
