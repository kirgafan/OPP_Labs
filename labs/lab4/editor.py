import os
from tkinter import *
from tkinter import messagebox


class MyEditor:
    def __init__(self):
        self.mode = "крапка"
        self.checks = {}
        self.win = None
        self.c = None

    def build(self):
        self.win = Tk()
        self.win.title("Lab4")
        self.win.geometry("820x580+40+30")

        self.c = Canvas(self.win, bg="#d0d0d0")
        self.c.pack(fill=BOTH, expand=True)

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

    def run(self):
        self.build()
        self.win.mainloop()

    def add_item(self, label, mode):
        v = IntVar(value=0)
        self.checks[mode] = v

        def click():
            self.set_mode(mode)

        self.m_obj.add_checkbutton(label=label, variable=v, command=click)

    def on_menu(self):
        for mode in self.checks:
            if mode == self.mode:
                self.checks[mode].set(1)
            else:
                self.checks[mode].set(0)

    def set_mode(self, mode):
        self.mode = mode
        self.on_menu()

    def close_app(self):
        self.win.destroy()

    def about(self):
        messagebox.showinfo("Довідка", "Lab4. Кузнецов Кирило, група IM-о51")


# глобальний статичний об'єкт, ще не singleton
editor = MyEditor()
