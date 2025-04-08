import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Create or connect to the database
def init_db():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bmi_records (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      weight REAL,
                      height REAL,
                      bmi REAL,
                      category TEXT)''')
    conn.commit()
    conn.close()

# Function to calculate BMI and categorize

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive values.")
            return
        
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        save_bmi(name, weight, height, bmi, category)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Save data to the database
def save_bmi(name, weight, height, bmi, category):
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bmi_records (name, weight, height, bmi, category) VALUES (?, ?, ?, ?, ?)",
                   (name, weight, height, bmi, category))
    conn.commit()
    conn.close()

# Show BMI history and trend
def show_history():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bmi_records")
    data = cursor.fetchall()
    conn.close()
    
    if not data:
        messagebox.showinfo("No Data", "No BMI records found.")
        return
    
    names, bmis = zip(*[(row[1], row[4]) for row in data])
    
    plt.figure(figsize=(8, 5))
    plt.plot(names, bmis, marker='o', linestyle='-', color='b')
    plt.xlabel("User")
    plt.ylabel("BMI")
    plt.title("BMI History")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# GUI Setup
init_db()
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_btn = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

history_btn = tk.Button(root, text="View History", command=show_history)
history_btn.pack()

root.mainloop()

