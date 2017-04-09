from plugins.mock.light.Light import Light
from plugins.mock.lock.Lock import Lock
from plugins.philipsHue.white.DimmableLight import DimmableLight
from plugins.philipsHue.color.ColorLight import ColorLight


class PluginManager:
    """
    A hard coded plugin manager.

    this is a hard coded plugin manager that implements all the functions we expect from the plugin manager.
    it is build so that later it can used as a adaptor around the real implementation of the plugin manager.
    """
    def __init__(self):
        self.plugins = {
                "Philips": {"DimmableLight": DimmableLight, "ColorLight": ColorLight , "ExtendedColorLight": ColorLight, "ColorTemperatureLight": DimmableLight},
                "Mock": {"Lock": Lock, "Light": Light}
               }

    def get_organizations(self):
        """ Get a list of organizations """
        organizations = list(self.plugins.keys())
        return organizations

    def get_plugins_of(self, organization):
        """ Get all the plugins of an organization """
        organization_plugins = self.plugins.get(organization)
        plugin_names = list(organization_plugins.keys())
        return plugin_names

    def get_required_info_of(self, organization, plugin_name):
        """ Get the required information of a specific """
        plugin = self.__get_class_of(organization, plugin_name)
        return plugin._get_default_required_info()

    def get_implementation_of(self, info):
        """ Get a concrete implementation of a plugin """
        organization = info['organization']
        plugin_name = info['plugin']
        plugin = self.__get_class_of(organization, plugin_name)
        plugin_impl = plugin()
        plugin_impl.required_info = info
        return plugin_impl

    def __get_class_of(self, organization, plugin_name):
        """ Get the class of an plugin """
        organization_plugins = self.plugins.get(organization)
        plugin = organization_plugins.get(plugin_name)
        return plugin
