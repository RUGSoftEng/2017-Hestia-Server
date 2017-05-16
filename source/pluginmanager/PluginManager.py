import importlib
import json

import copy
from bson.objectid import ObjectId

from util.NotFoundException import NotFoundException


class PluginManager:
    """
    This class is a link between the logic classes and plugins. 
    It is used to get information about plugins and instantiate plugins.
    """
    
    def __init__(self, device_config):
        self._plugins = json.load(open(device_config))

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
        organizations = list(self._plugins.keys())
        return organizations

    def get_plugins_of(self, organization):
        """ Get all the plugins of an organization """
        organization_plugins = self.__get_organization_plugins(organization)
        plugin_names = list(organization_plugins.keys())
        return plugin_names

    def get_required_info_of(self, organization, plugin_name):
        """ Get the required information of a specific """
        plugin = self.__get_plugin(organization, plugin_name)
        required_info = plugin["required_info"]
        required_info['name'] = 'default_name'
        return {'organization': organization
                , 'plugin_name': plugin_name
                , 'required_info': plugin["required_info"]
                }

    def _get_class(self, mod, class_name):
        mod = importlib.import_module(mod)
        return getattr(mod, class_name)

    def __get_organization_plugins(self, organization):
        """get all plugin names within an organization"""
        if organization in self._plugins:
            return self._plugins[organization]
        else:
            message = "Organization [" + organization + "] not found."
            raise NotFoundException(message)

    def __get_plugin(self, organization, plugin_name):
        """get required info of plugin based on organization and plugin name"""
        organization_plugins = self.__get_organization_plugins(organization)
        if plugin_name in organization_plugins:
            return organization_plugins[plugin_name]
        else:
            message = "Plugin [" \
                      + plugin_name \
                      + "] of organization [" \
                      + organization \
                      + "] not found."
            raise NotFoundException(message)
