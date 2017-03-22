from abc import ABC, abstractmethod


class Device(ABC):
    cntr = 0

    def __init__(self):
        self.deviceId = self.__class__.newId()
        self._activators = list()

    @classmethod
    def newId(cls):
        cls.cntr += 1
        return cls.cntr

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def pluginType(self):
        pass

    @property
    def activators(self):
        return self._activators

    def addActivator(self, activator):
        self.activators.append(activator)

    def getActivator(self, activatorId):
        return next(activator for activator in self.activators if activator.activatorId == activatorId)
