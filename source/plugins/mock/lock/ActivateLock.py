from model.Activator import Activator
from model.util.stringToBool import string_to_bool


class ActivateLock(Activator):
    """
    Activator for the mock lock plugin. Depicts how a lock could be
    closed or opened.
    """
    def __init__(self):
        super().__init__()
        self._state = True

    @property
    def name(self):
        return "lock/Unlock"

    @property
    def type(self):
        return "bool"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = string_to_bool(value)

    def perform(self, devicerequired_info):
        if self.state:
            print("Open lock")
        else:
            print("Close lock")
