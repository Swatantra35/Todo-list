import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

task_entry = tk.Entry(root, width=25)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=30, height=10)
tasks_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
