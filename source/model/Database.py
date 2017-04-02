class Database:
    """ A singleton that represents our database """
    devices = list()
    device_counter = 0

    def __init__(self):
        pass

    def get_devices(self):
        """ Get a devices from the Data Access Object """
        return Database.devices

    def get_device(self, device_id):
        """ Get a device with a specific id from the Data Access Object """
        return next(device for device in Database.devices if device.deviceId == device_id)

    def add_device(self, device):
        """ Add a device to the the Data Access Object """
        self.increment_counter()
        device.deviceId = self.device_counter
        Database.devices.append(device)

    def delete_device(self, device_id):
        """ Delete a device with a specif id from the Data Access Object """
        device = next(device for device in Database.devices if device.deviceId == device_id)
        Database.devices.remove(device)

    @classmethod
    def increment_counter(cls):
        cls.device_counter += 1