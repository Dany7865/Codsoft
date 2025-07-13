import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected = listbox_tasks.curselection()[0]
        new_task = entry_task.get()
        if new_task != "":
            listbox_tasks.delete(selected)
            listbox_tasks.insert(selected, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter updated task text.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectbackground="skyblue", selectforeground="black")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=5)

button_add_task = tk.Button(root, text="Add Task", width=48, bg="#4CAF50" , fg="white", command=add_task)
button_add_task.pack(pady=2)

button_delete_task = tk.Button(root, text="Delete Task", width=48, bg="#f44336", fg="white", command=delete_task)
button_delete_task.pack(pady=2)

button_update_task = tk.Button(root, text="Update Task", width=48, bg="#2196F3", fg="white", command=update_task)
button_update_task.pack(pady=2)

root.mainloop()