import json

from model.Device import Device
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff
import requests


class BasicWhiteLight(Device):
    def __init__(self):
        super().__init__()
        super().add_activator(SwitchOnOff())

    def setup(self):
        self._baseUrl = url = "http://" + self.required_info["ip"] + "/api"
        self.getUser()
        self.getLampId()

    def getUser(self):
        #data = '{"devicetype":"hue#whiteLight"}'
        #response = requests.post(self._baseUrl, data)
        #message = json.loads(response.content)[0]
        #succes = message['success']
        self.required_info["user"] = 'ijShBPnAiPkGfR9re364j8klsOeqat-C3fIjJeKw'#succes['username']

    def getLampId(self):
        url = self._baseUrl + self.required_info["user"] + "/lights"
        response = json.loads(requests.get(url).content)
        found = False
        for key, value in response.items():
            if value['state']['reachable']:
                if found:
                    raise Exception("Multiple lights were found")
                else :
                    found = True
                    self._lampId = int(key)

        if not found:
            raise Exception("No lights were found")

        print(self._lampId)

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