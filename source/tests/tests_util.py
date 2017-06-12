from database.TinyDatabase import TinyDatabase
from pluginmanager.PluginManager import PluginManager
from database.MongoDatabase import MongoDatabase
from util.BasePath import get_base_path


def get_database():
    return get_tiny_database()


def get_tiny_database():
    return TinyDatabase("testing")


def get_mongo_database():
    return MongoDatabase("testing")


def get_plugin_manager():
    test_config = get_base_path() + "tests/test_plugin/"
    return PluginManager(test_config)
