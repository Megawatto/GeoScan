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
root.title('GeoScanHelper_Python_v0.13')
root.geometry("%dx%d" % (550, 420))
fr = Frame(root)
fr2 = Frame(root, bg='white')
images = ImageTk.PhotoImage(file='лого.png')
button_open = Button(fr2, text='open file', width=10, height=2, bg='#0080FF', fg='white', font='Alabama 14', relief=GROOVE)
button_filter = Button(fr2, text='filter', width=10, height=2, bg='#0080FF', fg='white', font='Alabama 14', relief=GROOVE , state = DISABLED)
button_cluster = Button(fr2, text='cluster', width=10, height=2, bg='#0080FF', fg='white', font='Alabama 14', relief=GROOVE, state = DISABLED)
sca = Scale(fr2, orient=HORIZONTAL,length=100, from_=1,to=3, resolution=1, bg ='#0080FF', fg = "white",label = 'Scale',font='Alabama 11', relief=GROOVE)
can = Canvas(root, bg="white", height=images.height(), width=images.width(),  bd=0, highlightthickness=0)
can.create_image(0, 0, anchor=NW, image=images)


def create_canvas():
    global can
    global images
    global limit_box
    limit_box = [0, 0, 0, 0]
    images = ImageTk.PhotoImage(file='test.png')
    if (images.width() + 50) < 550:
        siz = 550
    else:
        siz = images.width()
    root.geometry('%dx%d' % (siz+50, images.height()+100))
    print('size img',images.height(), images.width())
    #todo смотри fixme по левый\правый
    limit_box = [0, images.height(), 0, images.width()]
    print(limit_box)
    can.config(height=images.height(), width=images.width(), cursor="pencil", bg ='blue')
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


def press_open(event=0):
    op = askopenfilename(filetypes=[("CSV", "*.csv")])
    global button_filter, button_cluster
    button_filter.config(state=NORMAL)
    button_cluster.config(state=NORMAL)
    if not op is None and not op == '':
        root.update()
        can.config(cursor='watch')
        m.parse(op, sca.get())
        create_canvas()
        print(op)
        # button_open.config(relief=RAISED)
    else:
        print('emty')


def press_filter(event = 0):
    print('filter click')
    m.start_filter(limit_box)
    repain()

def press_cluster(event = 0):
    print('cluster click')


def press_scale(var):
    # global sca
    # print(sca.get())
    print('sc',var)

def test(event):
    can.coords(rec, event.x, event.y, fx, fy)
    print('fx_%d fy_%d ex_%d e_y%d' % (fx, fy, event.x, event.y))
    global limit_box
    up_x = fy
    d_x = event.y
    l_y = fx
    r_y = event.x
    if fy > event.y:
        up_x = event.y
        d_x = fy
    if fx < event.x:
        l_y = event.x
        r_y = fx
    limit_box = [up_x, d_x, (images.width() - l_y)/sca.get(), (images.width() - r_y)/sca.get()]
    # limit_box = [fy, event.y, (images.width() - fx)/sca.get(), (images.width() - event.x)/sca.get()]
    print(limit_box)


def test2(event):
    global fx, fy
    fx = event.x
    fy = event.y
    global rec
    rec = can.create_rectangle(event.x, event.y, fx, fy, outline='red')
    print(fx, fy)


def test3(event):
    can.delete(rec)
    print(limit_box)
    m.start_filter(limit_box)
    repain()


def repain():
    create_canvas()

#todo дописать вывод
def out_result():
    global top
    top = Toplevel(root)
    top.title('Result')
    lab = Label(top, text="MaZaFaKa").pack()

# button_open.bind('<Button-1>', press_open)
button_open.config(command=press_open)
# button_filter.bind('<Button-1>', press_filter)
button_filter.config(command=press_filter)
# button_cluster.bind('<Button-1>', press_cluster)
button_cluster.config(command=press_cluster)
# can.bind('<B1-Motion>', test)
# can.bind('<Button-1>', test2)
# can.bind('<ButtonRelease-1>', test3)
# can.pack(side='top')


sca.config(command=press_scale)

fr.pack(side='top')
fr2.pack(side='bottom')
can.pack(side='top')
button_open.pack(side='left', pady =10)
button_filter.pack(side='right')
button_cluster.pack(side='right')
sca.pack(side = 'right')
root.mainloop()
