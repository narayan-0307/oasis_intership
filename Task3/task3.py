import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character set!"
    
    return "".join(random.choice(characters) for _ in range(length))

# Command-line version
def cli_version():
    length = int(input("Enter password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"Generated Password: {password}")

# GUI version
def gui_version():
    def generate():
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    root = tk.Tk()
    root.title("Password Generator")
    
    tk.Label(root, text="Password Length:").grid(row=0, column=0)
    length_entry = tk.Entry(root)
    length_entry.grid(row=0, column=1)
    
    letters_var = tk.BooleanVar()
    numbers_var = tk.BooleanVar()
    symbols_var = tk.BooleanVar()
    
    tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2)
    tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2)
    tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2)
    
    generate_button = tk.Button(root, text="Generate", command=generate)
    generate_button.grid(row=4, column=0, columnspan=2)
    
    password_entry = tk.Entry(root, width=30)
    password_entry.grid(row=5, column=0, columnspan=2)
    
    root.mainloop()

# Choose mode
if __name__ == "__main__":
    mode = input("Choose mode - CLI (c) or GUI (g): ").lower()
    if mode == 'c':
        cli_version()
    elif mode == 'g':
        gui_version()
    else:
        print("Invalid option. Choose 'c' for CLI or 'g' for GUI.")