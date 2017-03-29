from plugins.hestia.dimmableLight.DimmableLight import DimmableLight
from plugins.hestia.simpleLock.SimpleLock import SimpleLock


class PluginManager:
    """
    A hard coded plugin manager.

    this is a hard coded plugin manager that implements all the functions we expect from the plugin manager.
    it is build so that later it can used as a adaptor around the real implementation of the plugin manager.
    """
    def __init__(self):
        self.plugins = {
                "philipsHue": {},
                "hestia": {"SimpleLock": SimpleLock, "DimmablLight": DimmableLight}
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
        return plugin.getDefaultRequiredInfo()

    def get_implementation_of(self, organization, plugin_name, required_info):
        """ Get a concrete implementation of a plugin """
        # TODO implement this function
        raise NotImplemented()
        plugin = self.__get_class_of(organization, plugin_name)
        return plugin(required_info)

    def __get_class_of(self, organization, plugin_name):
        """ Get the class of an plugin """
        organization_plugins = self.plugins.get(organization)
        plugin = organization_plugins.get(plugin_name)
        return plugin
