from customtkinter import *

window = CTk()
window.geometry("400x400")
window.title("Click")

count=0
def click():
    global count
    count = count + 1
    lable.configure(text=f"{count}")

lable = CTkLabel(window, text="0")
lable.pack()

btn = CTkButton(window, text="Click", width=300, height=300, command=click)
btn.pack()




window.mainloop()
