import requests
from flask import json

from model.Activator import Activator
from model.Database import Database
from plugins.philipsHue.color.ColorLight import ColorLight
from plugins.philipsHue.white.DimmableLight import DimmableLight


class AddAllLights(Activator):
    def __init__(self):
        super().__init__()
        self._state = False
        self._database = Database()

    def set_state_with_string(self, value):
        self._state = (value == "True" or value == "true")

    @property
    def type(self):
        return "bool"

    def perform(self, devicerequired_info):
        if self._state:
            url = "http://" + devicerequired_info["ip"] + "/api/" + devicerequired_info["user"] + "/lights"
            response = json.loads(requests.get(url).content)
            device_id = devicerequired_info.pop("id", None)
            print(device_id)
            for key, value in response.items():
                if value["state"]["reachable"]:
                    device = None
                    if value["type"] in ["Extended color light", "Color light"]:
                        device = ColorLight()
                    elif value["type"] in ["Color temperature light", "Dimmable light"]:
                        device = DimmableLight()

                    device.name = value["name"]
                    _required_info = dict(devicerequired_info)
                    _required_info["lampId"] = int(key)
                    device.required_info = _required_info

                    self._database.add_device(device)
            self._database.delete_device(device_id)

    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return "Install all lights"