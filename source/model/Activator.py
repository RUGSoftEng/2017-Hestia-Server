from abc import ABC, abstractmethod


class Activator(ABC):

    def __init__(self, id):
        self.activatorId = id

    @property
    @abstractmethod
    def name(self):
        """ The name of the activator which will be shown on the button"""
        pass

    @property
    @abstractmethod
    def stateType(self):
        """ The type a state has. For example int, bool"""
        pass

    @property
    @abstractmethod
    def requiredInfo(self):
        """
        The information needed to operate the activator

        This should be a dict that with a key value pairs
        """
        pass

    @requiredInfo.setter
    @abstractmethod
    def requiredInfo(self, value):
        """ Set the required information """
        pass

    @property
    @abstractmethod
    def state(self):
        """ The current state of the activator"""
        pass

    @abstractmethod
    def setStateWithString(self, value):
        """ Transform a string to a new state"""
        pass

    @property
    def stateString(self, value):
        """ Return the state as a string """
        return str(self.state)

    @abstractmethod
    def perform(self):
        """ Update the real activator with the current state"""
        pass
