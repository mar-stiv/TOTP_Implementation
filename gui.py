import tkinter as tk
from tkinter import messagebox
import time
from totp_logic import get_current_totp_value, get_time_remaining, verify

def update_totp_display():
    """Update the TOTP value and time remaining every second."""
    current_totp_value = get_current_totp_value()
    totp_label.config(text=f"Current TOTP: {current_totp_value}")
    root.after(1000, get_time_remaining())
  

def check_totp():
    """Check if the entered TOTP is correct."""
    totp_entered = entry.get()
    if verify(totp_entered):
        result_label.config(text="Login successful", fg="green")
    else:
        result_label.config(text="Login failed", fg="red")

# Create the main window
root = tk.Tk()
root.title("TOTP App")

# Frame 1: Display TOTP and time remaining
totp_frame = tk.Frame(root, padx=20, pady=20, bd=2, relief=tk.GROOVE)
totp_frame.pack(pady=10)

current_totp_value = get_current_totp_value()
totp_label = tk.Label(totp_frame, text=f"Current TOTP: {current_totp_value}", font=("Arial", 14))
totp_label.pack()

time_remaining = get_time_remaining()
time_label = tk.Label(totp_frame, text=f"Time remaining: {time_remaining} seconds", font=("Arial", 12))
time_label.pack()

# Frame 2: Verification
verification_frame = tk.Frame(root, padx=20, pady=20, bd=2, relief=tk.GROOVE)
verification_frame.pack(pady=10)

tk.Label(verification_frame, text="To login, enter One-Time Password:", font=("Arial", 12)).pack()
entry = tk.Entry(verification_frame, font=("Arial", 12), justify="center")
entry.pack(pady=5)

ok_button = tk.Button(verification_frame, text="OK", command=check_totp)
ok_button.pack(pady=5)

result_label = tk.Label(verification_frame, text="", font=("Arial", 12, "bold"))
result_label.pack()

# Start the TOTP update loop
update_totp_display()

# Run the application
root.mainloop()