class Point:
    x = 0
    y = 0
    value = 0
    deep = 0
    time_trace = ''

    def __init__(self, x, y , value):
        print('create point %d' % (id(self)))
        self.x = x
        self.y = y
        self.value = value

    def set_param_point(self, deep, desc):
        self.deep = deep
        self.time_trace = desc

    def print_status(self):
        print('<x=%d y=%d v=%d d=%d tt=%s>' % (self.x, self.y, self.value, self.deep, self.time_trace))
