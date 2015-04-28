import math

__author__ = 'Valera'
import csv
import sys
from filter import Filter
from wrapper import Wrapper
import img


class Handler:
    out = []
    wrappers = Wrapper()

    def parse(self, url):
        print('parse')
        try:
            row = 0
            file = open(url)
            reader = csv.reader(x.replace('\0', '').replace(' ', '') for x in file)
            for x in reader:
                if len(x) == 0:
                    print(x)
                else:
                    if len(x) == 1:
                        print(x)
                    else:
                        self.wrappers.depth_value.append(float(x[0]))
                        del x[0]
                        del x[len(x) - 1]
                        self.wrappers.trace_time.append(x[len(x) - 1])
                        del x[len(x) - 1]
                        self.wrappers.column = len(x)
                    try:
                        i = 0
                        while i < len(x):
                            x[i] = float(x[i])
                            self.paint(x[i], i, row)
                            i += 1
                        row += 1
                        self.out.append(x)
                    except Exception:
                        if type(x[i]) == str:
                            print('label')
                            self.wrappers.label = x[i]
                        print(sys.exc_info())
            self.wrappers.row = row
            return self.out
        except IOError:
            print(sys.exc_info())  # file not found
        except TypeError:
            print(sys.exc_info())
        except Exception:
            print(sys.exc_info())  # critical

    def filtering(self, data):
        filters = Filter()
        points = filters.appFilter_01(data)
        self.set_final_param_point(points)
        img.create_limit(filters.limit_up, filters.limit_left, filters.limit_down, filters.limit_right)


    def print_wrapper(self):
        print(' %s + %s + %s + %s' % (
            self.wrappers.row, self.wrappers.column, self.wrappers.trace_time, self.wrappers.depth_value))

    def paint(self, value, x, y):
        # gp = img.get_new_gradient_invert(100, -500, 500, value)
        gp = img.get_new_gradient_invert(100, -12500, 4000, value)
        img.set_pix(x, y, (gp, gp, gp), 3)

    def set_final_param_point(self, points):
        for point in points:
            point.set_param_point(self.wrappers.depth_value[point.y], self.wrappers.trace_time[point.y])
            print(point.print_status())
            print('test')
