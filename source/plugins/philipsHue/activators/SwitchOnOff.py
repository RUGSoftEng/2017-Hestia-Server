import requests
from model.Activator import Activator

class SwitchOnOff(Activator):
    def __init__(self):
        super().__init__()
        self._state = True

    @property
    def name(self):
        return "On/Off"

    @property
    def type(self):
        return "bool"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = (value == "True" or value == "true")
        print(self.state)

    def perform(self, devicerequired_info):
        if self._state:
            url = "http://" + devicerequired_info["ip"] + "/api/" + devicerequired_info["user"] + "/lights/" \
                  + str(devicerequired_info["lampId"]) + "/state"
            data = '{"on":true}'
            response = requests.put(url, data)
            print(response.content)
        else:
            url = "http://" + devicerequired_info["ip"] + "/api/" + devicerequired_info["user"] + "/lights/" + str(
                devicerequired_info["lampId"]) + "/state"
            data = '{"on":false}'
            response = requests.put(url, data)
            print(response.content)