from model.Device import Device
from .ActivateLight import ActivateLight
from .Dimmer import Dimmer


class DimmableLight(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLight())
        super().add_activator(Dimmer())

    @classmethod
    def _get_organization(cls):
        return "Hestia"

    @classmethod
    def _get_name(cls):
        return "DimmableLight"

    @classmethod
    def _get_plugin_type(cls):
        return "Light"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0"}

