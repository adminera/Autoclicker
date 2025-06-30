# Autoclicker

<p>A simple Python-based AutoClicker application with a graphical user interface (GUI) built using Tkinter. This tool automates mouse clicks at a user-specified speed, making it useful for repetitive tasks in games, testing, or other applications requiring continuous clicking.</p>

---

# Features

- Customizable Click Speed: Set the interval between clicks (in seconds) via a GUI input field.
- Start/Stop Controls: Easily start and stop the auto-clicking process with dedicated buttons.
- Error Handling: Displays error messages for invalid inputs (e.g., non-positive click speeds).
- Multithreaded: Uses threading to ensure the GUI remains responsive while the auto-clicker runs.
- Cross-Platform: Works on Windows, macOS, and Linux (with Python and dependencies installed).

---

# Requirements

To run the AutoClicker, you need:

- **Python 3.6 or higher**
- External Library **Pyautogui**

---

# Setup Instructions

Follow these steps to set up and run the AutoClicker:

1. Install Python:

Ensure Python 3.6+ is installed. Download it from python.org if needed.

Verify installation by running:
```sh
python --version
python3 --version
```

2. Install Dependencies:

The program requires pyautogui, this can be installed by either:

```sh
pip install -r requirements.txt
pip install pyautogui
```

3. Download program

# Usage

```sh
python autoclicker.py
python3 autoclicker.py
```
