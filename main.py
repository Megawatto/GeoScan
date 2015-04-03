# Main class test

import logic
import GUI
import sys


class Main:
    def start(self, url):
        runner = logic.Runner(), GUI.GUI()
        runner[0].parse(url)
        runner[0].handler(runner[0].akk)
        runner[1].output(runner[0].out)


try:
    print('start')
    m = Main()
    m.start('test.txt')
##    a = sys.argv
##    print(a)
##    if (a is None):
##        print('manual')
##        m.start(input("set file URL = "))
##    else:
##        print('auto')
##        m.start(a[1])
##    print('end')
except Exception:
    print(sys.exc_info())

