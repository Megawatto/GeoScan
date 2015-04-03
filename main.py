#Main class test

import logic
import GUI
import sys

class Main:
    def start(self, url):
        runer = logic.Runer(),GUI.GUI()
        runer[0].parse(url)
        runer[0].handler(runer[0].akk)
        runer[1].output(runer[0].out)

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

