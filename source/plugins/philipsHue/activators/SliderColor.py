import requests
from model.Activator import Activator


class SliderColor(Activator):
    """
    Activator that can be used with the philips hue lighting devices that have the feature of changing color.
    This activator is responsible for changing the color of a light.
    """
    def __init__(self):
        super().__init__()
        self._state = 0

    @property
    def name(self):
        return "Color"

    @property
    def type(self):
        return "unsigned_int16"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = float(value)

    def perform(self, devicerequired_info):
        """
        Sends an HTTP PUT request to change the lamp's color.
        :param devicerequired_info: should atleast contain an "user","lampID" and "ip" field
        """
        data = '{"on":true,"hue":' + str(int(self._state * 65535)) + '}'
        url = "http://" + devicerequired_info["ip"] + "/api/" + devicerequired_info["user"] + "/lights/" + str(devicerequired_info["lampId"]) + "/state"
        response = requests.put(url, data)
        print(response.content)
