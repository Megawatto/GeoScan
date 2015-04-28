
import handler
import sys
import img


class Mains:
    data = []
    def starter(self, url):
        handlers = handler.Handler()
        self.data = handlers.parse(url)
        handlers.filtering(handlers.out)
        handlers.print_wrapper()
        img.show()
        # gui.output()
try:
    print('start')
    m = Mains()
    m.starter('test.csv')

except Exception:
    print(sys.exc_info())