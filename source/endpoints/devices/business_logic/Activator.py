class BusinessLogicActivator:
    def __init__(self, db):
        self._database = db

    def get_activator_from_database_by_device_and_activator_id(self, device_id, activator_id):
        return self._get_activator(device_id, activator_id)

    def change_activator_state_with_string(self, device_id, activator_id, state):
        required_info = self._database.get_device(device_id).required_info
        activator = self._get_activator(device_id, activator_id)
        activator.set_state_with_string(state)
        activator.perform(required_info)

    def _get_activator(self, device_id, activator_id):
        device = self._database.get_device(device_id)
        activator = device.get_activator(activator_id)

        return activator