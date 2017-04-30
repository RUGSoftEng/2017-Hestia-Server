class BusinessLogicRequiredInfo:
    def __init__(self,plugin_manager):
        self._plugin_manager = plugin_manager

    def get_organizations_from_plugin_manager(self):
        return self.plugin_manager.get_organizations()

    def get_plugin_from_plugins_manager_by_organization(self,organization):
        return self.plugin_manager.get_plugins_of(organization)

    def get_required_info_from_plugin_manager_by_organization_and_plugin_name(self, organization, plugin_name):
        required_info = self.plugin_manager.get_required_info_of(organization, plugin_name)
        required_info["name"] = "default"
        return required_info
