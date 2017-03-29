from model.Device import Device
from plugins.dimmableLight.ActivateLight import ActivateLight
from plugins.dimmableLight.Dimmer import Dimmer


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

