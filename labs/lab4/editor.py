import os
from tkinter import *
from tkinter import messagebox

from point import PointShape
from line import LineShape
from rect import RectShape
from ellipse import EllipseShape
from line_circles import LineWithCircles
from cube import CubeWireframe


class MyEditor:
    def __init__(self):
        self.figures = []
        self.N = 106
        self.mode = "крапка"
        self.startx = 0
        self.starty = 0
        self.dragging = False
        self.tip = None
        self.tips = {}
        self.imgs = []
        self.checks = {}
        self.win = None
        self.c = None

    def build(self):
        self.win = Tk()
        self.win.title("Lab4")
        self.win.geometry("820x580+40+30")

        here = os.path.dirname(os.path.abspath(__file__))
        self.panel = Frame(self.win)
        self.panel.pack(side=TOP, fill=X)

        self.add_button(os.path.join(here, "point.gif"), "Крапка", "крапка")
        self.add_button(os.path.join(here, "line.gif"), "Лінія", "лінія")
        self.add_button(os.path.join(here, "rect.gif"), "Прямокутник", "прямокутник")
        self.add_button(os.path.join(here, "ellipse.gif"), "Еліпс", "еліпс")
        self.add_button(os.path.join(here, "linecirc.gif"), "Лінія з кружечками", "лінія з кружечками")
        self.add_button(os.path.join(here, "cube.gif"), "Каркас куба", "каркас куба")

        self.c = Canvas(self.win, bg="#d0d0d0")
        self.c.pack(fill=BOTH, expand=True)
        self.c.bind("<ButtonPress-1>", self.on_down)
        self.c.bind("<B1-Motion>", self.on_move)
        self.c.bind("<ButtonRelease-1>", self.on_up)

        menu = Menu(self.win)
        m_file = Menu(menu, tearoff=0)
        m_file.add_command(label="Вихід", command=self.close_app)
        menu.add_cascade(label="Файл", menu=m_file)

        self.m_obj = Menu(menu, tearoff=0, postcommand=self.on_menu)
        self.add_item("Крапка", "крапка")
        self.add_item("Лінія", "лінія")
        self.add_item("Прямокутник", "прямокутник")
        self.add_item("Еліпс", "еліпс")
        self.add_item("Лінія з кружечками", "лінія з кружечками")
        self.add_item("Каркас куба", "каркас куба")
        menu.add_cascade(label="Об'єкти", menu=self.m_obj)

        m_help = Menu(menu, tearoff=0)
        m_help.add_command(label="Про програму", command=self.about)
        menu.add_cascade(label="Довідка", menu=m_help)
        self.win.config(menu=menu)
        self.on_menu()

    def run(self):
        self.build()
        self.win.mainloop()

    def add_item(self, label, mode):
        v = IntVar(value=0)
        self.checks[mode] = v

        def click():
            self.set_mode(mode)

        self.m_obj.add_checkbutton(label=label, variable=v, command=click)

    def add_button(self, path, text, mode):
        img = PhotoImage(file=path)
        self.imgs.append(img)

        def click():
            self.set_mode(mode)

        b = Button(self.panel, image=img, command=click)
        b.pack(side=LEFT, padx=3, pady=3)
        self.tips[b] = text
        b.bind("<Enter>", self.OnNotify)
        b.bind("<Leave>", self.hide_tip)

    def OnNotify(self, e):
        if e.widget in self.tips:
            text = self.tips[e.widget]
        else:
            return
        self.hide_tip(None)
        x = e.widget.winfo_rootx() - self.win.winfo_rootx() + 4
        y = e.widget.winfo_rooty() - self.win.winfo_rooty() + e.widget.winfo_height() + 2
        t = Label(self.win, text=text, bg="#fff8c4", relief=SOLID, bd=1)
        t.place(x=x, y=y)
        t.lift()
        self.tip = t

    def hide_tip(self, e):
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

    def redraw(self):
        self.c.delete("all")
        for i in range(len(self.figures)):
            self.figures[i].Show(self.c)

    def trail(self, x, y):
        self.c.delete("temp")
        self.make_shape(x, y).Show(self.c, preview=True)

    def make_shape(self, x, y):
        if self.mode == "крапка":
            obj = PointShape()
            obj.set(x, y, x, y)
        elif self.mode == "лінія":
            obj = LineShape()
            obj.set(self.startx, self.starty, x, y)
        elif self.mode == "прямокутник":
            obj = RectShape()
            obj.set(self.startx, self.starty, x, y)
        elif self.mode == "еліпс":
            obj = EllipseShape()
            obj.set(self.startx, self.starty, x, y)
        elif self.mode == "лінія з кружечками":
            obj = LineWithCircles()
            obj.set(self.startx, self.starty, x, y)
        else:
            obj = CubeWireframe()
            obj.set(self.startx, self.starty, x, y)
        return obj

    def on_down(self, e):
        self.startx = e.x
        self.starty = e.y
        self.dragging = True

    def on_move(self, e):
        if self.dragging == False:
            return
        self.trail(e.x, e.y)

    def on_up(self, e):
        if self.dragging == False:
            return
        self.dragging = False
        self.c.delete("temp")
        if len(self.figures) >= self.N:
            return
        self.figures.append(self.make_shape(e.x, e.y))
        self.redraw()

    def close_app(self):
        self.win.destroy()

    def about(self):
        messagebox.showinfo("Довідка", "Lab4. Кузнецов Кирило, група IM-о51")


# глобальний статичний об'єкт, ще не singleton
editor = MyEditor()
