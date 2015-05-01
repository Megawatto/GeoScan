import traceback
import handler
import sys
import img


class Mains:
    data = []
    size = 0
    def starter(self, url):
        handlers = handler.Handler()
        print(str(id(handlers)))
        self.data = handlers.parse(url)
        handlers.filtering(handlers.out)
        handlers.print_wrapper()
        img.show()
        # gui.output()

    def parse(self, url):
        handlers = handler.Handler()
        print(str(id(handlers)))
        self.data = handlers.parse(url)
        self.size = handlers.get_wrappers()


# try:
#     print('start')
#     m = Mains()
#     m.starter('test.csv')
#     # m.starter('4.csv')
#     # m.starter('test.csv')
#
#
# except Exception:
#     print(traceback.print_exc())