import traceback
import handler
import sys
import img


class Mains:
    data = []
    def starter(self, url):
        handlers = handler.Handler()
        print(str(id(handlers)))
        self.data = handlers.parse(url)
        handlers.filtering(handlers.out)
        handlers.print_wrapper()
        img.show()
        # gui.output()
try:
    print('start')
    m = Mains()
    m.starter('2.csv')
    # m.starter('4.csv')
    # m.starter('test.csv')


except Exception:
     print(traceback.print_exc())