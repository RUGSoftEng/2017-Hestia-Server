from logic.util import abort_with_error
from util.NotFoundException import NotFoundException


class PluginLogic:
    """
    This class holds the logic to retrieve information regarding plugins.
    """

    def __init__(self, plugin_manager):
        self._plugin_manager = plugin_manager

    def get_collections(self):
        return self._plugin_manager.get_collections()

    def get_plugins(self, collection):
        try:
            return self._plugin_manager.get_plugins_of(collection)
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def get_required_info(self, collection, plugin_name):
        try:
            required_info = self._plugin_manager.get_required_info_of(
                collection, plugin_name)
            required_info['name'] = 'This name will be used to represent the device'
            return {"collection": collection
                , 'plugin_name': plugin_name
                , 'required_info': required_info
                    }
        except NotFoundException as exception:
            abort_with_error(str(exception))
