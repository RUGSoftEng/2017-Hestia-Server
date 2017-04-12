import json

from model.Device import Device
from plugins.philipsHue.activators.SliderBrightness import SliderBrightness
from plugins.philipsHue.activators.SliderColor import SliderColor
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff
import requests


class ColorLight(Device):
    """
    Device that can be used for the following philips hue types:
        - Color light
        - Extended color light
    """
    def __init__(self):
        super().__init__()
        super().add_activator(SwitchOnOff())
        super().add_activator(SliderBrightness())
        super().add_activator(SliderColor())

    """
    Setup connects with the philips hue bridge to get all the information neccessary
    to control the light.
    """
    def setup(self):
        self._baseUrl = "http://" + self.required_info["ip"] + "/api"
        self.getUser()
        self.getLampId()

    """
    Philips hue needs an string as identification for communication. When no string is given or it is said to be 
    unknown this method retrieves a string that can be used as identification for all further communications.
    """
    def getUser(self):
        if self.required_info["user"] in ["unknown", ""]:
            data = '{"devicetype":"hue#whiteLight"}'
            response = requests.post(self._baseUrl, data)
            message = json.loads(response.content)[0]
            succes = message['success']
            self.required_info["user"] = succes['username']

    """
    Gets the id of the new lamp. Can use two different methods.
    last : retrieves the id of the last lamp added to the philips hue bridge.
    reachable : retrieves the id of the only lamp that is currently reachable. This requires all other lights to not
    have power.
    """
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

    """
    ip : ip of philips hue bridge
    user : identification string for identification
    search_method : method used to find the lamp ID
    """
    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "user": "unknown", "search_methode" : "last/reachable"}