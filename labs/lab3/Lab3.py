import os
from tkinter import *
from tkinter import messagebox

from point import PointShape
from line import LineShape
from rect import RectShape
from ellipse import EllipseShape


class MainWin:
    def __init__(self):
        self.figures = []
        self.N = 106
        self.mode = "крапка"
        self.startx = 0
        self.starty = 0
        self.tyagnu = False
        self.tip = None
        self.pidkazka = {}
        self.imgs = []
        self.checks = {}

        self.win = Tk()
        self.win.title("Lab3")
        self.win.geometry("780x560+60+40")

        here = os.path.dirname(os.path.abspath(__file__))
        # кнопки без тексту, тільки картинка
        self.panel = Frame(self.win)
        self.panel.pack(side=TOP, fill=X)

        self.dodaty_knopku(os.path.join(here, "point.gif"), "Крапка", "крапка")
        self.dodaty_knopku(os.path.join(here, "line.gif"), "Лінія", "лінія")
        self.dodaty_knopku(os.path.join(here, "rect.gif"), "Прямокутник", "прямокутник")
        self.dodaty_knopku(os.path.join(here, "ellipse.gif"), "Еліпс", "еліпс")

        self.c = Canvas(self.win, bg="#d0d0d0")
        self.c.pack(fill=BOTH, expand=True)
        self.c.bind("<ButtonPress-1>", self.on_down)
        self.c.bind("<B1-Motion>", self.on_move)
        self.c.bind("<ButtonRelease-1>", self.on_up)

        menu = Menu(self.win)
        m_file = Menu(menu, tearoff=0)
        m_file.add_command(label="Вихід", command=self.vyhod)
        menu.add_cascade(label="Файл", menu=m_file)

        self.m_obj = Menu(menu, tearoff=0, postcommand=self.on_menu)
        self.dodaty_punkt("Крапка", "крапка")
        self.dodaty_punkt("Лінія", "лінія")
        self.dodaty_punkt("Прямокутник", "прямокутник")
        self.dodaty_punkt("Еліпс", "еліпс")
        menu.add_cascade(label="Об'єкти", menu=self.m_obj)

        m_help = Menu(menu, tearoff=0)
        m_help.add_command(label="Про програму", command=self.pro)
        menu.add_cascade(label="Довідка", menu=m_help)
        self.win.config(menu=menu)
        self.on_menu()

    def dodaty_punkt(self, label, mode):
        v = IntVar(value=0)
        self.checks[mode] = v

        def klik():
            self.set_mode(mode)

        self.m_obj.add_checkbutton(label=label, variable=v, command=klik)

    def dodaty_knopku(self, path, text, mode):
        img = PhotoImage(file=path)
        self.imgs.append(img)

        def klik():
            self.set_mode(mode)

        b = Button(self.panel, image=img, command=klik)
        b.pack(side=LEFT, padx=3, pady=3)
        self.pidkazka[b] = text
        b.bind("<Enter>", self.OnNotify)
        b.bind("<Leave>", self.spryaty_pidkazku)

    def OnNotify(self, e):
        if e.widget in self.pidkazka:
            text = self.pidkazka[e.widget]
        else:
            return
        self.spryaty_pidkazku(None)
        x = e.widget.winfo_rootx() - self.win.winfo_rootx() + 4
        y = e.widget.winfo_rooty() - self.win.winfo_rooty() + e.widget.winfo_height() + 2
        t = Label(self.win, text=text, bg="#fff8c4", relief=SOLID, bd=1)
        t.place(x=x, y=y)
        t.lift()
        self.tip = t

    def spryaty_pidkazku(self, e):
        if self.tip != None:
            self.tip.destroy()
            self.tip = None

    def on_menu(self):
        for mode in self.checks:
            if mode == self.mode:
                self.checks[mode].set(1)
            else:
                self.checks[mode].set(0)

    def set_mode(self, mode):
        self.mode = mode
        self.on_menu()

    def peremaluvaty(self):
        self.c.delete("all")
        for i in range(len(self.figures)):
            self.figures[i].Show(self.c)

    def on_down(self, e):
        self.startx = e.x
        self.starty = e.y
        self.tyagnu = True

    def on_move(self, e):
        if self.tyagnu == False:
            return
        self.c.delete("temp")
        if self.mode == "крапка":
            self.c.create_oval(e.x - 4, e.y - 4, e.x + 4, e.y + 4, outline="blue", tags="temp")
        elif self.mode == "лінія":
            self.c.create_line(self.startx, self.starty, e.x, e.y, fill="blue", width=2, tags="temp")
        elif self.mode == "прямокутник":
            self.c.create_rectangle(self.startx, self.starty, e.x, e.y, outline="blue", width=2, tags="temp")
        elif self.mode == "еліпс":
            dx = e.x - self.startx
            if dx < 0:
                dx = -dx
            dy = e.y - self.starty
            if dy < 0:
                dy = -dy
            self.c.create_oval(self.startx - dx, self.starty - dy, self.startx + dx, self.starty + dy, outline="blue", width=2, tags="temp")

    def on_up(self, e):
        if self.tyagnu == False:
            return
        self.tyagnu = False
        self.c.delete("temp")
        if len(self.figures) >= self.N:
            return

        if self.mode == "крапка":
            obj = PointShape()
            obj.set(e.x, e.y, e.x, e.y)
        elif self.mode == "лінія":
            obj = LineShape()
            obj.set(self.startx, self.starty, e.x, e.y)
        elif self.mode == "прямокутник":
            obj = RectShape()
            obj.set(self.startx, self.starty, e.x, e.y)
        else:
            obj = EllipseShape()
            obj.set(self.startx, self.starty, e.x, e.y)

        self.figures.append(obj)
        self.peremaluvaty()

    def vyhod(self):
        self.win.destroy()

    def pro(self):
        messagebox.showinfo("Довідка", "Lab3. Кузнецов Кирило, група IM-о51")


app = MainWin()

if __name__ == "__main__":
    # ЗАПУСК (PowerShell):
    # cd C:\Users\wyxxn\Desktop\LabsOOPMain\labs\lab3
    # python Lab3.py
    app.win.mainloop()
