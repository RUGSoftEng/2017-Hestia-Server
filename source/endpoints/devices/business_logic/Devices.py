class BusinessLogicDevices:
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
        self._plugin_manager.implement_plugin(organization
                                                       , plugin_name
                                                       , name
                                                       , json)



