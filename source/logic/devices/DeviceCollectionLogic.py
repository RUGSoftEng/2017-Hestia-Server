from exceptions.NotFoundException import NotFoundException
from logic.util import abort_with_error


class DeviceCollectionLogic:
    """
    This class contains methods to interact with the collection of device, this
    includes methods to add devices to this collection.
    """
    def __init__(self, db, pm):
        self._database = db
        self._plugin_manager = pm

    def get_all_devices(self):
        devices = self._database.get_all_devices()
        return devices

    def create_new_device(self, json):
        collection = json.pop("collection")
        plugin_name = json.pop("plugin_name")
        required_info = json.pop('required_info')
        name = required_info.pop("name")
        plugin = self._plugin_manager.get_plugin(collection
                                        , plugin_name
                                        , required_info)
        plugin["name"] = name
        self._database.add_device(plugin)

    def get_device(self, device_id):
        return self._database.get_device(device_id)

    def remove_device(self, device_id):
        return self._database.delete_device(device_id)

    def change_device_name(self, device_id, new_name):
        device = self.get_device(device_id)
        device.name = new_name