# import tkinter as tk

# def say_hello():
#     print("Hello")

# def say_goodbye():
#     print("Goodbye")

# root = tk.Tk()
# root.title("Greet")
# root.geometry("240x144")

# label = tk.Label(root, text="Click a button:")
# label.pack(pady=10)

# hello_button = tk.Button(root, text="Say Hello", command=say_hello)
# hello_button.pack(pady=5)

# goodbye_button = tk.Button(root, text="Say Goodbye", command=say_goodbye)
# goodbye_button.pack(pady=5)

# root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title("Welcome to PERSONAL OS")
root.geometry("720x400")
name_var=tk.StringVar()
def catch_me():
    # print("Don't touch me")
    label = tk.Label(root, text="Comming Suun")
    label.pack()
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
# name_entry.grid(row=0,column=1)
name_entry.pack()
button = tk.Button(root, text="Touch ME is u can!!", command=catch_me)
button.pack()
root.mainloop()