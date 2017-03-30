from model.Activator import Activator
from model.util.stringToBool import string_to_bool


class ActivateLock(Activator):
    def __init__(self):
        super().__init__()
        self._requiredInfo = {"IpAddress": "0.0.0.0", "Port": 0}
        self._state = True

    @property
    def name(self):
        return "Lock/Unlock"

    @property
    def state_type(self):
        return bool

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
        self._state = string_to_bool(value)

    def perform(self):
        if self.state:
            print("Open lock")
        else:
            print("Close lock")
