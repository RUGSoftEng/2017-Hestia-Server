from model.Device import Device
from plugins.hestia.simpleLock.ActivateLock import ActivateLock


class SimpleLock(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLock())

    def setup(self):
        print("setup lock")

    @classmethod
    def _get_organization(cls):
        return "Hestia"

    @classmethod
    def _get_name(cls):
        return "HestiaMotor"

    @classmethod
    def _get_plugin_type(cls):
        return "Motor"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0"}