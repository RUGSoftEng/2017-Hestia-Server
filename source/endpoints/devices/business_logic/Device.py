class BusinessLogicDevice:
    def __init__(self, db):
        self._database = db

    def get_device(self, device_id):
        return self._database.get_device(device_id)

    def remove_device(self, device_id):
        self._database.delete_device(device_id)