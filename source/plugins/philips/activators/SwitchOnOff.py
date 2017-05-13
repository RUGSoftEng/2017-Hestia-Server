from plugins.philips.PhilipsActivator import PhilipsActivator


class SwitchOnOff(PhilipsActivator):
    def __init__(self, database, device_id, activator_id):
        super().__init__(database, device_id, activator_id)

    def perform(self, options):
        print("test")