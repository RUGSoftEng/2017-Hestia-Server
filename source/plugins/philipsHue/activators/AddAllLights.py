import requests
from flask import json

from model.Activator import Activator
from model.Database import Database
from plugins.philipsHue.color.ColorLight import ColorLight
from plugins.philipsHue.white.DimmableLight import DimmableLight


class AddAllLights(Activator):
    """
    Activator for the philips hue setup device. When a "true" state is performed
    all lights in the hue bridge are
    added.
    """
    color_types = ["Extended color light", "Color light"]
    basic_types = ["Color temperature light", "Dimmable light"]


    def __init__(self):
        super().__init__()
        self._state = False
        self._database = Database()

    def set_state_with_string(self, value):
        self._state = (value == "True" or value == "true")

    @property
    def type(self):
        return "bool"

    def perform(self, device_required_info):
        """
        Retrieves all lights from the hue bridge. Adds all reachable lights to
        the database using their corresponding device class. Duplicate lights
        aren't added. Removes the encapsulating device after all lights are
        added.
        device_required_info: requires a "user", "ip" and "id" field.
        """
        if self._state:
            url = ("http://" + device_required_info["ip"]
                   + "/api/" + device_required_info["user"]
                   + "/lights")
            response = json.loads(requests.get(url).content)
            device_id = device_required_info.pop("id", None)
            for key, value in response.items():
                lamp_id = int(key)
                if not self.is_already_installed(lamp_id):
                    device = self.get_device_instance(value["type"])
                    device.name = value["name"]
                    device.required_info = dict(device_required_info)
                    device_required_info[lamp_id] = lamp_id
                    self._database.add_device(device)

            self._database.delete_device(device_id)

    def is_already_installed(self, lamp_id):
        """
        Checks if there is already a philips hue light in the database that has
        the given lamp id.
        lamp_id: id to search for in the database.
        """
        devices = self._database.get_devices()
        for d in devices:
            if (("lampId" in d.required_info.keys())
                    and d.required_info["lampId"] == lamp_id):
                return True

        return False

    def get_device_instance(self, type):
        if type in self.color_types:
            device = ColorLight()
        elif type in self.basic_types:
            device = DimmableLight()

        return device

    @property
    def state(self):
        return self._state

    @property
    def name(self):
        return "Install all lights"
