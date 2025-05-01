import pygame
import tkinter as tk
from tkinter import filedialog
import pickle
import os
import webbrowser  # Importiere die Bibliothek für das Öffnen von Websites

# Initialisiere pygame
pygame.mixer.init()

# Speicherpfad für die Musikdatei
SAVED_FILE = "saved_music.pkl"
TEMP_FILE = "temp.mp3"
music_data = None  # Speichert die Musikdaten im RAM

def load_music():
    """Lädt gespeicherte Musik, falls vorhanden."""
    global music_data
    if os.path.exists(SAVED_FILE):
        with open(SAVED_FILE, "rb") as f:
            music_data = pickle.load(f)
    else:
        music_data = None

def save_music(file_path):
    """Speichert die Musikdatei als binäre Daten."""
    global music_data
    with open(file_path, "rb") as f:
        music_data = f.read()  # Direkt in die Variable speichern
    with open(SAVED_FILE, "wb") as f:
        pickle.dump(music_data, f)

def stop_music():
    """Stoppt die Musik und setzt pygame zurück."""
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.mixer.init()

def play_music():
    """Spielt die gespeicherte Musik."""
    stop_music()  # Stopp vorherige Musik

    if music_data:
        # Falls temp.mp3 existiert, löschen
        if os.path.exists(TEMP_FILE):
            try:
                os.remove(TEMP_FILE)
            except PermissionError:
                print("Fehler: temp.mp3 konnte nicht gelöscht werden.")
                return

        with open(TEMP_FILE, "wb") as f:
            f.write(music_data)

        pygame.mixer.music.load(TEMP_FILE)
        pygame.mixer.music.play()
    else:
        print("Keine Musik gespeichert. Bitte eine Datei auswählen.")

def select_music():
    """Lässt den Nutzer eine neue MP3-Datei wählen und speichert sie."""
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        stop_music()  # Stoppe laufende Musik
        save_music(file_path)  # Speichere neue Musik
        play_music()  # Spiele direkt die neue Musik

def open_website():
    """Öffnet eine Website."""
    webbrowser.open("https://cobalt.tools/")  # Ersetze mit der gewünschten URL

def do_nothing():
    """Leere Funktion, die nichts tut."""
    pass

# Lade gespeicherte Musik beim Start
load_music()

# GUI mit Tkinter
root = tk.Tk()
root.title("MP3 Player")
root.geometry("400x400")  # Großes Fenster

# Buttons für Play, Stop und Datei auswählen
play_button = tk.Button(root, text="▶ Play", font=("Arial", 14), command=play_music, width=20, height=2)
play_button.pack(pady=10)

stop_button = tk.Button(root, text="⏹ Stop", font=("Arial", 14), command=stop_music, width=20, height=2)
stop_button.pack(pady=10)

select_button = tk.Button(root, text="New Mp3", font=("Arial", 12), command=select_music, width=20, height=2)
select_button.pack(pady=10)

# Button für die Website
website_button = tk.Button(root, text="yt vids to mp3", font=("Arial", 12), command=open_website, width=20, height=2)
website_button.pack(pady=10)

# Button, der nichts tut
nothing_button = tk.Button(root, text="Made by MarlonVr", font=("Arial", 12), command=do_nothing, width=20, height=2)
nothing_button.pack(pady=10)

root.mainloop()
