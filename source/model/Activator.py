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

    @state.setter
    @abstractmethod
    def setstate(self, value):
        pass

    @abstractmethod
    def perform(self):
        pass
