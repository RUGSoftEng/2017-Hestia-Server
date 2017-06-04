from zeroconf import *
import socket


class MyListener(object):
    def __init__(self):
        self.r = Zeroconf()

    def remove_service(self, zeroconf, type, name):
        print("Service", name, "removed")

    def add_service(self, zeroconf, type, name):
        print("Service", name, "added")
        print("Type is", type)
        info = self.r.get_service_info(type, name)
