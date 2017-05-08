from flask_restplus import abort

from model.util.NotFoundException import NotFoundException


class BusinessLogicRequiredInfo:
    """
    This class holds the logic behind the methods in RequiredInfo
    """

    def __init__(self,plugin_manager):
        self._plugin_manager = plugin_manager

    def get_organizations(self):
        return self._plugin_manager.get_organizations()

    def get_plugins_by_organization(self, organization):
        try:
            plugins = self._plugin_manager.get_plugins_of(organization)
            return plugins
        except NotFoundException as exception:
            self.__show_error(exception)

    def get_required_info(self, organization, plugin_name):
        try:
            required_info = self._plugin_manager.get_required_info_of(organization, plugin_name)
            required_info["name"] = "default"
            return required_info
        except NotFoundException as exception:
            self.__show_error(exception)

    @staticmethod
    def __show_error(exception):
        message = str(exception)
        abort(404, "", error=message)


