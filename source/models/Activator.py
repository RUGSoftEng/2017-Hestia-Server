from abc import ABC, abstractmethod

from exceptions.InvalidStateException import InvalidStateException


class Activator(ABC):
    """
    An abstract implementation of an activator.
    Concrete activators should only implement the abstract method perform.
    """

    def __init__(self, database, device_id, activator_id):
        self._database = database
        self._device_id = device_id
        self._activator_id = activator_id

    @property
    def identifier(self):
        return self._activator_id

    @property
    def rank(self):
        return self._database.get_activator_field(self._device_id, self._activator_id, "rank")

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
        if type(value) is eval(self.type):
            self._database.update_activator_field(self._device_id, self._activator_id, "state", value)
        else:
            raise InvalidStateException(value, eval(self.type))

    @abstractmethod
    def perform(self, options):
        """ Update the real activator with the current state"""
        pass
