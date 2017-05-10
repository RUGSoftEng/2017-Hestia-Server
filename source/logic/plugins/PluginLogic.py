class PluginLogic:
    """
    This class holds the logic to retrieve information regarding plugins.
    """

    def __init__(self, plugin_manager):
        self._plugin_manager = plugin_manager

    def get_organizations(self):
        return self._plugin_manager.get_organizations()

    def get_plugins(self, organization):
        return self._plugin_manager.get_plugins_of(organization)

    def get_required_info(self, organization, plugin_name):
        required_info = self._plugin_manager.get_required_info_of(organization, plugin_name)
        required_info["organization"] = organization
        required_info["plugin_name"] = plugin_name
        required_info["name"] = "default"
        return required_info
