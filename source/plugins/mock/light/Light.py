from model.Device import Device
from .ActivateLight import ActivateLight
from .Dimmer import Dimmer


class Light(Device):
    """"
    Mock light device. 
    """
    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLight())
        super().add_activator(Dimmer())

    def setup(self):
        print("Mock light is being setup")

    @classmethod
    def _get_organization(cls):
        return "Mock"

    @classmethod
    def _get_plugin_name(cls):
        return "Light"

    @classmethod
    def _get_plugin_type(cls):
        return "Light"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0"}

