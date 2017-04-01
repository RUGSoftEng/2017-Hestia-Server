from abc import ABC, abstractmethod


class Device(ABC):
    """
    An abstract implementation of a device
    Concrete plugins should implement his device.

    ----------------------------------------------------------------------------
    A device consist of a set of properties and a set of _get_<property_name>
    functions.
    The properties are associated with concrete implementations of a device.
    While the _get_<property_name> functions are associated with the class /
    plugin implementation of a device. The _get_<property_name> functions should
    only be used when interacting with the class of a plugin not when
    interacting with a concrete device.

    As standard the __<function_name> functions are for internal use and should
    not be called from the outside.
    """
    activator_counter = 0

    def __init__(self):
        self._activators = list()
        self._required_info = self._get_default_required_info()
        self._id = None

    @property
    def id(self):
        """ The current id of the device. """
        return self._id

    @property
    def organization(self):
        """ The name of the organization to which this plugin belongs. """
        return self._get_organization()

    @property
    def name(self):
        """
        The name.
        So that we might identify different plugins form the same organization.
        """
        return self._get_name()

    @property
    def plugin_type(self):
        """ The type of a device for example: Lock, Light. """
        return self._get_plugin_type()

    @property
    def activators(self):
        """ The activators of a device """
        return self._activators

    def add_activator(self, activator):
        """ Add an activator to a device """
        self.activator_counter += 1
        activator.activatorId = self.activator_counter
        self.activators.append(activator)

    def get_activator(self, activator_id):
        """ Get a specific activator of a device"""
        return next(activator for activator in self.activators if activator.activatorId == activator_id)

    @property
    def required_info(self):
        """ The required info"""
        return self._required_info

    @classmethod
    def _get_default_required_info(cls):
        """ Get the default information of this device """
        default_info = cls.__get_standard_required_info()
        extra_info = cls._get_extra_required_info()
        total = default_info.copy()
        total.update(extra_info)
        return total

    @classmethod
    def __get_standard_required_info(cls):
        """ Returns that required information that is needed for all devices"""
        return {"organization": cls._get_organization()
                , "plugin": cls._get_name()}

    @classmethod
    @abstractmethod
    def _get_organization(cls):
        """
        The name of the organization to which this plugin belongs.
        This is the implementation at the plugin level.
        """
        pass

    @classmethod
    @abstractmethod
    def _get_name(cls):
        """
        The name.
        So that we might identify different plugins form the same organization.
        This is the implementation at the plugin level.
        """
        pass

    @classmethod
    @abstractmethod
    def _get_plugin_type(cls):
        """
        The type of a device for example: Lock, Light.
        This is the implementation at the plugin level.
        """
        pass

    @classmethod
    @abstractmethod
    def _get_extra_required_info(cls) -> dict:
        """ Return that part of the required information that is specific to each device"""
        pass

    @required_info.setter
    def required_info(self,info):
        self._required_info = info