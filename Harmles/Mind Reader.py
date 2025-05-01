import tkinter as tk
import random
import time
from tkinter import messagebox

def read_mind():
    number = entry.get()
    if not number.isdigit() or not (1 <= int(number) <= 10):
        messagebox.showerror("Error", "Please enter a number between 1 and 10.")
        return
    
    button.config(state=tk.DISABLED)
    label.config(text="Analyzing brainwaves...")
    root.update()
    time.sleep(1.5)
    
    label.config(text="Calculating probabilities...")
    root.update()
    time.sleep(1.5)
    
    guessed_number = random.randint(1, 10)
    messagebox.showinfo("Mind Reader", f"You're thinking of the number {guessed_number}.")
    button.config(state=tk.NORMAL)
    label.config(text="Think of a number between 1 and 10:")

root = tk.Tk()
root.title("Mind Reader")
root.geometry("300x200")

label = tk.Label(root, text="Think of a number between 1 and 10:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Read my mind", command=read_mind)
button.pack(pady=20)

root.mainloop()
