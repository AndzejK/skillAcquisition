import pyautogui
from pynput import mouse
import threading
import time

# Flag to stop the mouse movement
stop_movement = False

# Function to detect real mouse movement
def on_move(x, y):
    global stop_movement
    stop_movement = True
    return False # Stop listener
# Function to move the mouse slightly

def move_mouse():
    while not stop_movement:
        pyautogui.moveRel(1, 0, duration=0.1)
        pyautogui.moveRel(-1, 0, duration=0.1)
        time.sleep(5)

# Start the mouse listener in a separate thread
listener = mouse.Listener(on_move=on_move)
listener.start()

# Start moving the mouse
move_mouse()

# Wait for listener to finish
listener.join()

print("Mouse movement detected. Script stopped.")
