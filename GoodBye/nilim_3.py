import tkinter as tk

root=tk.Tk()
root.title("Task Management App")
root.geometry("500x500")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)

def delete_task():
    task_listbox.delete(tk.ANCHOR)
def clear_task():
    task_listbox.delete(0,tk.END)

task_entry = tk.Entry(root,width=75)
task_entry.pack(pady=20)

tk.Button(root,text="Entry",command=add_task).pack()
tk.Button(root,text="Delete",command=delete_task).pack()
tk.Button(root,text="Finish All",command=clear_task).pack()

task_listbox = tk.Listbox(root,width=50,height=50)
task_listbox.pack(pady=20)


root.mainloop()