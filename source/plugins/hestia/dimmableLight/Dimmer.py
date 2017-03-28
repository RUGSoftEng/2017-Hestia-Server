from model.Activator import Activator


class Dimmer(Activator):
    def __init__(self):
        self._requiredInfo = {"IpAdress": "0.0.0.0", "Port": 0}
        self._state = 5

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return "Intensity"

    @property
    def stateType(self):
        return int

    @property
    def requiredInfo(self):
        return self._requiredInfo

    @requiredInfo.setter
    def requiredInfo(self, value):
        self._requiredInfo = value

    @property
    def state(self):
        return self._state


    def setStateWithString(self, value):
        self._state = bool(value)

    def perform(self):
        print("Set intesity to: " + str(self.state))