class DeviceDAO():

    def __init__(self):
        self.devices = list()

    def get(self):
        return self.devices

    def getDevice(self, deviceId):
        return next(device for device in self.devices if device.deviceId == deviceId)

    def addDevice(self, device):
        self.devices.append(device)
        return device

    def deleteDevice(self, deviceId):
        device = next(device for device in self.devices if device.deviceId == deviceId)
        self.devices.remove(device)

