import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg = "light blue")


def number():
    yield "y"


rectangle1 = tk.Label(root)

number1 = tk.Button(root, text="1", bg="white", fg="black")
number2 = tk.Button(root, text="2", bg="white", fg="black")
number3 = tk.Button(root, text="3", bg="white", fg="black")
number4 = tk.Button(root, text="4", bg="white", fg="black")
number5 = tk.Button(root, text="5", bg="white", fg="black")
number6 = tk.Button(root, text="6", bg="white", fg="black")
number7 = tk.Button(root, text="7", bg="white", fg="black")
number8 = tk.Button(root, text="8", bg="white", fg="black")
number9 = tk.Button(root, text="9", bg="white", fg="black")
number0 = tk.Button(root, text="0", bg="white", fg="black")
period = tk.Button(root, text=".", bg="white", fg="black")
equal = tk.Button(root, text="=", bg="white", fg="black")
plus = tk.Button(root, text="+", bg="white", fg="black")
minus = tk.Button(root, text="-", bg="white", fg="black")
divide = tk.Button(root, text="/", bg="white", fg="black")
multiply = tk.Button(root, text="*", bg="white", fg="black")


rectangle1.grid(row="0", columnspan="4", sticky="NSEW")
number1.grid(row="1", column="0", sticky="NSEW")
number2.grid(row="1", column="1", sticky="NSEW")
number3.grid(row="1", column="2", sticky="NSEW")
number4.grid(row="2", column="0", sticky="NSEW")
number5.grid(row="2", column="1", sticky="NSEW")
number6.grid(row="2", column="2", sticky="NSEW")
number7.grid(row="3", column="0", sticky="NSEW")
number8.grid(row="3", column="1", sticky="NSEW")
number9.grid(row="3", column="2", sticky="NSEW")
number0.grid(row="4", column="1", sticky="NSEW")
period.grid(row="4", column="0", sticky="NSEW")
equal.grid(row="4", column="2", sticky="NSEW")
plus.grid(row="4", column="3", sticky="NSEW")
minus.grid(row="3", column="3", sticky="NSEW")
divide.grid(row="2", column="3", sticky="NSEW")
multiply.grid(row="1", column="3", sticky="NSEW")







root.mainloop()