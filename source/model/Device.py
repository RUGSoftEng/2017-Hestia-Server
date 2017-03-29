from abc import ABC, abstractmethod


class Device(ABC):
    """
    An abstract implementation of a device
    Concrete plugins should implement his device.
    """
    activator_counter = 0

    def __init__(self):
        self._activators = list()
        self._id = None

    @property
    def id(self):
        """ The current id of the device"""
        return self._id

    @property
    @abstractmethod
    def name(self):
        """ The name. So that we might identify different plugins by name """
        pass

    @property
    @abstractmethod
    def plugin_type(self):
        """ The type of a device for example: Lock, Light"""
        pass

    @property
    def activators(self):
        """ The activators of a device """
        return self._activators

    @staticmethod
    @abstractmethod
    def get_default_required_info():
        pass

    def add_activator(self, activator):
        """ Add an activator to a device """
        self.activator_counter += 1
        activator.activatorId = self.activator_counter
        self.activators.append(activator)

    def get_activator(self, activator_id):
        """ Get a specific activator of a device"""
        return next(activator for activator in self.activators if activator.activatorId == activator_id)
