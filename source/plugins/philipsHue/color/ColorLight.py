import json

from model.Device import Device
from plugins.philipsHue.activators.SliderBrightness import SliderBrightness
from plugins.philipsHue.activators.SliderColor import SliderColor
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff
import requests


class ColorLight(Device):
    def __init__(self):
        super().__init__()
        super().add_activator(SwitchOnOff())
        super().add_activator(SliderBrightness())
        super().add_activator(SliderColor())

    def setup(self):
        self._baseUrl = "http://" + self.required_info["ip"] + "/api"
        self.getUser()
        self.getLampId()

    def getUser(self):
        if self.required_info["user"] == "unknown" :
            data = '{"devicetype":"hue#whiteLight"}'
            response = requests.post(self._baseUrl, data)
            message = json.loads(response.content)[0]
            succes = message['success']
            self.required_info["user"] = succes['username']

    def getLampId(self):
        url = self._baseUrl + self.required_info["user"] + "/lights"
        response = json.loads(requests.get(url).content)
        found = False
        lamp_id = 0
        if self.required_info["seach_method"] == "reachable":
            for key, value in response.items():
                if value['state']['reachable'] and (value['type'] == 'Color light' or value['type'] == 'Extended color light'):
                    if found:
                        raise Exception("Multiple lights were found")
                    else :
                        found = True
                        lamp_id = int(key)

        elif self.required_info["search_method"] == "last":
            for key, value in response.items():
                if value['state'] and (value['type'] == 'Color light' or value['type'] == 'Extended color light'):
                    found = True
                    lamp_id = int(key)

        if not found:
            raise Exception("No lights were found")

        self.required_info["lampId"] = lamp_id

    @classmethod
    def _get_organization(cls):
        return 'Philips'

    @classmethod
    def _get_plugin_name(cls):
        return "ColorLight"

    @classmethod
    def _get_plugin_type(cls):
        return "Light"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "user": "unknown", "search_methode" : "last/reachable"} #search method can also be "reachable"