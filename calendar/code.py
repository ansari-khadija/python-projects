
import tkinter as tk
import calendar
from datetime import date

# Pastel vintage color palette
CREAM = "#FFF8EF"
DUSTY_PINK = "#D8A7A7"
DARK_BROWN = "#6B4F4F"
SAGE_GREEN = "#A8B5A0"
PALE_PINK = "#F5E6E0"
WHITE = "#FFFFFF"

root = tk.Tk()
root.title("Vintage Calendar")
root.geometry("560x500")
root.configure(bg=CREAM)
root.resizable(False, False)

today = date.today()
current_year = today.year
current_month = today.month

# Heading
tk.Label(
    root,
    text="~ My Little Calendar ~",
    font=("Georgia", 22, "italic"),
    bg=CREAM,
    fg=DARK_BROWN
).pack(pady=(18, 5))

tk.Label(
    root,
    text="✿  ─────────────────────  ✿",
    font=("Georgia", 12),
    bg=CREAM,
    fg=DUSTY_PINK
).pack()

# Month and year
month_label = tk.Label(
    root,
    font=("Georgia", 18, "bold"),
    bg=CREAM,
    fg=DARK_BROWN
)
month_label.pack(pady=12)

calendar_frame = tk.Frame(
    root,
    bg=PALE_PINK,
    highlightbackground=DUSTY_PINK,
    highlightthickness=2
)
calendar_frame.pack(padx=20, pady=5)

def show_calendar(year, month):
    global current_year, current_month
    current_year, current_month = year, month

    for widget in calendar_frame.winfo_children():
        widget.destroy()

    month_label.config(
        text=f"{calendar.month_name[month]} {year}"
    )

    # Weekday headings
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for col, day_name in enumerate(weekdays):
        tk.Label(
            calendar_frame,
            text=day_name,
            width=7,
            font=("Georgia", 10, "bold"),
            bg=DUSTY_PINK,
            fg=WHITE,
            pady=8
        ).grid(row=0, column=col, padx=2, pady=2)

    # Calendar dates
    weeks = calendar.monthcalendar(year, month)

    for row, week in enumerate(weeks, start=1):
        for col, day in enumerate(week):
            bg_color = PALE_PINK
            fg_color = DARK_BROWN

            if day == 0:
                text = ""
            else:
                text = str(day)

                if (year, month, day) == (
                    today.year, today.month, today.day
                ):
                    bg_color = SAGE_GREEN
                    fg_color = WHITE

            tk.Label(
                calendar_frame,
                text=text,
                width=7,
                height=2,
                font=("Georgia", 10),
                bg=bg_color,
                fg=fg_color,
                relief="flat"
            ).grid(row=row, column=col, padx=2, pady=2)

def previous_month():
    year = current_year
    month = current_month - 1

    if month < 1:
        month = 12
        year -= 1

    show_calendar(year, month)

def next_month():
    year = current_year
    month = current_month + 1

    if month > 12:
        month = 1
        year += 1

    show_calendar(year, month)

# Navigation buttons
button_frame = tk.Frame(root, bg=CREAM)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="❮ Previous",
    command=previous_month,
    font=("Georgia", 10),
    bg=PALE_PINK,
    fg=DARK_BROWN,
    activebackground=DUSTY_PINK,
    relief="flat",
    padx=12,
    pady=7,
    cursor="hand2"
).grid(row=0, column=0, padx=12)

tk.Button(
    button_frame,
    text="Next ❯",
    command=next_month,
    font=("Georgia", 10),
    bg=PALE_PINK,
    fg=DARK_BROWN,
    activebackground=DUSTY_PINK,
    relief="flat",
    padx=12,
    pady=7,
    cursor="hand2"
).grid(row=0, column=1, padx=12)

# Footer
tk.Label(
    root,
    text="made with love  ♡",
    font=("Georgia", 11, "italic"),
    bg=CREAM,
    fg=DUSTY_PINK
).pack(pady=3)

show_calendar(current_year, current_month)

root.mainloop()
