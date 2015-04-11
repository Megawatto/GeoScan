# Main class test

import handler
import GUI
import sys


class Main:
    def starter(self, url):
        runner = handler.Runner()
        gui = GUI.GUI()
        runner.parse(url)
        runner.handler(runner.agr)
        gui.output()



try:
    print('start')
    m = Main()
    m.starter('3.csv')

except Exception:
    print(sys.exc_info())

##    a = sys.argv
##    print(a)
##    if (a is None):
##        print('manual')
##        m.start(input("set file URL = "))
##    else:
##        print('auto')
##        m.start(a[1])
##    print('end')