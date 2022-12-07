import tkinter as tk

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def add_digit(digit):
    value = calc_field.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc_field.delete(0, END)
    calc_field.insert(0, value + digit)

def add_operation(operation):
    value = calc_field.get()
    if value[-1] in '-+/*':
        calc_field.delete(len(value)-1)
    elif '+' in value or '-' in value or '*' in value or '+' in value:
        calculate()
        value = calc_field.get()
    calc_field.insert(tk.END, operation)

def calculate():
    try:
        value = calc_field.get()
        if value[-1] in '+-*/':
            value = value + value[:-1]
        calc_field.delete(0, END)
        calc_field.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Division by zero', 'inf')
        calc_field.insert(0, '0')
    except (NameError, SyntaxError):
        messagebox.showinfo('Error', 'Non-numeric characters are not supported')
        calc_field.insert(0, '0')


def clear():
    calc_field.delete(0, END)
    calc_field.insert(0, '0')


def make_digit_button(digit):
    return Button(tab1, text=digit, bd=5, font=('Arial',13), command=lambda : add_digit(digit))

def make_operation_button(op):
    return Button(tab1, text=op, bd=5, font=('Arial',13), fg='green',command=lambda : add_operation(op))

def make_calc_button(op):
    return Button(tab1, text=op, bd=5, font=('Arial',13), fg='green',command=calculate)

def make_clear_button(op):
    return Button(tab1, text=op, bd=5, font=('Arial',13), fg='green',command=clear)

window = Tk()
window.title("Window Name")

window.geometry('800x600')
window.resizable(width=False, height=False)

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Calculator')
tab_control.add(tab2, text='ChexBox')
tab_control.add(tab3, text='Text')




# ----------------------------------------------
# Вкладка с калькулятором
calc_field = Entry(tab1, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc_field.insert(0, '0')
calc_field.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)


tab1.grid_columnconfigure(0, minsize=60)
tab1.grid_columnconfigure(1, minsize=60)
tab1.grid_columnconfigure(2, minsize=60)
tab1.grid_columnconfigure(3, minsize=60)

tab1.rowconfigure(1, minsize=60)
tab1.rowconfigure(2, minsize=60)
tab1.rowconfigure(3, minsize=60)
tab1.rowconfigure(4, minsize=60)
tab1.rowconfigure(5, minsize=60)
tab1.rowconfigure(6, minsize=60)



# Вкладка с CheckBox
def first_label():
    messagebox.showinfo('Message', 'You have chosen the first button')

def second_label():
    messagebox.showinfo('Message', 'You have chosen the second button')

def third_label():
    messagebox.showinfo('Message', 'You have chosen the third button')

var = IntVar()
var.set(0)

Radiobutton(tab2,text="First", command=first_label, variable=var, value=0).grid()
Radiobutton(tab2, text="Second", command=second_label,variable=var, value=1).grid()
Radiobutton(tab2, text="Third", command=third_label,variable=var, value=2).grid()



# Вкладка работы с текстом
def load_text():
    with open('pr10_output_november.txt', 'r') as file:
        lst = file.readlines()

    listbox.delete(0, END)
    for item in lst:
        listbox.insert(END, item)
    file.close()

load_btn = Button(tab3, text="Upload text", bd=5, font=('Arial',13), fg='green',command=load_text).grid()

listbox = Listbox(tab3, width=40, height=20)
listbox.grid()
listbox.insert(END, "Contents of the file pr10_output_november.txt")

# ----------------------------------------------
tab_control.pack(expand=1, fill='both')
window.mainloop()
