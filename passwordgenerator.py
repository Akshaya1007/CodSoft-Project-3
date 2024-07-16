import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive.")
    except ValueError as e:
        messagebox.showerror("Invalid input", "Please enter a valid number for length.")
        return
    
    characters = ""
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation

    if var_exclude_similar.get():
        characters = characters.translate(str.maketrans('', '', 'l1Io0'))
    if var_exclude_ambiguous.get():
        characters = characters.translate(str.maketrans('', '', '{}[]()/\'"`~,;:.<>'))

    if not characters:
        messagebox.showerror("No character sets selected", "Please select at least one character set.")
        return
    
    global password
    password = ''.join(random.choice(characters) for i in range(length))
    label_result.config(text=password)

def save_password():
    if not password:
        messagebox.showerror("No password", "Please generate a password first.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(password)
        messagebox.showinfo("Password Saved", f"Password saved to {file_path}")

def copy_password():
    if not password:
        messagebox.showerror("No password", "Please generate a password first.")
        return
    
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Password Copied", "Password copied to clipboard")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.config(bg="#ffcccb")  # Background color for the main window (light pink)

# Create and place widgets
tk.Label(root, text="Enter the desired length of the password:", bg="#ffcccb").pack(pady=10)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Checkboxes for character sets
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()
var_exclude_similar = tk.BooleanVar()
var_exclude_ambiguous = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg="#ffcccb").pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase, bg="#ffcccb").pack(anchor='w')
tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg="#ffcccb").pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg="#ffcccb").pack(anchor='w')
tk.Checkbutton(root, text="Exclude Similar Characters (l, 1, I, O, 0)", variable=var_exclude_similar, bg="#ffcccb").pack(anchor='w')
tk.Checkbutton(root, text="Exclude Ambiguous Characters ({}[]()/\'\"`~,;:.<>)", variable=var_exclude_ambiguous, bg="#ffcccb").pack(anchor='w')

tk.Button(root, text="Generate Password", command=generate_password, bg="#ff9999").pack(pady=10)

# Result label in a black box
label_result = tk.Label(root, text="", bg="black", fg="white", width=30, height=2)
label_result.pack(pady=10)

# Save password button
tk.Button(root, text="Save Password", command=save_password, bg="#ff9999").pack(pady=10)

# Copy password button
tk.Button(root, text="Copy Password", command=copy_password, bg="#ff9999").pack(pady=10)

# Global variable to store the password
password = ""

# Run the application
root.mainloop()
