from model.Device import Device
from .ActivateLight import ActivateLight
from .Dimmer import Dimmer


class DimmableLight(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLight())
        super().add_activator(Dimmer())

    @classmethod
    def organization(self):
        return "Hestia"

    @property
    def name(self):
        return "DimmableLight"
    
    @property
    def plugin_type(self):
        return "Light"

    @classmethod
    def get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0"}

