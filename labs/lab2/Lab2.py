from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Lab2")
win.geometry("780x560+60+40")

c = Canvas(win, bg="#d0d0d0")
c.pack(fill=BOTH, expand=True)


def vyhod():
    win.destroy()


def pro_programu():
    messagebox.showinfo("Довідка", "Lab2. Кузнецов Кирило, група IM-о51")


menu = Menu(win)
m_file = Menu(menu, tearoff=0)
m_file.add_command(label="Вихід", command=vyhod)
menu.add_cascade(label="Файл", menu=m_file)

m_obj = Menu(menu, tearoff=0)
m_obj.add_command(label="Крапка")
m_obj.add_command(label="Лінія")
m_obj.add_command(label="Прямокутник")
m_obj.add_command(label="Еліпс")
menu.add_cascade(label="Об'єкти", menu=m_obj)

m_help = Menu(menu, tearoff=0)
m_help.add_command(label="Про програму", command=pro_programu)
menu.add_cascade(label="Довідка", menu=m_help)
win.config(menu=menu)

if __name__ == "__main__":
    win.mainloop()
