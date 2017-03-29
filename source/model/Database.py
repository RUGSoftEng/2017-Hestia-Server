class Database():
    """ A singleton that represents our database """
    devices = list()
    cntrDevices = 0

    def __init__(self):
        pass

    def getDevices(self):
        """ Get a devices from the Data Access Object """
        return Database.devices

    def getDevice(self, deviceId):
        """ Get a device with a specific id from the Data Access Object """
        return next(device for device in Database.devices if device.deviceId == deviceId)

    def addDevice(self, device):
        """ Add a device to the the Data Access Object """
        self.cntrDevices += 1
        device.deviceId = self.cntrDevices
        Database.devices.append(device)
        return device

    def deleteDevice(self, deviceId):
        """ Delete a device with a specifc id from the Data Access Object """
        device = next(device for device in Database.devices if device.deviceId == deviceId)
        Database.devices.remove(device)

