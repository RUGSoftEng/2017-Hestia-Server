from model.Device import Device
from .ActivateLock import ActivateLock


class simpleLock(Device):
    def __init__(self):
        super().__init__()
        super().addActivator(ActivateLock())

    @property
    def name(self):
        return "SimpleLock"
    
    @property
    def pluginType(self):
        return "Lock"

