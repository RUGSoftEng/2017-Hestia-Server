from abc import abstractmethod
import requests
from flask import json

from models.Activator import Activator

class PhilipsActivator(Activator):
    def __init__(self, database, device_id, activator_id):
        super().__init__(database, device_id, activator_id)

    @abstractmethod
    def perform(self, options):
        pass

    @Activator.state.getter
    def state(self):
        json_state = self._retrieve_state_from_device()
        state = self._translate_state(json_state)
        self._database.update_activator_field(self._device_id, self._activator_id, "state", state)
        return state

    def _send_data_to_bridge(self, data):
        options = self._database.get_field(self._device_id, "options")
        base_path = options["base_path"]
        url = base_path + "state"

        return requests.put(url, json.dumps(data))

    def _retrieve_state_from_device(self):
        options = self._database.get_field(self._device_id, "options")
        base_path = options["base_path"]
        device = json.loads(requests.get(base_path).content)

        return device["state"]

    @abstractmethod
    def _translate_state(self, state):
        pass

