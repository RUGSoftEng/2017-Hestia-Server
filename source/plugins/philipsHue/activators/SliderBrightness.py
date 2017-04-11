import requests
from model.Activator import Activator


class SliderBrightness(Activator):
    def __init__(self):
        super().__init__()
        self._state = 0

    @property
    def name(self):
        return "Brightness"

    @property
    def type(self):
        return "unsigned_int8"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = float(value)

    def perform(self, devicerequired_info):
        int_state = int(self._state * 255)
        if int_state == 0:
            data = '{"on":false,"bri":0}'
        else :
            data = '{"on":true,"bri":' + str(int_state) + '}'

        url = "http://" + devicerequired_info["ip"] + "/api/" + devicerequired_info["user"] + "/lights/" + str(devicerequired_info["lampId"]) + "/state"
        response = requests.put(url, data)
        print(response.content)
