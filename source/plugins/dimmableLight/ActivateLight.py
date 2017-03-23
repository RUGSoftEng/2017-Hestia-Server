from model.Activator import Activator

class ActivateLight(Activator):
    def __init__(self, id):
        super().__init__(id)

        self._requiredInfo = {"IpAdress": "0.0.0.0", "Port": 0}
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

    def setStateWithString(self, value):
        self._state = bool(value)

    def perform(self):
        if self.state == True:
            print("Light goes on")
        else:
            print("Light goes offk")
