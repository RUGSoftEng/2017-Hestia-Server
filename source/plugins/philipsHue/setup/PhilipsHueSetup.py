import json

import requests

from model.Device import Device
from plugins.philipsHue.activators.AddAllLights import AddAllLights
from plugins.philipsHue.utils import get_new_user_if_needed


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
        self.required_info["id"] = self.id
        get_new_user_if_needed(self.required_info)

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
