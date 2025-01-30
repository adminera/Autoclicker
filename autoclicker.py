import pyautogui
import tkinter as tk
from threading import Thread
import time
import threading

# Function to simulate mouse clicks
def auto_clicker(click_speed, stop_event):
    while not stop_event.is_set():
        pyautogui.click()
        time.sleep(click_speed)

# Function to start the autoclicker
def start_clicking():
    try:
        click_speed = float(entry_speed.get())  # Get the click speed (seconds between clicks)
        if click_speed <= 0:
            raise ValueError("Click speed must be greater than 0.")
        
        # Start the clicking in a new thread
        stop_event.clear()
        threading_thread = Thread(target=auto_clicker, args=(click_speed, stop_event))
        threading_thread.daemon = True  # So it stops when the main program exits
        threading_thread.start()
        start_button.config(state=tk.DISABLED)  # Disable start button while autoclicker is running
        stop_button.config(state=tk.NORMAL)  # Enable stop button
    except ValueError as e:
        error_label.config(text=f"Error: {str(e)}")

# Function to stop the autoclicker
def stop_clicking():
    stop_event.set()
    start_button.config(state=tk.NORMAL)  # Re-enable the start button
    stop_button.config(state=tk.DISABLED)  # Disable the stop button

# Create GUI window
window = tk.Tk()
window.title("AutoClicker")
window.geometry("300x200")

stop_event = threading.Event()

# Speed entry widget
label_speed = tk.Label(window, text="Click Speed (seconds):")
label_speed.pack(pady=10)

entry_speed = tk.Entry(window)
entry_speed.insert(0, "0.1")  # Default to 0.1 seconds between clicks
entry_speed.pack(pady=5)

# Start and Stop buttons
start_button = tk.Button(window, text="Start", command=start_clicking)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop", command=stop_clicking, state=tk.DISABLED)
stop_button.pack(pady=5)

# Error message display
error_label = tk.Label(window, text="", fg="red")
error_label.pack(pady=5)

window.mainloop()
