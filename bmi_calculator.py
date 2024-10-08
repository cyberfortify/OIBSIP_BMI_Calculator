import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive values.")
            return
        
        bmi = weight / (height ** 2)
        category = identify_bmi(bmi)
        
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}")
        
        # Store historical data (for demonstration, we just print it)
        historical_data.append(bmi)
        print(f"Historical BMI Data: {historical_data}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Function to identify the BMI category
def identify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

root = tk.Tk()
root.title("BMI Calculator")

# Weight input
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Height input
height_label = tk.Label(root, text="Enter your height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Initialize historical data
historical_data = []

root.mainloop()
