from plugins.philips.PhilipsActivator import PhilipsActivator


class SwitchOnOff(PhilipsActivator):
    def _translate_state(self, state):
        print("test")

    def perform(self, options):
        print("test")