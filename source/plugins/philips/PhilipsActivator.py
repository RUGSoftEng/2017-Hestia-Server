from abc import abstractmethod

import requests

from models.Activator import Activator


class PhilipsActivator(Activator):
    def __init__(self, database, device_id, activator_id):
        super().__init__(database, device_id, activator_id)

    def state(self):
        state = self._retrieve_state_from_device()
        return state

    @abstractmethod
    def perform(self, options):
        pass

    def _send_data_to_bridge(self, data):
        options = self._database.get_field(self._device_id, "options")
        base_path = options["base_path"]
        url = base_path + "state"

        return requests.put(url, data)

    def _retrieve_state_from_device(self):
        options = self._database.get_field(self._device_id, "options")
        base_path = options["base_path"]
        url = base_path + "state"

        return requests.get(url)

    @abstractmethod
    def _translate_state(self, state):
        pass

