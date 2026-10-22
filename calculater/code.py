import tkinter as tk


class Calculator:

    def __init__(self, display):
        self.display = display
        self.current = ""

    # Instance method
    def press(self, value):
        self.current += str(value)
        self.display.config(text=self.current)

    # Instance method
    def clear(self):
        self.current = ""
        self.display.config(text="0")

    # Instance method
    def calculate(self):
        try:
            result = eval(self.current)
            self.current = str(result)
            self.display.config(text=self.current)
        except:
            self.current = ""
            self.display.config(text="Error")


# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("♡ Pastel Y2K Calculator ♡")
window.geometry("420x600")
window.resizable(True, True)

# Soft Y2K pastel colors
BG = "#FCE4EC"
DISPLAY_BG = "#FFF5FA"
PINK = "#F8BBD0"
PINK_DARK = "#E8A0B8"
LAVENDER = "#DCD6F7"
BLUE = "#CDE7F0"
TEXT = "#76546A"
WHITE = "#FFF9FC"

window.configure(bg=BG)


# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="♡ Y2K CALCULATOR ♡",
    font=("Arial", 20, "bold"),
    bg=BG,
    fg=TEXT
)

title.pack(pady=(25, 15))


# ---------------- DISPLAY ----------------

display = tk.Label(
    window,
    text="0",
    font=("Arial", 30, "bold"),
    bg=DISPLAY_BG,
    fg=TEXT,
    anchor="e",
    padx=15,
    relief="flat"
)

display.pack(
    padx=25,
    pady=10,
    fill="x",
    ipady=20
)


# Create calculator object
calc = Calculator(display)


# ---------------- BUTTON FRAME ----------------

button_frame = tk.Frame(
    window,
    bg=BG
)

button_frame.pack(pady=20)


# ---------------- BUTTON FUNCTION ----------------

def create_button(text, row, column, color, command):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 17, "bold"),
        bg=color,
        fg=TEXT,
        activebackground=WHITE,
        activeforeground=TEXT,
        relief="flat",
        bd=0,
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=6,
        pady=6
    )


# ---------------- BUTTONS ----------------

create_button("7", 0, 0, PINK, lambda: calc.press("7"))
create_button("8", 0, 1, PINK, lambda: calc.press("8"))
create_button("9", 0, 2, PINK, lambda: calc.press("9"))
create_button("÷", 0, 3, LAVENDER, lambda: calc.press("/"))

create_button("4", 1, 0, PINK, lambda: calc.press("4"))
create_button("5", 1, 1, PINK, lambda: calc.press("5"))
create_button("6", 1, 2, PINK, lambda: calc.press("6"))
create_button("×", 1, 3, LAVENDER, lambda: calc.press("*"))

create_button("1", 2, 0, PINK, lambda: calc.press("1"))
create_button("2", 2, 1, PINK, lambda: calc.press("2"))
create_button("3", 2, 2, PINK, lambda: calc.press("3"))
create_button("-", 2, 3, LAVENDER, lambda: calc.press("-"))

create_button("0", 3, 0, PINK, lambda: calc.press("0"))
create_button(".", 3, 1, PINK, lambda: calc.press("."))
create_button("+", 3, 2, LAVENDER, lambda: calc.press("+"))
create_button("=", 3, 3, BLUE, calc.calculate)

create_button("CLEAR", 4, 0, PINK_DARK, calc.clear)


# ---------------- FOOTER ----------------

footer = tk.Label(
    window,
    text="✦ soft pastel computing ✦",
    font=("Arial", 10),
    bg=BG,
    fg=TEXT
)

footer.pack(pady=15)


window.mainloop()
