import copy
import importlib
import json
from os import listdir, path

from bson.objectid import ObjectId

from exceptions.NotFoundException import NotFoundException


class PluginManager:
    """
    This class is a link between the logic classes and plugins. 
    It is used to get information about plugins and instantiate plugins.
    """
    def __init__(self, path):
        self.plugin_path = path

    def get_plugin(self, collection, plugin_name, required_info):
        """create new plugin"""
        plugin = self.__get_plugin(collection, plugin_name)
        data = copy.deepcopy(plugin)

        device_id = str(ObjectId())
        data["_id"] = device_id

        #Remove unneeded plugin info
        activators = data.pop('activators', None)
        data.pop("required_info", None)

        #Create class and setup
        device_class = self._get_class(data["module"], data["class"])
        data["options"] = device_class.setup(required_info)

        #Rewrite to dict format
        data["activators"] = {}
        for activator in activators:
            _id = str(ObjectId())
            data["activators"][_id] = activator

        return data

    def get_collections(self):
        """ Get a list of collections """
        collections = list()
        for directory in listdir(self.plugin_path):
            if (path.isdir(path.join(self.plugin_path, directory)) and directory != "__pycache__"):
                collections.append(directory)
        return collections

    def get_required_info_of(self, collection, plugin_name):
        """ Get the required information of a specific plugin """
        plugin = self.__get_plugin(collection, plugin_name)
        required_info = plugin["required_info"]
        return required_info

    def _get_class(self, mod, class_name):
        mod = importlib.import_module(mod)
        return getattr(mod, class_name)

    def get_plugins_of(self, collection):
        """ Get all plugin names within an collection"""
        collections = self.get_collections()
        if collection in collections:
            devices_path = self.plugin_path + collection + "/devices/"
            plugins = list()
            for directory in listdir(devices_path):
                if path.isdir(path.join(devices_path, directory)) and directory != "__pycache__":
                    plugins.append(directory)
            return plugins
        else:
            message = "Collection [" + collection + "] not found."
            raise NotFoundException(message)

    def __get_plugin(self, collection, plugin_name):
        """ Get plugin based on collection and plugin name"""
        collection_plugins = self.get_plugins_of(collection)
        if plugin_name in collection_plugins:
            config_path = self.plugin_path + collection + "/devices/" + plugin_name + "/Configuration"
            plugin = json.load(open(config_path))
            return plugin
        else:
            message = "Plugin [" \
                      + plugin_name \
                      + "] of collection [" \
                      + collection \
                      + "] not found."
            raise NotFoundException(message)
