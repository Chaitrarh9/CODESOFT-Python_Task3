import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    length = int(entry_length.get())
    password = generate_password(length)
    result_var.set(password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.configure(bg="#2c3e50")

# Create and pack widgets
label_length = tk.Label(window, text="Password Length:", font=("Arial", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_length.pack(pady=(20, 5))

entry_length = tk.Entry(window, font=("Arial", 14))
entry_length.pack(pady=(0, 10))

generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked, bg="#3498db", fg="white", font=("Arial", 14, "bold"))
generate_button.pack(pady=20)

result_var = StringVar()
label_result = tk.Label(window, textvariable=result_var, font=("Arial", 16), wraplength=300, bg="#2c3e50", fg="white")
label_result.pack(pady=(10, 20))

# Center the label and button
window.update_idletasks()
label_length.place(relx=0.5, rely=0.25, anchor="center")
entry_length.place(relx=0.5, rely=0.4, anchor="center")
generate_button.place(relx=0.5, rely=0.55, anchor="center")
label_result.place(relx=0.5, rely=0.7, anchor="center")

# Start the GUI
window.mainloop()
