from tkinter import *

win = Tk()
win.title("Lab1")
win.geometry("520x340+80+80")

Label(win, text="Lab1", font=("Segoe UI", 16)).pack(pady=18)

def robota1():
    pass

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