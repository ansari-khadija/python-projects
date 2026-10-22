
import tkinter as tk
from time import strftime

# Pastel vintage color palette
CREAM = "#FFF8EF"
DUSTY_PINK = "#D8A7A7"
DARK_BROWN = "#6B4F4F"
SAGE_GREEN = "#A8B5A0"
PALE_PINK = "#F5E6E0"

# Main window
root = tk.Tk()
root.title("Vintage Digital Clock")
root.geometry("550x320")
root.configure(bg=CREAM)
root.resizable(False, False)

# Decorative heading
title_label = tk.Label(
    root,
    text="~ A Little Vintage Clock ~",
    font=("Georgia", 20, "italic"),
    bg=CREAM,
    fg=DARK_BROWN
)
title_label.pack(pady=(25, 8))

# Decorative line
line = tk.Label(
    root,
    text="✿  ───────────────  ✿",
    font=("Georgia", 12),
    bg=CREAM,
    fg=DUSTY_PINK
)
line.pack()

# Clock display frame
clock_frame = tk.Frame(
    root,
    bg=PALE_PINK,
    highlightbackground=DUSTY_PINK,
    highlightthickness=2
)
clock_frame.pack(padx=35, pady=20, fill="x")

# Digital time
clock_label = tk.Label(
    clock_frame,
    font=("Courier New", 35, "bold"),
    bg=PALE_PINK,
    fg=DARK_BROWN
)
clock_label.pack(pady=(20, 5))

# Date display
date_label = tk.Label(
    clock_frame,
    font=("Georgia", 13, "italic"),
    bg=PALE_PINK,
    fg=SAGE_GREEN
)
date_label.pack(pady=(0, 18))

# Update time and date
def update_clock():
    clock_label.config(text=strftime("%I:%M:%S %p"))
    date_label.config(text=strftime("%A, %d %B %Y"))
    root.after(1000, update_clock)

# Footer decoration
footer = tk.Label(
    root,
    text="made with love  ♡",
    font=("Georgia", 11, "italic"),
    bg=CREAM,
    fg=DUSTY_PINK
)
footer.pack(pady=(0, 10))

# Start clock
update_clock()

root.mainloop()
