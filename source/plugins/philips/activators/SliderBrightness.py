from plugins.philips.PhilipsActivator import PhilipsActivator


class SliderBrightness(PhilipsActivator):
    def __init__(self, database, device_id, activator_id):
        super().__init__(database, device_id, activator_id)

    def _translate_state(self, state):
        _state = state["bri"]
        return (float(_state)/255.0)

    def perform(self, options):
        data = {}
        _state = int(self._database.get_activator_field(self._device_id, self._activator_id, "state") * 255.0)
        if _state < 20:
            data["on"] = False
        else:
            data["on"] = True
        data["bri"] = _state
        response = self._send_data_to_bridge(data)

        print(response)
