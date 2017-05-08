import importlib
import json
import uuid

from bson import ObjectId


class PluginManager:
    def __init__(self, device_config_location, database):
        self._plugins = json.load(open(device_config_location))
        self._database = database

    def implement_plugin(self, organization, plugin_name, name, required_info):
        data = self._plugins[organization][plugin_name]

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
        data["name"] = name
        self._database.add_device(data)

    def get_organizations(self):
        """ Get a list of organizations """
        organizations = list(self._plugins.keys())
        return organizations

    def get_plugins_of(self, organization):
        """ Get all the plugins of an organization """
        organization_plugins = self._plugins[organization]
        plugin_names = list(organization_plugins.keys())
        return plugin_names

    def get_required_info_of(self, organization, plugin_name):
        """ Get the required information of a specific """
        return self._plugins[organization][plugin_name]["required_info"]

    def _get_class(self, mod, class_name):
        mod = importlib.import_module(mod)
        return getattr(mod, class_name)