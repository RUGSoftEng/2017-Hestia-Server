class DeviceDAO():
    devices = list()

    def __init__(self):
        pass

    def get(self):
        return DeviceDAO.devices

    def getDevice(self, deviceId):
        return next(device for device in DeviceDAO.devices if device.deviceId == deviceId)

    def addDevice(self, device):
        DeviceDAO.devices.append(device)
        return device

    def deleteDevice(self, deviceId):
        device = next(device for device in DeviceDAO.devices if device.deviceId == deviceId)
        DeviceDAO.devices.remove(device)

