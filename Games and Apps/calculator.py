import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget to display the equation
equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, padx=5, pady=5)

# Function to update entry field when buttons are pressed
def press(num):
    equation.set(equation.get() + str(num))

# Function to evaluate the expression
def calculate():
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except:
        equation.set("Error")

# Function to clear the entry field
def clear():
    equation.set("")

# Create a frame for the buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Add buttons to the frame
for row in buttons:
    frame_row = tk.Frame(btn_frame)
    frame_row.pack(fill="both", expand=True)
    for char in row:
        btn = tk.Button(frame_row, text=char, font=("Arial", 20), width=5, height=2,
                        command=lambda ch=char: press(ch) if ch not in ("C", "=") else clear() if ch == "C" else calculate())
        btn.pack(side="left", fill="both", expand=True)

# Run the Tkinter event loop
root.mainloop()
