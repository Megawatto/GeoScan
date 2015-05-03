import traceback
import handler
import sys
import img


class Mains:
    data = []
    size = 0
    scale = 0
    handlers = handler.Handler()

    def starter(self, url):
        handlers = handler.Handler()
        print(str(id(handlers)))
        self.data = handlers.parse(url)
        handlers.filtering(handlers.out)
        handlers.print_wrapper()
        img.show()
        # gui.output()

    def parse(self, url, scale):
        self.scale = scale
        handlers = handler.Handler()
        self.data = handlers.parse(url)
        self.size = handlers.get_wrappers()
        img.create_img(self.size[0], self.size[1], scale)
        img.draw_radarogramms(self.data, scale)
        self.handlers = handlers

    def start_filter(self):
        self.handlers.filtering(self.data)

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