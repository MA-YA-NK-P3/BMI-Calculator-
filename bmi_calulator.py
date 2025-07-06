
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# --------------- BMI Logic -----------------
def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100
        weight = float(entry_weight.get())
        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)

        result_text = f"BMI: {bmi:.2f} ({category})"
        label_result.config(text=result_text, foreground="#007f5f")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Retry function
def retry():
    entry_name.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    label_result.config(text="")

# --------------- GUI Setup -----------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x560")
root.configure(bg="#e6f2ff")

# Load and display banner image
try:
    banner_img = Image.open("assets/banner.png")
    banner_img = banner_img.resize((360, 200))
    banner_photo = ImageTk.PhotoImage(banner_img)
    banner_label = tk.Label(root, image=banner_photo, bg="#e6f2ff")
    banner_label.image = banner_photo  # Keep reference
    banner_label.pack(pady=10)
except Exception as e:
    print("Banner image could not be loaded:", e)

# Style
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(pady=10)

header = ttk.Label(main_frame, text="BMI Calculator", font=("Segoe UI", 18, "bold"), foreground="#007f5f")
header.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky='e', pady=5)
entry_name = ttk.Entry(main_frame, width=25)
entry_name.grid(row=1, column=1)

ttk.Label(main_frame, text="Height (cm):").grid(row=2, column=0, sticky='e', pady=5)
entry_height = ttk.Entry(main_frame, width=25)
entry_height.grid(row=2, column=1)

ttk.Label(main_frame, text="Weight (kg):").grid(row=3, column=0, sticky='e', pady=5)
entry_weight = ttk.Entry(main_frame, width=25)
entry_weight.grid(row=3, column=1)

ttk.Button(main_frame, text="Calculate BMI", command=calculate_bmi).grid(row=4, column=0, columnspan=2, pady=10)
label_result = ttk.Label(main_frame, text="", font=("Segoe UI", 11))
label_result.grid(row=5, column=0, columnspan=2, pady=5)

ttk.Button(main_frame, text="Retry", command=retry).grid(row=6, column=0, pady=10)
ttk.Button(main_frame, text="Exit", command=root.destroy).grid(row=6, column=1, pady=10)

root.mainloop()
