import tkinter as tk
from tkinter import messagebox

# Colors
BG_COLOR = "#2E2E2E"
DISPLAY_COLOR = "#1C1C1C"
BUTTON_COLOR = "#4D4D4D"
BUTTON_HOVER = "#666666"
OPERATOR_COLOR = "#FF9500"
TEXT_COLOR = "#FFFFFF"

# Create main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# Display
expression = ""
input_text = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    bg=DISPLAY_COLOR,
    fg=TEXT_COLOR,
    bd=0,
    relief=tk.FLAT,
    justify="right",
    insertbackground=TEXT_COLOR
)
display.pack(fill="both", ipadx=8, ipady=20, pady=(10, 0))


# Functions
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)


def clear():
    global expression
    expression = ""
    input_text.set("")


def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


def equalpress():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero!")
        expression = ""
        input_text.set("")
    except:
        messagebox.showerror("Error", "Invalid input!")
        expression = ""
        input_text.set("")


# Button frame
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(expand=True, fill="both", pady=10)


# Button creation function
def create_button(text, row, col, color=BUTTON_COLOR, command=None):
    btn = tk.Button(
        btn_frame,
        text=text,
        font=("Arial", 18, "bold"),
        bg=color,
        fg=TEXT_COLOR,
        relief=tk.FLAT,
        activebackground=BUTTON_HOVER,
        activeforeground=TEXT_COLOR,
        command=command
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3, ipadx=5, ipady=15)


# Configure grid
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
    btn_frame.columnconfigure(i, weight=1)

# Row 0
create_button("C", 0, 0, "#FF3B30", clear)
create_button("⌫", 0, 1, "#FF9500", backspace)
create_button("%", 0, 2, OPERATOR_COLOR, lambda: press("%"))
create_button("/", 0, 3, OPERATOR_COLOR, lambda: press("/"))

# Row 1
create_button("7", 1, 0, BUTTON_COLOR, lambda: press(7))
create_button("8", 1, 1, BUTTON_COLOR, lambda: press(8))
create_button("9", 1, 2, BUTTON_COLOR, lambda: press(9))
create_button("*", 1, 3, OPERATOR_COLOR, lambda: press("*"))

# Row 2
create_button("4", 2, 0, BUTTON_COLOR, lambda: press(4))
create_button("5", 2, 1, BUTTON_COLOR, lambda: press(5))
create_button("6", 2, 2, BUTTON_COLOR, lambda: press(6))
create_button("-", 2, 3, OPERATOR_COLOR, lambda: press("-"))

# Row 3
create_button("1", 3, 0, BUTTON_COLOR, lambda: press(1))
create_button("2", 3, 1, BUTTON_COLOR, lambda: press(2))
create_button("3", 3, 2, BUTTON_COLOR, lambda: press(3))
create_button("+", 3, 3, OPERATOR_COLOR, lambda: press("+"))

# Row 4
create_button("0", 4, 0, BUTTON_COLOR, lambda: press(0))
create_button(".", 4, 1, BUTTON_COLOR, lambda: press("."))
create_button("=", 4, 2, OPERATOR_COLOR, equalpress)
# Empty space for alignment
tk.Label(btn_frame, bg=BG_COLOR).grid(row=4, column=3, sticky="nsew")

root.mainloop()
