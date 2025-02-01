import tkinter as tk

root =tk.Tk()
root.title =("Communication")
root.geometry("400x200")

def say_hello():
    print("Hello!")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

label = tk.Label(root, text="Hi, How aer you!")
label.pack()

C = tk.Canvas(root, bg="yellow",
           height=250, width=300)
 
line = C.create_line(108, 120,
                     320, 40,
                     fill="green")
 
arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")
 
oval = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")
 
C.pack()

root.mainloop()