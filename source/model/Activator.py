from abc import ABC, abstractmethod


class Activator(ABC):
    """
    An abstract implementation of a Activator.
    Concrete activators of a plugin should implement this class.
    """
    def __init__(self):
        self._id = None

    @property
    def id(self):
        """ The current id of the activator"""
        return self._id

    @id.setter
    def id(self, value):
        """ The current id of the activator"""
        self._id = value

    @property
    @abstractmethod
    def name(self):
        """ The name of the activator which will be shown on the button"""
        pass

    @property
    @abstractmethod
    def type(self):
        """ 
        The type a state has. For example int, bool. This type can be used by the clients to decide how the 
        activator should be represented
        """
        pass

    @property
    @abstractmethod
    def state(self):
        """ The current state of the activator"""
        pass

    @abstractmethod
    def set_state_with_string(self, value):
        """ Transform a string to a new state"""
        pass

    @property
    def state_string(self):
        """ Return the state as a string """
        return str(self.state)

    @abstractmethod
    def perform(self, devicerequired_info):
        """ 
        Calling this method should result in an action performed by the real life peripheral of which the device
        containing this activator is an abstraction.
        """
        pass
