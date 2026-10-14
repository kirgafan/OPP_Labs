from tkinter import *
from tkinter import messagebox

from point import PointShape
from line import LineShape
from rect import RectShape
from ellipse import EllipseShape

# слід - червоний суцільний
figures = [None] * 105
n =0
rezhym = "крапка"
startx = 0
starty = 0
tyagnu = False

win = Tk()
win.title("крапка")
win.geometry("780x560+60+40")

c = Canvas(win, bg="#d0d0d0")
c.pack(fill=BOTH, expand=True)


def peremaluvaty():
    c.delete("all")
    for i in range(n):
        figures[i].Show(c)


def postavyty(name):
    global rezhym
    rezhym = name
    win.title(name)


def na_press(e):
    global startx, starty, tyagnu
    startx = e.x
    starty = e.y
    tyagnu = True


def na_ruh(e):
    global tyagnu
    if tyagnu == False:
        return
    c.delete("temp")
    if rezhym == "крапка":
        c.create_oval(e.x - 4, e.y - 4, e.x + 4, e.y + 4, outline="red", tags="temp")
    elif rezhym == "лінія":
        c.create_line(startx, starty, e.x, e.y, fill="red", width=2, tags="temp")
    elif rezhym == "прямокутник":
        dx = e.x - startx
        if dx < 0:
            dx = -dx
        dy = e.y - starty
        if dy < 0:
            dy = -dy
        c.create_rectangle(startx - dx, starty - dy, startx + dx, starty + dy, outline="red", width=2, tags="temp")
    elif rezhym == "еліпс":
        c.create_oval(startx, starty, e.x, e.y, outline="red", width=2, tags="temp")


def na_release(e):
    global n, tyagnu
    if tyagnu == False:
        return
    tyagnu = False
    c.delete("temp")
    if n >= 105:
        return

    if rezhym == "крапка":
        obj = PointShape()
        obj.set(e.x, e.y, e.x, e.y)
    elif rezhym == "лінія":
        obj = LineShape()
        obj.set(startx, starty, e.x, e.y)
    elif rezhym == "прямокутник":
        obj = RectShape()
        obj.set(startx, starty, e.x, e.y)
    else:
        obj = EllipseShape()
        obj.set(startx, starty, e.x, e.y)

    figures[n] = obj
    n = n + 1
    peremaluvaty()


def vyhod():
    win.destroy()


def pro_programu():
    messagebox.showinfo("Довідка", "Lab2. Кузнецов Кирило, група IM-о51")


c.bind("<ButtonPress-1>", na_press)
c.bind("<B1-Motion>", na_ruh)
c.bind("<ButtonRelease-1>", na_release)

menu = Menu(win)
m_file = Menu(menu, tearoff=0)
m_file.add_command(label="Вихід", command=vyhod)
menu.add_cascade(label="Файл", menu=m_file)

def vyb_krapka():
    postavyty("крапка")


def vyb_liniya():
    postavyty("лінія")


def vyb_pryam():
    postavyty("прямокутник")


def vyb_elips():
    postavyty("еліпс")


m_obj = Menu(menu, tearoff=0)
m_obj.add_command(label="Крапка", command=vyb_krapka)
m_obj.add_command(label="Лінія", command=vyb_liniya)
m_obj.add_command(label="Прямокутник", command=vyb_pryam)
m_obj.add_command(label="Еліпс", command=vyb_elips)
menu.add_cascade(label="Об'єкти", menu=m_obj)

m_help = Menu(menu, tearoff=0)
m_help.add_command(label="Про програму", command=pro_programu)
menu.add_cascade(label="Довідка", menu=m_help)
win.config(menu=menu)

if __name__ == "__main__":
    # ЗАПУСК (PowerShell):
    # cd C:\Users\wyxxn\Desktop\LabsOOPMain\labs\lab2
    # python Lab2.py
    win.mainloop()
