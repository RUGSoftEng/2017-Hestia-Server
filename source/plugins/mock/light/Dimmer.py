from model.Activator import Activator


class Dimmer(Activator):
    """
    Activator for the mock light plugin. Depicts how a lights
    brightness could be changed.
    """
    def __init__(self):
        super().__init__()
        self._state = 0

    @property
    def name(self):
        return "Brightness"

    @property
    def type(self):
        return "unsigned_int8"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = float(value)

    def perform(self, devicerequired_info):
        print("Set intensity to: " + str(int(self.state * 255)))
