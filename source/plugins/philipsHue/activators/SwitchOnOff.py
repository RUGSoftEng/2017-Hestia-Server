import requests
from model.Activator import Activator


class SwitchOnOff(Activator):
    """
    Activator that can be used with the philips hue lighting devices.
    Turns the lamp on or off.
    """
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

    def perform(self, device_required_info):
        """
        Sends an HTTP PUT request to turn a light on or off.
        device_required_info: should at least contain a "user","lampID"
                              and "ip" field
        """
        if self._state:
            data = '{"on":true}'
        else:
            data = '{"on":false}'

        url = ("http://" + device_required_info["ip"]
               + "/api/" + device_required_info["user"]
               + "/lights/" + str(device_required_info["lampId"])
               + "/state" )
        response = requests.put(url, data)