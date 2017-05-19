from logic.util import abort_with_error
from util.NotFoundException import NotFoundException
from pluginmanager.PluginManager import PluginManager
from util.ConfigPath import get_info_plugin


class DeviceCollectionLogic:
    """
    This class contains methods to interact with the collection of device, this
    includes methods to add devices to this collection.
    """
    def __init__(self, db):
        self._database = db

    def get_all_devices(self):
        devices = self._database.get_all_devices()
        return devices

    def create_new_device(self, json):
        try:
            organization = json.pop("organization")
            plugin_name = json.pop("plugin_name")
            name = json.pop("name")

            plugin_manager = self.get_plugin_manager(organization, plugin_name)

            plugin = plugin_manager.get_plugin(organization
                                            , plugin_name
                                            , json)
            plugin["name"] = name
            self._database.add_device(plugin)
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def get_device(self, device_id):
        try:
            return self._database.get_device(device_id)
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def remove_device(self, device_id):
        try:
            return self._database.delete_device(device_id)
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def change_device_name(self, device_id, new_name):
        device = self.get_device(device_id)
        device.name = new_name

    def get_plugin_manager(self, organization, plugin_name):
        device_config = get_info_plugin(organization, plugin_name)
        return PluginManager(device_config)
