import tkinter as tk
from tkinter import messagebox, filedialog
import csv

# -------------------------------
# BMI Calculation Logic
# -------------------------------
class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # in kilograms
        self.height = height  # in meters

    def calculate_bmi(self):
        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        return round(self.weight / (self.height ** 2), 2)

    def category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

# -------------------------------
# Console Mode
# -------------------------------
def console_mode():
    print("=== BMI Calculator (Console Mode) ===")
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        calc = BMICalculator(weight, height)
        bmi = calc.calculate_bmi()
        print(f"Your BMI is: {bmi}")
        print(f"Category: {calc.category(bmi)}")
    except Exception as e:
        print("Error:", e)

# -------------------------------
# Batch Mode (CSV Input/Output)
# -------------------------------
def batch_mode(input_file="bmi_input.csv", output_file="bmi_output.csv"):
    results = []
    try:
        with open(input_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    name, weight, height = row
                    calc = BMICalculator(float(weight), float(height))
                    bmi = calc.calculate_bmi()
                    category = calc.category(bmi)
                    results.append([name, weight, height, bmi, category])
                except Exception as e:
                    results.append([row[0], "Error", str(e)])
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Weight (kg)", "Height (m)", "BMI", "Category"])
            writer.writerows(results)
        print(f"Batch results saved to {output_file}")
    except FileNotFoundError:
        print(f"Input file {input_file} not found.")

# -------------------------------
# GUI Mode
# -------------------------------
class BMIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")

        tk.Label(root, text="Weight (kg):").pack()
        self.weight_var = tk.DoubleVar()
        tk.Entry(root, textvariable=self.weight_var).pack()

        tk.Label(root, text="Height (m):").pack()
        self.height_var = tk.DoubleVar()
        tk.Entry(root, textvariable=self.height_var).pack()

        tk.Button(root, text="Calculate BMI", command=self.calculate).pack(pady=10)
        tk.Button(root, text="Save Result", command=self.save_result).pack(pady=5)

        self.output = tk.Text(root, height=5, width=40)
        self.output.pack(pady=10)

    def calculate(self):
        try:
            calc = BMICalculator(self.weight_var.get(), self.height_var.get())
            bmi = calc.calculate_bmi()
            category = calc.category(bmi)
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, f"BMI: {bmi}\nCategory: {category}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_result(self):
        result = self.output.get("1.0", tk.END).strip()
        if result:
            file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file:
                with open(file, "w") as f:
                    f.write(result)
                messagebox.showinfo("Saved", f"Result saved to {file}")
        else:
            messagebox.showwarning("Warning", "No result to save!")

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    print("Choose mode:")
    print("1. Console Mode")
    print("2. Batch Mode (CSV)")
    print("3. GUI Mode")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        console_mode()
    elif choice == "2":
        batch_mode()
    elif choice == "3":
        root = tk.Tk()
        app = BMIGUI(root)
        root.mainloop()
    else:
        print("Invalid choice.")
