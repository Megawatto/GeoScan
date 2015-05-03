import traceback
from PIL import ImageTk
from setuptools.command.easy_install import easy_install
from img import get_new_gradient_invert
from main import Mains

__author__ = 'Valera'
from tkinter.filedialog import askopenfilename
from tkinter import *


root = Tk()
root.config(bg='white')
root.title('GeoScanHelper_Impl_Python_v0.1')
fr = Frame(root)
fr2 = Frame(root)
images = ImageTk.PhotoImage(file='лого.png')
button_open = Button(fr2, text='open file', width=10, height=2, bg='grey', fg='white', font='arial 14', relief=GROOVE)
button_filter = Button(fr2, text='filter', width=10, height=2, bg='grey', fg='white', font='arial 14', relief=GROOVE)
button_cluster = Button(fr2, text='cluster', width=10, height=2, bg='grey', fg='white', font='arial 14', relief=GROOVE)
# sca = Scale(fr2,orient=HORIZONTAL,length=300, from_=0,to=100,tickinterval=10,resolution=5)
can = Canvas(root, bg="white", height=images.height(), width=images.width(), cursor="pencil", bd=0, highlightthickness=0)
can.create_image(0, 0, anchor=NW, image=images)
root.geometry("%dx%d" % (400, 400))


def create_canvas(size, scale):
    global can
    can.config(height=size[0]*scale, width=size[1])
    root.geometry('%dx%d' % (size[0]*scale+50, size[1]+50))
    global images
    images = ImageTk.PhotoImage(file='test.png')
    can.create_image(0, 0, anchor=NW, image=images)
    can.bind('<B1-Motion>', test)
    can.bind('<Button-1>', test2)
    can.bind('<ButtonRelease-1>', test3)


fx = 0
fy = 0
m = Mains()


def convert(value):
    a = hex(value)
    if len(a) == 3:
        a = '0' + a[2:]
        return a
    return a[2:]



def press_open(event):
    op = askopenfilename()
    if not op is None and not op == '':
        m.parse(op, 2)
        create_canvas(m.size, m.scale)
        print(op)
        button_open.config(relief=RAISED)
    else:
        print('emty')


def press_filter(event):
    print('filter clic')


def test(event):
    can.coords(rec, event.x, event.y, fx, fy)
    print('%d %d %d %d' % (fx, fy, event.x, event.y))


def test2(event):
    global fx, fy
    fx = event.x
    fy = event.y
    global rec
    rec = can.create_rectangle(event.x, event.y, fx, fy, outline='red')
    print(fx)


def test3(event):
    can.delete(rec)


def repain(data):
    pass


button_open.bind('<Button-1>', press_open)
button_filter.bind('<Button-1>', press_filter)
# can.bind('<B1-Motion>', test)
# can.bind('<Button-1>', test2)
# can.bind('<ButtonRelease-1>', test3)
# can.pack(side='top')
fr.pack(side='top')
fr2.pack(side='bottom')
can.pack(side='top')
button_open.pack(side='left')
button_filter.pack(side='right')
button_cluster.pack(side='right')
# sca.pack(side = 'bottom')
root.mainloop()
