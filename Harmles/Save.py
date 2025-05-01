import tkinter as tk
from tkinter import messagebox


def cycle_colors():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    current_color = cycle_colors.counter % len(colors)
    save_button.config(bg=colors[current_color])
    cycle_colors.counter += 1
    root.after(300, cycle_colors)  

cycle_colors.counter = 0


def save_progress():
    if messagebox.askokcancel("Progress Saved", "You saved your life progress"):
        root.quit() 


root = tk.Tk()
root.title("Save Progress")
root.geometry("300x200")


save_button = tk.Button(root, text="Save", font=("Arial", 16), command=save_progress)
save_button.pack(expand=True)


cycle_colors()


root.mainloop()
