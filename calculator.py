import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="light blue")


problem = ""


def number_1(number):
    global problem
    if problem == "":
        problem = number
    else:
        problem = problem + number
    rectangle1.config(text=problem)

def symbol(sym):
    global problem
    if problem != "" and problem[len(problem)-1] != "+" and problem[len(problem)-1] != "-" and problem[len(problem)-1] != "/" and problem[len(problem)-1] != "*" and problem[len(problem)-1] != "=" and problem[len(problem)-1] != ".":
        problem = problem + sym
    rectangle1.config(text=problem)

def calculate(e):
    global problem
    problem = eval(problem)
    rectangle1.config(text=problem)

def clear1():
    global problem
    problem = ""
    rectangle1.config(text=problem)

rectangle1 = tk.Label(root)

number1 = tk.Button(root, text="1", bg="white", fg="black", command=lambda:number_1("1"))
number2 = tk.Button(root, text="2", bg="white", fg="black", command=lambda:number_1("2"))
number3 = tk.Button(root, text="3", bg="white", fg="black", command=lambda:number_1("3"))
number4 = tk.Button(root, text="4", bg="white", fg="black", command=lambda:number_1("4"))
number5 = tk.Button(root, text="5", bg="white", fg="black", command=lambda:number_1("5"))
number6 = tk.Button(root, text="6", bg="white", fg="black", command=lambda:number_1("6"))
number7 = tk.Button(root, text="7", bg="white", fg="black", command=lambda:number_1("7"))
number8 = tk.Button(root, text="8", bg="white", fg="black", command=lambda:number_1("8"))
number9 = tk.Button(root, text="9", bg="white", fg="black", command=lambda:number_1("9"))
number0 = tk.Button(root, text="0", bg="white", fg="black", command=lambda:number_1("0"))
period = tk.Button(root, text=".", bg="white", fg="black", command=lambda:symbol("."))
equal = tk.Button(root, text="=", bg="white", fg="black", command=lambda:calculate("="))
plus = tk.Button(root, text="+", bg="white", fg="black", command=lambda:symbol("+"))
minus = tk.Button(root, text="-", bg="white", fg="black", command=lambda:symbol("-"))
divide = tk.Button(root, text="/", bg="white", fg="black", command=lambda:symbol("/"))
multiply = tk.Button(root, text="*", bg="white", fg="black", command=lambda:symbol("*"))
clear = tk.Button(root, text="C", bg="white", fg="black", command=clear1)

rectangle1.grid(row="0", columnspan="4", ipady=10, sticky="NSEW")
number1.grid(row="1", column="0", ipadx=15, ipady=10, sticky="NSEW")
number2.grid(row="1", column="1", ipadx=15, ipady=10, sticky="NSEW")
number3.grid(row="1", column="2", ipadx=15, ipady=10, sticky="NSEW")
number4.grid(row="2", column="0", ipadx=15, ipady=10, sticky="NSEW")
number5.grid(row="2", column="1", ipadx=15, ipady=10, sticky="NSEW")
number6.grid(row="2", column="2", ipadx=15, ipady=10, sticky="NSEW")
number7.grid(row="3", column="0", ipadx=15, ipady=10, sticky="NSEW")
number8.grid(row="3", column="1", ipadx=15, ipady=10, sticky="NSEW")
number9.grid(row="3", column="2", ipadx=15, ipady=10, sticky="NSEW")
number0.grid(row="4", column="1", ipadx=15, ipady=10, sticky="NSEW")
period.grid(row="4", column="0", ipadx=15, ipady=10, sticky="NSEW")
equal.grid(row="4", column="2", ipadx=15, ipady=10, sticky="NSEW")
plus.grid(row="4", column="3", ipadx=15, ipady=10, sticky="NSEW")
minus.grid(row="3", column="3", ipadx=15, ipady=10, sticky="NSEW")
divide.grid(row="2", column="3", ipadx=15, ipady=10, sticky="NSEW")
multiply.grid(row="1", column="3", ipadx=15, ipady=10, sticky="NSEW")
clear.grid(row="5", column="0", ipadx=15, ipady=10, sticky="NSEW")

root.mainloop()
