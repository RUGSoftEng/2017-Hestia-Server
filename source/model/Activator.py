from abc import ABC, abstractmethod


class Activator(ABC):

    def __init__(self, id):
        self.activatorId = id

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stateType(self):
        pass

    @property
    @abstractmethod
    def requiredInfo(self):
        pass

    @requiredInfo.setter
    @abstractmethod
    def requiredInfo(self, value):
        pass

    @property
    @abstractmethod
    def state(self):
        pass

    @abstractmethod
    def setStateWithString(self, value):
        pass

    @property
    def stateString(self, value):
        str(self.state)

    @abstractmethod
    def perform(self):
        pass
