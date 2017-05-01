class Database:
    """ This class represents our database """

    def __init__(self):
        self.devices = list()
        self._device_counter = len(self.devices)

    def get_devices(self):
        """ Get all devices from the Data Access Object """
        return self.devices

    def get_device(self, device_id):
        """ Get a device with a specific id from the Data Access Object """
        return next(device for device in self.devices if device.id == device_id)

    def add_device(self, device):
        """ Add a device to the the Data Access Object """
        device.id = self.get_new_counter()
        self.devices.append(device)

    def delete_device(self, device_id):
        """ Delete a device with a specific id from the Data Access Object """
        device = next(device for device in self.devices if device.id == device_id)
        self.devices.remove(device)

    def get_new_counter(self):
        """ Get a new counter for a device """
        new_counter = self._device_counter
        self._device_counter += 1
        return new_counter
