from model.Device import Device
from plugins.hestia.simpleLock.ActivateLock import ActivateLock


class SimpleLock(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLock())

    @classmethod
    def organization(cls):
        return "Hestia"

    @classmethod
    def name(cls):
        return "SimpleLock"
    
    @property
    def plugin_type(self):
        return "Lock"

    @classmethod
    def get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0"}