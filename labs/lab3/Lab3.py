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

        self.win = Tk()
        self.win.title(self.mode)
        self.win.geometry("780x560+60+40")

        self.c = Canvas(self.win, bg="#d0d0d0")
        self.c.pack(fill=BOTH, expand=True)
        self.c.bind("<ButtonPress-1>", self.on_down)
        self.c.bind("<ButtonRelease-1>", self.on_up)

        menu = Menu(self.win)
        m_file = Menu(menu, tearoff=0)
        m_file.add_command(label="Вихід", command=self.vyhod)
        menu.add_cascade(label="Файл", menu=m_file)

        m_obj = Menu(menu, tearoff=0)
        m_obj.add_command(label="Крапка", command=self.krapka)
        m_obj.add_command(label="Лінія", command=self.liniya)
        m_obj.add_command(label="Прямокутник", command=self.pryam)
        m_obj.add_command(label="Еліпс", command=self.elips)
        menu.add_cascade(label="Об'єкти", menu=m_obj)

        m_help = Menu(menu, tearoff=0)
        m_help.add_command(label="Про програму", command=self.pro)
        menu.add_cascade(label="Довідка", menu=m_help)
        self.win.config(menu=menu)

    def krapka(self):
        self.set_mode("крапка")

    def liniya(self):
        self.set_mode("лінія")

    def pryam(self):
        self.set_mode("прямокутник")

    def elips(self):
        self.set_mode("еліпс")

    def set_mode(self, mode):
        self.mode = mode
        self.win.title(mode)

    def peremaluvaty(self):
        self.c.delete("all")
        for i in range(len(self.figures)):
            self.figures[i].Show(self.c)

    def on_down(self, e):
        self.startx = e.x
        self.starty = e.y
        self.tyagnu = True

    def on_up(self, e):
        if self.tyagnu == False:
            return
        self.tyagnu = False
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
app.win.mainloop()
