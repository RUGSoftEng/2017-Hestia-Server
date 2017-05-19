from os.path import isfile, join

from logic.util import abort_with_error
from pluginmanager.PluginManager import PluginManager
from util.ConfigPath import get_info_plugin
from util.ConfigPath import get_config_path
from util.ConfigPath import get_plugins_path
from util.NotFoundException import NotFoundException
from os import listdir


class PluginLogic:
    """
    This class holds the logic to retrieve information regarding plugins.
    """

    def get_organizations(self):
        return listdir(get_config_path())


    def get_plugins(self, organization):
        try:
            plugins_path = get_plugins_path(organization)
            plugins = listdir(plugins_path)
            return plugins
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def get_required_info(self, organization, plugin_name):
        try:
            plugin_manager = self.get_plugin_manager(organization, plugin_name)
            required_info = plugin_manager.get_required_info_of(
                organization, plugin_name)
            required_info["organization"] = organization
            required_info["plugin_name"] = plugin_name
            required_info["name"] = "default"
            return required_info
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def get_plugin_manager(self, organization, plugin_name):
        device_config = get_info_plugin(organization, plugin_name)
        return PluginManager(device_config)
