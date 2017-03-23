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
        """ The name. So that we might identify different type of devices """
        pass

    @property
    @abstractmethod
    def pluginType(self):
        """ The type of a device for example: Lock, Light"""
        pass

    @property
    def activators(self):
        """ The activators of a device """
        return self._activators

    def addActivator(self, activator):
        """ Add an activator to a device """
        self.activators.append(activator)

    def getActivator(self, activatorId):
        """ Get a specific activator of a device"""
        return next(activator for activator in self.activators if activator.activatorId == activatorId)
