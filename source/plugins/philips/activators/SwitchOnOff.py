from plugins.philips.PhilipsActivator import PhilipsActivator


class SwitchOnOff(PhilipsActivator):
    def __init__(self, database, device_id, activator_id):
        super().__init__(database, device_id, activator_id)

    def _translate_state(self, state):
        _state = state["on"]
        return _state

    def perform(self, options):
        data = {}
        if self._database.get_activator_field(self._device_id, self._activator_id, "state"):
            data["state"] = True
        else:
            data["state"] = False
        self._send_data_to_bridge(data)
