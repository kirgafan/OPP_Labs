# перше вікно роботи2, кнопки Далі і Відміна

from tkinter import *

vidp = 0


def run(parent):
    global vidp
    vidp = 0

    top = Toplevel(parent)
    top.title("Робота2")
    top.geometry("300x120+220+180")
    top.resizable(False, False)
    top.transient(parent)

    Label(top, text="Перше вікно").pack(pady=12)

    def dali():
        global vidp
        vidp = 1
        top.destroy()

    def vidmina():
        global vidp
        vidp = 0
        top.destroy()

    top.protocol("WM_DELETE_WINDOW", vidmina)

    row = Frame(top)
    row.pack()
    Button(row, text="Далі", width=12, command=dali).pack(side=LEFT, padx=6)
    Button(row, text="Відміна", width=12, command=vidmina).pack(side=LEFT, padx=6)

    top.grab_set()
    parent.wait_window(top)
    return vidp
