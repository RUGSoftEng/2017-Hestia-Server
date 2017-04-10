import requests
from model.Activator import Activator


class SliderColor(Activator):
    def __init__(self):
        super().__init__()
        self._state = 0

    @property
    def name(self):
        return "Brightness"

    @property
    def type(self):
        return "unsigned_int16"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = int(float(value) * 65535)

    def perform(self, devicerequired_info):
        data = '{"on":true,"hue":' + str(self._state) + '}'
        url = "http://" + devicerequired_info["ip"] + "/api/" + devicerequired_info["user"] + "/lights/" + str(devicerequired_info["lampId"]) + "/state"
        response = requests.put(url, data)
        print(response.content)
