from exceptions.NotFoundException import NotFoundException
from logic.util import abort_with_error


class PluginLogic:
    """
    This class holds the logic to retrieve information regarding plugins.
    """

    def __init__(self, plugin_manager):
        self._plugin_manager = plugin_manager

    def get_collections(self):
        return self._plugin_manager.get_collections()

    def get_plugins(self, collection):
        return self._plugin_manager.get_plugins_of(collection)

    def get_required_info(self, collection, plugin_name):
        required_info = self._plugin_manager.get_required_info_of(
                collection, plugin_name)
        required_info['name'] = 'This name will be used to represent the device'
        return {"collection": collection
                , 'plugin_name': plugin_name
                , 'required_info': required_info
                }
