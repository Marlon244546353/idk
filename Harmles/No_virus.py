import tkinter as tk
from tkinter import messagebox
import random
import threading
import keyboard
import pyautogui
import time

ads = []
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_ad():
    ad = tk.Toplevel()
    ad.title("🔥 EXKLUSIVES ANGEBOT! 🔥")

    
    screen_width = ad.winfo_screenwidth()
    screen_height = ad.winfo_screenheight()
    x = random.randint(0, screen_width - 300)
    y = random.randint(0, screen_height - 200)
    ad.geometry(f"300x200+{x}+{y}")

  
    label = tk.Label(ad, text="💰 Sie haben gewonnen! 💰", font=("Arial", 14, "bold"), fg="red")
    label.pack(pady=20)

    button = tk.Button(ad, text="Hier klicken!", font=("Arial", 12), bg="yellow", command=lambda: print("Wir haben deine daten Loser"))
    button.pack()

    ads.append(ad)  


def start_ads():
    for _ in range(1000): 
        time.sleep(random.uniform(0.100, 0))  
        create_ad()


def close_all():
    for ad in ads:
        ad.destroy()
    trail_window.destroy()
    root.destroy()


def draw_trail():
    last_x, last_y = None, None  

    while True:
        x, y = pyautogui.position()
        color = random.choice(rainbow_colors)

        if last_x is not None and last_y is not None:
            
            canvas.create_line(last_x, last_y, x, y, fill=color, width=5)

        last_x, last_y = x, y  
        trail_window.update()
        time.sleep(0.01)  


def block_win_key(event):
    if event.name == 'win':
        return False  

keyboard.hook(block_win_key)  


root = tk.Tk()
root.withdraw()  


messagebox.showwarning("⚠️ Warnung", "Dieses programm ist nur ein joke wenn du es beenden willst \nDrücke 'X', manchmal musst du x öffters drücken wenn du es mehr als 5 minuten laufen lässt könnte es lag verursachen")


trail_window = tk.Toplevel()
trail_window.geometry(f"{pyautogui.size().width}x{pyautogui.size().height}+0+0")
trail_window.attributes('-topmost', True)  
trail_window.overrideredirect(True)  
trail_window.wm_attributes('-transparentcolor', 'black')  


canvas = tk.Canvas(trail_window, width=pyautogui.size().width, height=pyautogui.size().height, bg="black", highlightthickness=0)
canvas.pack()
canvas.configure(bg="black")


threading.Thread(target=start_ads, daemon=True).start()


threading.Thread(target=draw_trail, daemon=True).start()


keyboard.add_hotkey("x", close_all)

root.mainloop()