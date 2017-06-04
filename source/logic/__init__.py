from database.TinyDatabase import TinyDatabase
from database.users.MockUserDatabase import MockUserDatabase
from logic.devices.ActivatorLogic import ActivatorLogic
from logic.devices.DeviceCollectionLogic import DeviceCollectionLogic
from logic.plugins.PluginLogic import PluginLogic
from logic.users.Login import LoginLogic
from pluginmanager.PluginManager import PluginManager
from util.PluginPath import get_plugin_path

_device_database = TinyDatabase("hestia")
_user_database = MockUserDatabase()

_plugin_manager = PluginManager(get_plugin_path())

device_logic = DeviceCollectionLogic(_device_database, _plugin_manager)
activator_logic = ActivatorLogic(_device_database)
plugin_logic = PluginLogic(_plugin_manager)
login_logic = LoginLogic(_user_database)