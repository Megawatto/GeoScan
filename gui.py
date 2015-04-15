
__author__ = 'Valera'
from tkinter.filedialog import askopenfilename
from tkinter import *
import main
import img


root = Tk()
_main = main.Mains()
button_open = Button(root, text='open file', width=10, height=2, bg='black', fg='red', font='arial 14')
button_filter = Button(root, text='filter', width=10, height=2, bg='black', fg='red', font='arial 14')
can = Canvas(root, bg="white", height=500, width=500)


def opens(event):
    op = askopenfilename()
    _main.starter(op)
    repain(_main.data)
    print(op)

def repain(data):
    pass


button_open.bind('<Button-1>', opens)

can.pack(side='top')
button_open.pack(side='right')
button_filter.pack(side='right')
root.mainloop()
