class BusinessLogicDevices:
    def __init__(self, db, pm):
        self._database = db
        self._plugin_manager = pm

    def get_all_devices_from_database(self):
        return self._database.get_devices()

    def create_new_device_from_json_input(self, json):
        information = eval(json)
        name = information.pop("name", None)
        plugin = self._plugin_manager.get_implementation_of(information)
        plugin.name = name
        return plugin

    def install_new_device(self, device):
        self._database.add_device = device
        device.setup()


