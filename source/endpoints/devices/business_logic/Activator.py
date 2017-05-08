class BusinessLogicActivator:
    def __init__(self, db):
        self._database = db

    def get_activator(self, device_id, activator_id):
        device = self._database.get_device(device_id)
        activator = device.get_activator(activator_id)
        return activator

    def change_activator_state(self, device_id, activator_id, state):
        device = self._database.get_device(device_id)
        options = device.options
        activator = device.get_activator(activator_id)
        activator.state = state
        activator.perform(options)
