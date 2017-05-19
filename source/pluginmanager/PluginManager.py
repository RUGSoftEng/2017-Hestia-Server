import importlib

import copy
import json

from bson.objectid import ObjectId
from os import listdir

from util.ConfigPath import get_config_path

from util.NotFoundException import NotFoundException


class PluginManager:
    """
    This class is a link between the logic classes and plugins. 
    It is used to get information about plugins and instantiate plugins.
    """

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
        return listdir(get_config_path())

    def get_plugins_of(self, organization):
        """ Get all the plugins of an organization """
        organization_plugins = self.__get_organization_plugins(organization)
        #plugin_names = list(organization_plugins.keys())
        return organization_plugins

    def get_required_info_of(self, organization, plugin_name):
        """ Get the required information of a specific plugin """
        plugin = self.__get_plugin(organization, plugin_name)
        return plugin["required_info"]

    def _get_class(self, mod, class_name):
        mod = importlib.import_module(mod)
        return getattr(mod, class_name)

    def __get_organization_plugins(self, organization):
        """get all plugin names within an organization"""
        config_path = get_config_path()
        organizations = listdir(config_path)
        if organization in organizations:
            plugin_path = config_path + organization + "/"
            plugins = listdir(plugin_path)
            return plugins
        else:
            message = "Organization [" + organization + "] not found."
            raise NotFoundException(message)

    def __get_plugin(self, organization, plugin_name):
        """get plugin based on organization and plugin name"""
        organization_plugins = self.__get_organization_plugins(organization)
        if plugin_name in organization_plugins:
            config_path = get_config_path()
            plugin_path = config_path + organization + "/" + plugin_name
            plugin = json.load(open(plugin_path))
            return plugin[organization][plugin_name]
        else:
            message = "Plugin [" \
                      + plugin_name \
                      + "] of organization [" \
                      + organization \
                      + "] not found."
            raise NotFoundException(message)
