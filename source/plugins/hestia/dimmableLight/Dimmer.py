from model.Activator import Activator


class Dimmer(Activator):
    def __init__(self):
        super().__init__()
        self._requiredInfo = {"IpAddress": "0.0.0.0", "Port": 0}
        self._state = 5

    @property
    def name(self):
        return "Intensity"

    @property
    def state_type(self):
        return int

    @property
    def required_info(self):
        return self._requiredInfo

    @required_info.setter
    def required_info(self, value):
        self._requiredInfo = value

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = bool(value)

    def perform(self):
        print("Set intensity to: " + str(self.state))
