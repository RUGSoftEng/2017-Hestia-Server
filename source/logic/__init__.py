from database.DeviceDatabase import DeviceDatabase
from logic.devices.ActivatorLogic import ActivatorLogic
from logic.devices.DeviceCollectionLogic import DeviceCollectionLogic
from logic.plugins.PluginLogic import PluginLogic
from pluginmanager.PluginManager import PluginManager
from util.BasePath import get_base_path

_device_database = DeviceDatabase("devices")

device_config = get_base_path() + "deviceConfig"
_plugin_manager = PluginManager()


device_logic = DeviceCollectionLogic(_device_database, _plugin_manager)
activator_logic = ActivatorLogic(_device_database)
plugin_logic = PluginLogic(_plugin_manager)