from abc import ABC, abstractmethod


class Activator(ABC):
    """
    An abstract implementation of a Activator.
    Concrete activators of a plugin should implement this class
    """

    def __init__(self):
        self._id = None

    @property
    def id(self):
        """ The current id of the activator"""
        return self._id

    @property
    @abstractmethod
    def name(self):
        """ The name of the activator which will be shown on the button"""
        pass

    @property
    @abstractmethod
    def state_type(self):
        """ The type a state has. For example int, bool"""
        pass

    @property
    @abstractmethod
    def required_info(self):
        """
        The information needed to operate the activator

        This should be a dict that with a key value pairs
        """
        pass

    @required_info.setter
    @abstractmethod
    def required_info(self, value):
        """ Set the required information """
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
    def perform(self):
        """ Update the real activator with the current state"""
        pass
