from model.Activator import Activator


class SwitchOnOff(Activator):
    def __init__(self):
        super().__init__()
        self._state = True

    @property
    def name(self):
        return "On/Off"

    @property
    def type(self):
        return bool

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = bool(value)

    def perform(self):
        if self.state:
            print("Switch light on")
        else:
            print("Switch loght off")