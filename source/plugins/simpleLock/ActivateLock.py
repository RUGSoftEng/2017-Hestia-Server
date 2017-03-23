from model.Activator import Activator
from model.IpAddressAndPort import IpAddressAndPort


class ActivateLock(Activator):
    def __init__(self, id):
        super().__init__(id)

        self._requiredInfo = IpAddressAndPort
        self._state = True

    @property
    def name(self):
        return "Lock/Unlock"

    @property
    def stateType(self):
        return bool

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

    @property
    def stateString(self, value):
        return str(self._state)


    def perform(self):
        if self.state == True:
            print("Open lock")
        else:
            print("Close lock")
