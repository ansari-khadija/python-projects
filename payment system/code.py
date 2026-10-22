
import tkinter as tk
from tkinter import ttk, messagebox


# ---------- Polymorphism ----------
class Payment:
    def pay(self, amount):
        return "Payment processed"


class UPI(Payment):
    def pay(self, amount):
        return f"UPI payment of Rs. {amount:.2f} successful!"


class CreditCard(Payment):
    def pay(self, amount):
        return f"Credit Card payment of Rs. {amount:.2f} successful!"


class Cash(Payment):
    def pay(self, amount):
        return f"Cash payment of Rs. {amount:.2f} successful!"


# ---------- Payment Logic ----------
def make_payment():
    try:
        total = float(total_entry.get())
        amount = float(amount_entry.get())

        if total <= 0 or amount <= 0:
            messagebox.showerror(
                "Invalid Amount",
                "Enter amounts greater than zero."
            )
            return

        if amount > total:
            messagebox.showerror(
                "Payment Error",
                "Payment cannot exceed the total amount."
            )
            return

        methods = {
            "UPI": UPI,
            "Credit Card": CreditCard,
            "Cash": Cash
        }

        payment = methods[payment_var.get()]()
        result = payment.pay(amount)
        balance = total - amount

        result_label.config(
            text="✓ " + result,
            fg="#15803d"
        )

        total_value.config(text=f"Rs. {total:,.2f}")
        paid_value.config(text=f"Rs. {amount:,.2f}")
        balance_value.config(text=f"Rs. {balance:,.2f}")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric amounts."
        )


def reset_form():
    total_entry.delete(0, tk.END)
    total_entry.insert(0, "70000")
    amount_entry.delete(0, tk.END)

    payment_var.set("UPI")
    result_label.config(text="")
    total_value.config(text="Rs. 0.00")
    paid_value.config(text="Rs. 0.00")
    balance_value.config(text="Rs. 0.00")


# ---------- Main Window ----------
root = tk.Tk()
root.title("Payment Management System")
root.geometry("560x690")
root.configure(bg="#f1f5f9")


# ---------- Header ----------
header = tk.Frame(root, bg="#1e3a8a", height=110)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="PAYMENT MANAGER",
    font=("Arial", 22, "bold"),
    bg="#1e3a8a",
    fg="white"
).pack(pady=(22, 5))

tk.Label(
    header,
    text="Simple • Secure • Convenient",
    font=("Arial", 10),
    bg="#1e3a8a",
    fg="#dbeafe"
).pack()

# ---------- Main Card ----------
card = tk.Frame(
    root, bg="white",
    highlightbackground="#dbe3ef",
    highlightthickness=1
)
card.pack(fill="x", padx=28, pady=22)

def add_label(parent, text):
    tk.Label(
        parent,
        text=text,
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#334155"
    ).pack(anchor="w", padx=22, pady=(12, 5))


def add_entry(parent, default=""):
    entry = tk.Entry(
        parent,
        font=("Arial", 12),
        relief="solid",
        bd=1
    )
    entry.pack(fill="x", padx=22, ipady=8)
    if default:
        entry.insert(0, default)
    return entry


add_label(card, "Total Amount (Rs.)")
total_entry = add_entry(card, "70000")

add_label(card, "Payment Amount (Rs.)")
amount_entry = add_entry(card)

add_label(card, "Select Payment Method")

payment_var = tk.StringVar(value="UPI")

payment_box = ttk.Combobox(
    card,
    textvariable=payment_var,
    values=["UPI", "Credit Card", "Cash"],
    state="readonly",
    font=("Arial", 11)
)
payment_box.pack(fill="x", padx=22, ipady=5)

# ---------- Buttons ----------
button_frame = tk.Frame(card, bg="white")
button_frame.pack(fill="x", padx=22, pady=22)

tk.Button(
    button_frame,
    text="PAY NOW",
    command=make_payment,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
).pack(side="left", expand=True, fill="x", ipady=9, padx=(0, 6))

tk.Button(
    button_frame,
    text="RESET",
    command=reset_form,
    bg="#e2e8f0",
    fg="#1e293b",
    activebackground="#cbd5e1",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2"
).pack(side="left", expand=True, fill="x", ipady=9, padx=(6, 0))

# ---------- Result ----------
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold"),
    bg="#f1f5f9",
    wraplength=490
)
result_label.pack(pady=(0, 10))

# ---------- Payment Summary ----------
summary = tk.Frame(root, bg="white")
summary.pack(fill="x", padx=28, pady=5)

tk.Label(
    summary,
    text="PAYMENT SUMMARY",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#1e3a8a"
).pack(anchor="w", padx=18, pady=(14, 8))

def summary_row(label):
    row = tk.Frame(summary, bg="white")
    row.pack(fill="x", padx=18, pady=7)

    tk.Label(
        row, text=label,
        font=("Arial", 10),
        bg="white", fg="#64748b"
    ).pack(side="left")

    value = tk.Label(
        row, text="Rs. 0.00",
        font=("Arial", 10, "bold"),
        bg="white", fg="#0f172a"
    )
    value.pack(side="right")
    return value


total_value = summary_row("Total Amount")
paid_value = summary_row("Paid Amount")
balance_value = summary_row("Remaining Balance")

tk.Label(
    root,
    text="Educational project • No real money is transferred",
    font=("Arial", 9),
    bg="#f1f5f9",
    fg="#64748b"
).pack(pady=15)

root.mainloop()