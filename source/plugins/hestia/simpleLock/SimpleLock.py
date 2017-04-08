from model.Device import Device
from plugins.hestia.simpleLock.ActivateLock import ActivateLock


class SimpleLock(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLock())

    def setup(self):
        print("setup lock")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @classmethod
    def _get_organization(cls):
        return "hestia"

    @classmethod
    def _get_plugin_name(cls):
        return "SimpleLock"

    @classmethod
    def _get_plugin_type(cls):
        return "Motor"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0"}