from model.Device import Device
from .ActivateLock import ActivateLock


class SimpleLock(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLock())

    @property
    def name(self):
        return "SimpleLock"
    
    @property
    def plugin_type(self):
        return "Lock"

    @staticmethod
    def get_default_required_info():
        return {"ip": "127.0.0.1", "port": "0"}


