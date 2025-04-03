import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.config(bg="black")

# Fonts
large_font = ('Verdana', 15)
small_font = ('Verdana', 10)

frame = tk.Frame(root, width=500, height=400)
frame.grid(row=1, column=0)
top_frame = tk.Frame(root, width=500, height=100)
top_frame.grid(row=0, column=0)

result = tk.StringVar()
entry = tk.Entry(top_frame, textvariable=result, width=30, bg="black", fg="white", font=large_font)
entry.grid(row=0, column=0, ipady=15)

#Functii
def button_click(value):
    entry.insert(tk.END, value)

def button_clear():
    entry.delete(0, "end")

def equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, "end")
        entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("Eroare", "Împărțirea la zero nu este permisă!")
        entry.delete(0, "end")
    except Exception:
        messagebox.showerror("Eroare", "Expresie invalidă!")
        entry.delete(0, "end")

def add_decimal():
    current_text=entry.get()

    if not current_text:
        entry.insert(tk.END,0)
        return
    tokens=current_text.split()

    if tokens and tokens[-1].replace('.','').isdigit and "." not in tokens[-1]:
        entry.insert(tk.END,".")
    elif not tokens[-1].isdigit():
        entry.insert(tk.END,".")

#Butoane
button_clear = tk.Button(frame, text="C", padx=40, pady=20, command=button_clear, font=small_font)
button_clear.grid(row=1, column=0)
button_add_sub = tk.Button(frame, text="+/-", padx=39, pady=20)
button_add_sub.grid(row=1, column=1)
button_percentage = tk.Button(frame, text="%", padx=40, pady=20, command=lambda: button_click("%"))
button_percentage.grid(row=1, column=2)
button_division = tk.Button(frame, text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_division.grid(row=1, column=3)

button_7 = tk.Button(frame, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button_7.grid(row=2, column=0)
button_8 = tk.Button(frame, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button_8.grid(row=2, column=1)
button_9 = tk.Button(frame, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button_9.grid(row=2, column=2)
button_mult = tk.Button(frame, text="*", padx=40, pady=20, command=lambda: button_click("*"), bg="orange", font=small_font)
button_mult.grid(row=2, column=3)

button_4 = tk.Button(frame, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button_4.grid(row=3, column=0)
button_5 = tk.Button(frame, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button_5.grid(row=3, column=1)
button_6 = tk.Button(frame, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button_6.grid(row=3, column=2)
button_subtraction = tk.Button(frame, text="-", padx=40, pady=20, command=lambda: button_click("-"), bg="orange", font=small_font)
button_subtraction.grid(row=3, column=3)

button_1 = tk.Button(frame, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button_1.grid(row=4, column=0)
button_2 = tk.Button(frame, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button_2.grid(row=4, column=1)
button_3 = tk.Button(frame, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button_3.grid(row=4, column=2)
button_addition = tk.Button(frame, text="+", padx=40, pady=20, command=lambda: button_click("+"), bg="orange", font=small_font)
button_addition.grid(row=4, column=3)

button_0 = tk.Button(frame, text="0", padx=40, pady=20, command=lambda: button_click("0"))
button_0.grid(row=5, column=0, columnspan=2)
button_decimal = tk.Button(frame, text=".", padx=40, pady=20, command=add_decimal)
button_decimal.grid(row=5, column=2)
button_equal = tk.Button(frame, text="=", padx=40, pady=20, command=equal, bg="orange", font=small_font)
button_equal.grid(row=5, column=3)

root.mainloop()
