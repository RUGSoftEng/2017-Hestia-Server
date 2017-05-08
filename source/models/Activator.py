from abc import ABC, abstractmethod


class Activator(ABC):
    def __init__(self, database, device_id, activator_id):
        self._database = database
        self._device_id = device_id
        self._activator_id = activator_id

    @property
    def identifier(self):
        return self._activator_id

    @property
    def name(self):
        return self._database.get_activator_field(self._device_id, self._activator_id, "name")

    @property
    def type(self):
        return self._database.get_activator_field(self._device_id, self._activator_id, "type")

    @property
    def state(self):
        return self._database.get_activator_field(self._device_id, self._activator_id, "state")

    @state.setter
    def state(self, value):
        self._database.update_activator_field(self._device_id, self._activator_id, "state", value)

    @abstractmethod
    def perform(self, options):
        """ Update the real activator with the current state"""
        pass