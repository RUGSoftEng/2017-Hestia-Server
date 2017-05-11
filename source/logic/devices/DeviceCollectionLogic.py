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
        organization = json.pop("organization")
        plugin_name = json.pop("plugin_name")
        name = json.pop("name")
        plugin = self._plugin_manager.get_plugin(organization
                                        , plugin_name
                                        , json)
        plugin["name"] = name
        self._database.add_device(plugin)

    def get_device(self, device_id):
        return self._database.get_device(device_id)

    def remove_device(self, device_id):
        self._database.delete_device(device_id)
