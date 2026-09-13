# робота1 - горизонтальний повзунок, число 1..100

from tkinter import *

_chislo = 1
_kod = 0


def _ruh(val):
    global _chislo
    _chislo = int(float(val))


def run(parent):
    global _chislo, _kod
    _chislo = 1
    _kod = 0

    d = Toplevel(parent)
    d.title("Робота1")
    d.geometry("340x160+200+160")
    d.resizable(False, False)
    d.transient(parent)

    Label(d, text="Виберіть число від 1 до 100").pack(pady=8)

    sc = Scale(d, from_=1, to=100, orient=HORIZONTAL, length=300, command=_ruh)
    sc.set(1)
    sc.pack()

    def tak():
        global _chislo, _kod
        _chislo = int(sc.get())
        _kod = 1
        d.destroy()

    def vidmina():
        global _kod
        _kod = 0
        d.destroy()

    d.protocol("WM_DELETE_WINDOW", vidmina)

    bf = Frame(d)
    bf.pack(pady=8)
    Button(bf, text="Так", width=12, command=tak).pack(side=LEFT, padx=8)
    Button(bf, text="Відміна", width=12, command=vidmina).pack(side=LEFT, padx=8)

    d.grab_set()
    parent.wait_window(d)
    if _kod == 1:
        return _chislo
    return 0
