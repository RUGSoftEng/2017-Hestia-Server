from model.Activator import Activator


class Dimmer(Activator):
    def __init__(self):
        super().__init__()
        self._state = 5

    @property
    def name(self):
        return "Intensity"

    @property
    def type(self):
        return int

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = bool(value)

    def perform(self):
        print("Set intensity to: " + str(self.state))
