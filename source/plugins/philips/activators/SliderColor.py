from plugins.philips.PhilipsActivator import PhilipsActivator


class SliderColor(PhilipsActivator):
    def perform(self, options):
        hue = int(self._database.get_activator_field(self._device_id, self._activator_id, "state") * 65535.0)
        data = {"hue":hue}
        response = self._send_data_to_bridge(data)
        print(response.content)

    def _translate_state(self, state):
        hue = state["hue"]
        return (float(hue) / 65535)
