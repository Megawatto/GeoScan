class Point:
    x = 0
    y = 0
    value = 0
    deep = 0
    desc = ''

    def __init__(self, x, y , value):
        print('create point %d' % (id(self)))
        self.x = x
        self.y = y
        self.value = value

    def set_param_point(self, deep, desc):
        self.deep = deep
        self.desc = desc
