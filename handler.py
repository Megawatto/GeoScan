__author__ = 'Valera'
import csv
import sys
from filter import Filter
from wrapper import Wrapper


class Handler:
    out = []
    wrappers = Wrapper()

    def parse(self, url):
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
                        del x[len(x) - 1]
                        self.wrappers.trace_time.append(x[len(x) - 1])
                        del x[len(x) - 1]
                        self.wrappers.column = len(x)
                    try:
                        i = 0
                        while i < len(x):
                            x[i] = float(x[i])
                            i += 1
                        row += 1
                        self.out.append(x)
                    except Exception:
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
        filters.appFilter_01(data)
        return None

    def print_wrapper(self):
        print(' %s + %s + %s + %d' % (
            self.wrappers.row, self.wrappers.column, self.wrappers.trace_time, len(self.wrappers.trace_time)))
