from pluginmanager.PluginManager import PluginManager
from database.MongoDatabase import MongoDatabase
from util.BasePath import get_base_path


def get_database():
    return MongoDatabase("testing")


def get_plugin_manager():
    test_config = get_base_path() + "tests/testing_deviceConfig"
    return PluginManager(test_config)
