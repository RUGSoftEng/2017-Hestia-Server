import json
import requests

from model.Device import Device
from plugins.philipsHue.activators.SliderBrightness import SliderBrightness
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff
from plugins.philipsHue.utils import get_new_user_if_needed, get_lamp_id_for_types


class DimmableLight(Device):
    """
    Device that can be used for the following philips hue types:
    - Dimmable light
    - Color temperature light
    """

    types = ["Color temperature light", "Dimmable light"]

    def __init__(self):
        super().__init__()
        super().add_activator(SwitchOnOff())
        super().add_activator(SliderBrightness())
        self._base_url = None

    def setup(self):
        """
        By calling this method the system connects with the philips hue bridge
        to get all the information necessary to control the light.
        """
        get_new_user_if_needed(self.required_info)
        get_lamp_id_for_types(self.required_info, self.types)


    @classmethod
    def _get_organization(cls):
        return 'Philips'

    @classmethod
    def _get_plugin_name(cls):
        return "DimmableLight"

    @classmethod
    def _get_plugin_type(cls):
        return "Light"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        """
        ip :            ip of philips hue bridge
        user :          string for identification
        search_method : method used to find the lamp ID
        """
        return {"ip": "127.0.0.1", "user": "unknown", "search_method": "last"}