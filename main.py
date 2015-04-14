# Main class test

import handler
import sys
import wrapper
import img


class Main:
    def starter(self, url):
        wrapp = wrapper.Wrapper()
        handlers = handler.Handler()
        handlers.parse(url)
        handlers.filtering(handlers.out)
        handlers.print_wrapper()
        img.show()
        # gui.output()


try:
    print('start')
    m = Main()
    m.starter('4.csv')

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