# import csv
import filter


class Runner:
    akk = []
    out = []

    def parse(self, url):
        try:
            file = open(url, 'r')
            akk = ''
            for i in file:
                akk += file.readline()
                print(akk)
            akk = akk.replace('\n', ',')
            self.akk = akk.split(',')
            print(self.akk)
        except IOError:
            print(sys.exc_info())  # file not found
        except Exception:
            print(sys.exc_info())  # critical

    def handler(self, data):
        print('handler')
        filters = filter.Filter()  # not implement
        # filter.appFilter_01 # some work
        return None
