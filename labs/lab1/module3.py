# друге вікно роботи2: назад, так, відміна

from tkinter import *

kod = 0


def run(parent):
    global kod
    kod = 0

    w = Toplevel(parent)
    w.title("Робота2")
    w.geometry("380x120+240+200")
    w.resizable(False, False)
    w.transient(parent)

    Label(w, text="Друге вікно").pack(pady=10)

    def nazad():
        global kod
        kod = -1
        w.destroy()

    def tak():
        global kod
        kod = 1
        w.destroy()

    def vidmina():
        global kod
        kod = 0
        w.destroy()

    w.protocol("WM_DELETE_WINDOW", vidmina)

    row = Frame(w)
    row.pack(pady=4)
    Button(row, text="< Назад", width=10, command=nazad).pack(side=LEFT, padx=6)
    Button(row, text="Так", width=10, command=tak).pack(side=LEFT, padx=6)
    Button(row, text="Відміна", width=10, command=vidmina).pack(side=LEFT, padx=6)

    w.grab_set()
    parent.wait_window(w)
    return kod
