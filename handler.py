import math
import traceback

__author__ = 'Valera'
import csv
import sys
from filter import Filter
from wrapper import Wrapper
import img


class Handler:
    out = []
    wrappers = Wrapper()
    rows = 0
    column = 0

    def parse(self, url):
        print('parse')
        self.out = []
        try:
            row = 0
            file = open(url)
            reader = csv.reader(x.replace('\0', '').replace(' ', '') for x in file)
            for x in reader:
                if len(x) == 0:
                    pass
                    # print(x)
                else:
                    if len(x) == 1:
                        pass
                        # print(x)
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
                            # self.paint(x[i], i, row)
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
            print(traceback.print_exc())  # file not found
        except TypeError:
            print(traceback.print_exc())
        except Exception:
            print(traceback.print_exc())  # critical
    #todo Времянка scale
    def filtering(self, data, limit_box, scale):
        filters = Filter(self.wrappers.row, self.wrappers.column, scale)
        filters.set_limit(limit_box)
        # points = filters.app_filter_01(data)
        points = filters.app_filter_03(data)
        img.create_limit(filters.limit_up, filters.limit_left, filters.limit_down, filters.limit_right, scale)
        return self.set_final_param_point(points)

    def print_wrapper(self):
        print(' %s + %s + %s + %s' % (
            self.wrappers.row, self.wrappers.column, self.wrappers.trace_time, self.wrappers.depth_value))

    def set_final_param_point(self, points):
        for point in points:
            point.set_param_point(self.wrappers.depth_value[point.y], self.wrappers.trace_time[point.y])
            print(point.print_status())
        print(len(points))
        points = set(points)
        print(len(points))
        print('................FINISH.................')
        return points

    def get_wrappers(self):
        return self.wrappers.row, self.wrappers.column