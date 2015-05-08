__author__ = 'Valera'

from  server_build import s_main



def start_filter(data, limit, wrapper):
    global m
    m = s_main.Mains()
    return m.start_filter(data, limit, wrapper), m.handlers.cluster_zona