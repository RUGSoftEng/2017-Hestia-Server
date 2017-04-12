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
        """
        Philips hue needs a string as identification for communication. When no
        string is given or it is said to be unknown this method retrieves a
        string that can be used as identification for all further communications
        . It also adds the id of this device to the required_info, using this
        the activator can remove the device when needed.
        """
        if self.required_info["user"] in ["unknown", ""]:
            data = '{"devicetype":"hue#PhilipsSetup"}'
            response = requests.post("http://" + self.required_info["ip"]
                                     + "/api", data)
            message = json.loads(response.content)[0]
            success = message["success"]
            self.required_info["user"] = success["username"]
            self.required_info["id"] = self.id

    @classmethod
    def _get_plugin_type(cls):
        return "Setup"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        """
        ip : ip of philips hue bridge
        user : string for identification
        """
        return {"ip": "127.0.0.1", "user": "unknown"}

    @classmethod
    def _get_plugin_name(cls):
        return "PhilipsHue"
