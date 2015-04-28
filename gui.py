from setuptools.command.easy_install import easy_install

__author__ = 'Valera'
from tkinter.filedialog import askopenfilename
from tkinter import *


root = Tk()
root.geometry("1000x600")
button_open = Button(root, text='open file', width=10, height=2, bg='black', fg='red', font='arial 14')
button_filter = Button(root, text='filter', width=10, height=2, bg='black', fg='red', font='arial 14')
can = Canvas(root, bg="lightblue", height=500, width=500, cursor="pencil")

fx = 0
fy = 0

def opens(event):
    op = askopenfilename()
    print(op)

def test(event):
    can.coords(rec, event.x, event.y ,fx , fy)
    print('%d %d %d %d' % (fx,fy,event.x,event.y))

def test2(event):
    global  fx, fy
    fx = event.x
    fy = event.y
    global rec
    rec = can.create_rectangle(event.x, event.y, fx, fy,)
    print(fx)

def test3(event):
    can.delete(rec)

def repain(data):
    pass


button_open.bind('<Button-1>', opens)
can.bind('<B1-Motion>', test)
can.bind('<Button-1>', test2)
can.bind('<ButtonRelease-1>', test3)
can.pack(side='top')
button_open.pack(side='right')
button_filter.pack(side='right')
root.mainloop()
