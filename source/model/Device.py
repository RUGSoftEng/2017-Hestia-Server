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

    @classmethod
    @abstractmethod
    def organization(self):
        """ Return the organization name to which this plugin belongs"""
        pass

    @classmethod
    @abstractmethod
    def name(self):
        """ The name. So that we might identify different plugins form the same organization """
        pass

    @classmethod
    @abstractmethod
    def plugin_type(self):
        """ The type of a device for example: Lock, Light"""
        pass

    @property
    def activators(self):
        """ The activators of a device """
        return self._activators

    @classmethod
    def get_default_required_info(cls):
        """ Get the default information of this device """
        default_info = cls.__get_standard_required_info()
        extra_info = cls.get_extra_required_info()
        total = default_info.copy()
        total.update(extra_info)
        return total

    @classmethod
    @abstractmethod
    def get_extra_required_info(cls) -> dict:
        """ Return that part of the required information that is specific to each device"""
        pass

    @classmethod
    def __get_standard_required_info(cls):
        """ Returns that required information that is needed for all devices"""
        return {"organization": cls.organization(), "plugin": cls.name()}

    def add_activator(self, activator):
        """ Add an activator to a device """
        self.activator_counter += 1
        activator.activatorId = self.activator_counter
        self.activators.append(activator)

    def get_activator(self, activator_id):
        """ Get a specific activator of a device"""
        return next(activator for activator in self.activators if activator.activatorId == activator_id)
