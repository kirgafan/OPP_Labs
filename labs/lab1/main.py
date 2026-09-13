from tkinter import *

import module1

# число з повзунка. відміна його не чіпає
text1 = ""
chislo =1

win = Tk()
win.title("Lab1")
win.geometry("520x340+80+80")

Label(win, text="Lab1", font=("Segoe UI", 16)).pack(pady=18)
lbl = Label(win, text="", font=("Segoe UI", 32))
lbl.pack(pady=24)


def robota1():
    global text1, chislo
    r = module1.run(win)
    if r == 0:
        return
    chislo = r
    text1 = str(chislo)
    lbl.config(text=text1)


def robota2():
    pass


menu = Menu(win)
menu.add_command(label="Робота1", command=robota1)
menu.add_command(label="Робота2", command=robota2)
win.config(menu=menu)

if __name__ == "__main__":
    # ЗАПУСК (PowerShell):
    # cd C:\Users\wyxxn\Desktop\LabsOOPMain\labs\lab1
    # python main.py
    win.mainloop()