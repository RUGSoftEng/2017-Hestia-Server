import json

from model.Device import Device
from plugins.philipsHue.activators.SliderBrightness import SliderBrightness
from plugins.philipsHue.activators.SliderColor import SliderColor
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff
import requests

from plugins.setup.philips.AddAllLights import AddAllLights


class PhilipsHueSetup(Device):
    # This device has all activators neccessary to setup all light allready on a philips hue bridge
    def __init__(self):
        super().__init__()
        super().add_activator(AddAllLights())

    @classmethod
    def _get_organization(cls):
        return "Setup"

    def setup(self):
        if self.required_info["user"] == "unknown":
            #data = '{"devicetype":"hue#whiteLight"}'
            #response = requests.post(self._baseUrl, data)
            #message = json.loads(response.content)[0]
            #succes = message['success']
            self.required_info["user"] = 'CGxOchdTOaFQx-tUS8q0Orqfr4hYifYXQaRRJwR2'#succes['username']
            print(self.id)
            self.required_info["id"] = self.id

    @classmethod
    def _get_plugin_type(cls):
        return "Setup"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "192.168.2.19", "user": "unknown"}

    @classmethod
    def _get_plugin_name(cls):
        return "PhilipsSetup"
