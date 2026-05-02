from customtkinter import *

window = CTk()
window.geometry("500x500")
window.title("Calcurator")
print("hhhhhhhhh")
entry = CTkEntry(window, width=150)
entry.grid(column=1, row=0, columnspan=3, padx=5, pady=7)
def add_1():
    entry.insert("end", 1)

def add_2():
    entry.insert("end", 2)

def add_3():
    entry.insert("end", 3)

def add_4():
    entry.insert("end", 4)

def add_5():
    entry.insert("end", 5)

def add_6():
    entry.insert("end", 6)

def add_7():
    entry.insert("end", 7)

def add_8():
    entry.insert("end", 8)

def add_9():
    entry.insert("end", 9)

def add():
    entry.insert("end", "+")

def multiply():
    entry.insert("end", "*")

def do_math():
    res= eval(entry.get())
    entry.delete(0, 'end')
    entry.insert(0, str(res))

btn1=CTkButton(window, text="1", width=50, command=add_1)
btn1.grid( row=1, column =0)

btn2=CTkButton(window, text="2", width=50, command=add_2)
btn2.grid( row=1, column =1)

btn3=CTkButton(window, text="3", width=50, command=add_3)
btn3.grid( row=1, column =2)

btn4=CTkButton(window, text="4", width=50, command=add_4)
btn4.grid( row=1, column =3)

btn5=CTkButton(window, text="5", width=50, command=add_5)
btn5.grid( row=1, column =4)

btn6=CTkButton(window, text="6", width=50, command=add_6)
btn6.grid( row=1, column =5)

btn7=CTkButton(window, text="7", width=50, command=add_7)
btn7.grid( row=1, column =6)

btn8=CTkButton(window, text="8", width=50, command=add_8)
btn8.grid( row=1, column =7)

btn9=CTkButton(window, text="9", width=50, command=add_9)
btn9.grid( row=1, column =8)


btn_plus=CTkButton(window, text="+", width=50, command=add)
btn_plus.grid( row=2, column =3)

btn_equal = CTkButton(window, text="=", width=50, command=do_math)
btn_equal.grid( row=2, column =4)

btn_equal1 = CTkButton(window, text="*", width=50, command=multiply)
btn_equal1.grid( row=2, column =5)



window.mainloop()