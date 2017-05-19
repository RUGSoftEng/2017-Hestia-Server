from database.DeviceDatabase import DeviceDatabase
from logic.devices.ActivatorLogic import ActivatorLogic
from logic.devices.DeviceCollectionLogic import DeviceCollectionLogic
from logic.plugins.PluginLogic import PluginLogic

_device_database = DeviceDatabase("devices")

device_logic = DeviceCollectionLogic(_device_database)
activator_logic = ActivatorLogic(_device_database)
plugin_logic = PluginLogic()