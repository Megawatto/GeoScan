import traceback

__author__ = 'Valera'
import csv
import sys
from wrapper import Wrapper


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
                else:
                    if len(x) == 1:
                        pass
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