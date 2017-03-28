from model.Device import Device
from .ActivateLock import ActivateLock


class SimpleLock(Device):

    def __init__(self):
        super().__init__()
        super().addActivator(ActivateLock())

    @property
    def name(self):
        return "SimpleLock"
    
    @property
    def pluginType(self):
        return "Lock"

    @staticmethod
    def getEmptyRequiredInfo():
        return {"ip": "127.0.0.1", "port": "0"}


