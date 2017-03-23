from model.Activator import Activator
from model.IpAddressAndPort import IpAddressAndPort

class ActivateLight(Activator):
    def __init__(self, id):
        super().__init__(id)

        self._requiredInfo = IpAddressAndPort
        self._state = True

    @property
    def name(self):
        return "On/Off"

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

    @state.setter
    def state(self, value):
        if not isinstance(value, self.stateType):
            raise Exception()

        self._state = value

    def perform(self):
        if self.state == True:
            print("Light goes on")
        else:
            print("Light goes offk")
