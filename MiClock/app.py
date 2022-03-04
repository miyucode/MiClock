from tkinter import *
from time import *

w = Tk()
w.title("MiClock")
w.geometry("370x100")
w.resizable(False, False)
w.iconbitmap("icons/clock.ico")

l = Label(w, font=("Arial", 68, "bold"), bg="grey", fg="white")
l.pack(anchor="center", expand=True)

def update():
	t = strftime("%H:%M:%S")
	l.config(text=t)
	w.after(1000, update)

update()
w.mainloop()