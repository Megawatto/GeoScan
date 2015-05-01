import traceback
from setuptools.command.easy_install import easy_install
from img import get_new_gradient_invert, img
from main import Mains

__author__ = 'Valera'
from tkinter.filedialog import askopenfilename
from tkinter import *


root = Tk()
root.geometry("400x400")
root.title('GeoScanHelper_Impl_Python_v0.1')
button_open = Button(root, text='open file', width=10, height=2, bg='black', fg='red', font='arial 14')
button_filter = Button(root, text='filter', width=10, height=2, bg='black', fg='red', font='arial 14')
can = 0


def create_canvas(size):
    global can
    if not can == 0:
        can.config(height=size[0], width=size[1])
    else:
        root.update()
        can = Canvas(root, bg="lightblue", height=size[0], width=size[1], cursor="pencil")
        can.create_rectangle(0, 0, size[1], size[0], outline="black")
        # can.create_line(50,50,51,51, fill = ('#%s%s%s' % (convert(255), convert(0), convert(0))))
    print(id(can))
    can.bind('<B1-Motion>', test)
    can.bind('<Button-1>', test2)
    can.bind('<ButtonRelease-1>', test3)
    can.pack(side='top')


fx = 0
fy = 0
m = Mains()


def convert(value):
    a = hex(value)
    if len(a) == 3:
        a = '0' + a[2:]
        return a
    return a[2:]


def logic():
    try:
        print('start')
        m.parse('test.csv')
        # m.starter('4.csv')
        # m.starter('test.csv')
    except Exception:
        print(traceback.print_exc())


def opens(event):
    op = askopenfilename()
    m.parse(op)
    create_canvas(m.size)
    paint_pixel(m.data)
    print(op)


def paint_pixel(data):
    global can
    lim_y = len(data)
    lim_x = len(data[0])
    for y in range(0, lim_y):
        print(y)
        for x in range(0, lim_x):
            # print(x)
            gp = convert(get_gp(data[y][x]))
            can.create_line(x, y, x+1, y+1, fill=('#%s%s%s' % (gp,gp,gp)))
            root.update()
            # print('work')


def get_gp(value):
    gp = get_new_gradient_invert(100, -5000, 5000, value)
    # gp = img.get_new_gradient_invert(100, -12500, 4000, value)
    return gp


def test(event):
    can.coords(rec, event.x, event.y, fx, fy)
    print('%d %d %d %d' % (fx, fy, event.x, event.y))


def test2(event):
    global fx, fy
    fx = event.x
    fy = event.y
    global rec
    rec = can.create_rectangle(event.x, event.y, fx, fy, )
    print(fx)


def test3(event):
    can.delete(rec)


def repain(data):
    pass


button_open.bind('<Button-1>', opens)
# can.bind('<B1-Motion>', test)
# can.bind('<Button-1>', test2)
# can.bind('<ButtonRelease-1>', test3)
# can.pack(side='top')
button_open.pack(side='right')
button_filter.pack(side='right')
root.mainloop()
