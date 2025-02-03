import tkinter as tk

root = tk.Tk()
root.title("My First App")
root.geometry("300x200")
def say_hello():
    print("Hello!")


button = tk.Button(root,text="Click Me")
button.pack()
label = tk.Label(root, text="Hello World!")
label.pack()

root.mainloop()
