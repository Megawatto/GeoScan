# import csv
import sys
import filter


class Runner:
    agr = []
    out = []

    def parse(self, url):
        try:
            pass
        except IOError:
            print(sys.exc_info())  # file not found
        except TypeError:
            print(sys.exc_info())
        except Exception:
            print(sys.exc_info())  # critical

    def filtering(self, data):
        pass
        return None
