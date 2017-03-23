from model.Device import Device
from plugins.dimmableLight.ActivateLight import ActivateLight
from plugins.dimmableLight.Dimmer import Dimmer


class DimmableLight(Device):
    def __init__(self):
        super().__init__()
        super().addActivator(ActivateLight(1))
        super().addActivator(Dimmer(2))

    @property
    def name(self):
        return "DimmableLight"
    
    @property
    def pluginType(self):
        return "Light"

