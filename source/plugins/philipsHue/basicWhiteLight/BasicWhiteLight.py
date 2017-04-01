from model.Device import Device
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff


class BasicWhiteLight(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(SwitchOnOff())
        super().


    @classmethod
    def _get_organization(cls):
        return 'philipsHue'

    @classmethod
    def _get_name(cls):
        return "BasicWhiteLight"

    @classmethod
    def _get_plugin_type(cls):
        return "Light"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1"}