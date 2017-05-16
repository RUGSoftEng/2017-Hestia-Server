from pluginmanager.PluginManager import PluginManager
from database.DeviceDatabase import DeviceDatabase
from util.BasePath import get_base_path


def get_database():
    return DeviceDatabase("testing")


def get_plugin_manager(database):
    test_config = get_base_path() + "tests/testing_deviceConfig"
    return PluginManager(test_config, database)
