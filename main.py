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

    #todo Времянка scale потом удалить из метода фильтра
    def start_filter(self, limit_box):
        find_point = self.handlers.filtering(self.data, limit_box, self.scale)
        img.draw_point(find_point, self.scale)
        print('create_filter')

    #todo Проработать динамичное изменение размера
    def repain(self, scale):
        img.create_img(self.size[0], self.size[1], scale)
        img.draw_radarogramms(self.data, scale)
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