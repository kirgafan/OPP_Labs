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
        self.dragging = False
        self.tip = None
        self.tips = {}
        self.imgs = []
        self.checks = {}

        self.win = Tk()
        self.win.title("Lab3")
        self.win.geometry("780x560+60+40")

        here = os.path.dirname(os.path.abspath(__file__))
        # кнопки без тексту, тільки картинка
        self.panel = Frame(self.win)
        self.panel.pack(side=TOP, fill=X)

        self.add_button(os.path.join(here, "point.gif"), "Крапка", "крапка")
        self.add_button(os.path.join(here, "line.gif"), "Лінія", "лінія")
        self.add_button(os.path.join(here, "rect.gif"), "Прямокутник", "прямокутник")
        self.add_button(os.path.join(here, "ellipse.gif"), "Еліпс", "еліпс")

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
        menu.add_cascade(label="Об'єкти", menu=self.m_obj)

        m_help = Menu(menu, tearoff=0)
        m_help.add_command(label="Про програму", command=self.about)
        menu.add_cascade(label="Довідка", menu=m_help)
        self.win.config(menu=menu)
        self.on_menu()

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

    def on_down(self, e):
        self.startx = e.x
        self.starty = e.y
        self.dragging = True

    def on_move(self, e):
        if self.dragging == False:
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
        if self.dragging == False:
            return
        self.dragging = False
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
        self.redraw()

    def close_app(self):
        self.win.destroy()

    def about(self):
        messagebox.showinfo("Довідка", "Lab3. Кузнецов Кирило, група IM-о51")


app = MainWin()

if __name__ == "__main__":
    # ЗАПУСК (PowerShell):
    # cd C:\Users\wyxxn\Desktop\LabsOOPMain\labs\lab3
    # python Lab3.py
    app.win.mainloop()
