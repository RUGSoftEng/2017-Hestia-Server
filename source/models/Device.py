import importlib
from abc import ABC, abstractmethod


class Device(ABC):
    """
    An abstract implementation of a device
    Concrete plugins should only implement the abstract method setup().
    A device has a list of activators to give all actions it can perform.
    """

    def __init__(self, database, device_id):
        self._database = database
        self._device_id = device_id

    @property
    def identifier(self):
        return self._device_id

    @property
    def name(self):
        return self._database.get_field(self._device_id, "name")

    @name.setter
    def name(self, new_name):
        self._database.update_field(self._device_id, "name", new_name)

    @property
    def type(self):
        return self._database.get_field(self._device_id, "type")

    @property
    def options(self):
        return self._database.get_field(self._device_id, "options")

    @property
    def activators(self):
        activators = list()
        data = self._database.get_field(self._device_id, "activators")
        for activator_id in data:
            activators.append(self.get_activator(activator_id))
        return activators

    def get_activator(self, activator_id):
        return self._create_activator(activator_id)

    @classmethod
    @abstractmethod
    def setup(cls, required_info):
        return required_info

    def _create_activator(self, activator_id):
        module_name = self._database.get_activator_field(self._device_id, activator_id, "module")
        class_name = self._database.get_activator_field(self._device_id, activator_id, "class")
        module_ = importlib.import_module(module_name)
        class_ = getattr(module_, class_name)
        act = class_(self._database, self._device_id, activator_id)
        return act
