from model.Device import Device
from .ActivateLight import ActivateLight
from .Dimmer import Dimmer


class DimmableLight(Device):
    def __init__(self):
        super().__init__()
        super().addActivator(ActivateLight())
        super().addActivator(Dimmer())

    @property
    def name(self):
        return "DimmableLight"
    
    @property
    def pluginType(self):
        return "Light"

    @staticmethod
    def getDefaultRequiredInfo():
        return {"ip": "127.0.0.1", "port": "0"}

