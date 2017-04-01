from model.Activator import Activator
from model.util.stringToBool import string_to_bool


class ActivateLock(Activator):
    def __init__(self):
        super().__init__()
        self._state = True

    @property
    def name(self):
        return "Lock/Unlock"

    @property
    def state_type(self):
        return bool

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
