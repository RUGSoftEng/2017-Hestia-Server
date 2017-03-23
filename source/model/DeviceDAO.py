class DeviceDAO():
    devices = list()

    def __init__(self):
        pass

    def get(self):
        """ Get a devices from the Data Access Object """
        return DeviceDAO.devices

    def getDevice(self, deviceId):
        """ Get a device with a specific id from the Data Access Object """
        return next(device for device in DeviceDAO.devices if device.deviceId == deviceId)

    def addDevice(self, device):
        """ Add a device to the the Data Access Object """
        DeviceDAO.devices.append(device)
        return device

    def deleteDevice(self, deviceId):
        """ Delete a device with a specifc id from the Data Access Object """
        device = next(device for device in DeviceDAO.devices if device.deviceId == deviceId)
        DeviceDAO.devices.remove(device)

