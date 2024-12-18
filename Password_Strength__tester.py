import re
import tkinter as tk
from tkinter import ttk

def calculate_password_strength(password):
    point = 0
    width_power = ["1%", "25%", "50%", "75%", "100%"]
    color_power = ["#D73F40", "#DC6551", "#F2B84F", "#BDE952", "#3ba62f"]

    if len(password) >= 6:
        array_test = [r'[0-9]', r'[a-z]', r'[A-Z]', r'[^0-9a-zA-Z]']
        for pattern in array_test:
            if re.search(pattern, password):
                point += 1

    width = width_power[point]
    color = color_power[point]
    
    return width, color

def check_password():
    password = password_entry.get()
    width, color = calculate_password_strength(password)
    strength_bar['value'] = int(width.strip('%'))
    strength_bar.update()
    strength_bar_label.config(text=f"Strength: {width}", background=color)

def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        eye_button.config(text='Show')
    else:
        password_entry.config(show='')
        eye_button.config(text='Hide')

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

# Password entry
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)

password_frame = tk.Frame(root)
password_frame.pack(pady=5)

password_entry = tk.Entry(password_frame, show='*')
password_entry.pack(side=tk.LEFT, padx=(0, 5))

eye_button = tk.Button(password_frame, text='Show', command=toggle_password_visibility)
eye_button.pack(side=tk.LEFT)

# Check button
check_button = tk.Button(root, text="Check", command=check_password)
check_button.pack(pady=10)

# Strength bar
strength_bar_label = tk.Label(root, text="Strength: 0%", background="#D73F40", width=20)
strength_bar_label.pack(pady=5)

strength_bar = ttk.Progressbar(root, length=200, mode='determinate')
strength_bar.pack(pady=5)

root.mainloop()

