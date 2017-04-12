import json

from model.Device import Device
import requests

from plugins.setup.philips.AddAllLights import AddAllLights


class PhilipsHueSetup(Device):
    """
    Device that can be used to setup everything related to philips hue
    """
    def __init__(self):
        super().__init__()
        super().add_activator(AddAllLights())

    @classmethod
    def _get_organization(cls):
        return "Setup"

    def setup(self):
        if self.required_info["user"] in ["unknown", ""]:
            data = '{"devicetype":"hue#PhilipsSetup"}'
            response = requests.post("http://" + self.required_info["ip"] + "/api", data)
            message = json.loads(response.content)[0]
            succes = message['success']
            self.required_info["user"] = succes['username']
            print(self.id)
            self.required_info["id"] = self.id

    @classmethod
    def _get_plugin_type(cls):
        return "Setup"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "192.168.178.32", "user": "unknown"}

    @classmethod
    def _get_plugin_name(cls):
        return "PhilipsSetup"
