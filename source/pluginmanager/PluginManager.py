import importlib

import copy
import json

from bson.objectid import ObjectId
from os import listdir, path

from util.NotFoundException import NotFoundException


class PluginManager:
    """
    This class is a link between the logic classes and plugins. 
    It is used to get information about plugins and instantiate plugins.
    """
    def __init__(self, path):
        self.plugin_path = path

    def get_plugin(self, organization, plugin_name, required_info):
        """create new plugin"""
        plugin = self.__get_plugin(organization, plugin_name)
        data = copy.deepcopy(plugin)

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

    def get_organizations(self):
        """ Get a list of organizations """
        organizations = list()
        for directory in listdir(self.plugin_path):
            if (path.isdir(path.join(self.plugin_path, directory)) and directory != "__pycache__"):
                organizations.append(directory)
        return organizations

    def get_required_info_of(self, organization, plugin_name):
        """ Get the required information of a specific plugin """
        plugin = self.__get_plugin(organization, plugin_name)
        required_info = plugin["required_info"]
        return required_info

    def _get_class(self, mod, class_name):
        mod = importlib.import_module(mod)
        return getattr(mod, class_name)

    def get_plugins_of(self, organization):
        """get all plugin names within an organization"""
        organizations = self.get_organizations()
        if organization in organizations:
            devices_path = self.plugin_path + organization + "/devices/"
            plugins = list()
            for directory in listdir(devices_path):
                if path.isdir(path.join(devices_path, directory)) and directory != "__pycache__":
                    plugins.append(directory)
            return plugins
        else:
            message = "Organization [" + organization + "] not found."
            raise NotFoundException(message)

    def __get_plugin(self, organization, plugin_name):
        """get plugin based on organization and plugin name"""
        organization_plugins = self.get_plugins_of(organization)
        if plugin_name in organization_plugins:
            config_path = self.plugin_path + organization + "/devices/" + plugin_name + "/Configuration"
            plugin = json.load(open(config_path))
            return plugin
        else:
            message = "Plugin [" \
                      + plugin_name \
                      + "] of organization [" \
                      + organization \
                      + "] not found."
            raise NotFoundException(message)
