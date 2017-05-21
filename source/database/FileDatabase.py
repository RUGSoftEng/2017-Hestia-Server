import importlib

from database.Database import Database
from util.NotFoundException import NotFoundException


class FileDatabase(Database):
    """
    This is an abstract class for communication with a database.
    It has several abstract methods for this communication.
    """

    def __init__(self, name):
        #create file on base path to save all devices
        self._file = name + ".txt"
        database = open(self._file,"w+")
        database.write('{"devices": []}')
        database.close()

    def get_all_devices(self):
        """Instantiates all devices in database"""
        database = open(self._file, "r")
        devices_database = eval(database.read())["devices"]
        devices = []
        for data in devices_database:
            _id = data["_id"]
            device = self._get_class(data["module"], data["class"])(self, _id)
            devices.append(device)
        return devices


    def get_device(self, device_id):
        """Instantiates the device with the given device_id"""
        data = self.__get_device_data(device_id)
        device = self._get_class(data["module"], data["class"])
        return device(self, device_id)


    def add_device(self, plugin):
        """Adds the given plugin info as a new device """
        print("to do")
        database = open(self._file, "r+")
        devices_database = eval(database.read())["devices"]
        devices_database.append(plugin)
        database.seek(12)
        devices = str(devices_database) + "}"
        database.write(devices)
        database.close()




    def delete_device(self, device_id):
        print("to do")


    def update_field(self, device_id, field, new_value):
        print("to do")

    def get_field(self, device_id, field):
        data = self.__get_device_data(device_id)
        return data[field]


    def get_activator_field(self, device_id, activator_id, field):
        data = self.__get_device_data(device_id)
        activator = self.__get_activator(data, activator_id)
        return activator[field]


    def update_activator_field(self, device_id, activator_id, field, new_value):
        print("to do")

    @staticmethod
    def _get_class(module, class_name):
        module = importlib.import_module(module)
        return getattr(module, class_name)

    def __get_device_data(self, device_id):
        """Get data of device based on its id"""
        database = open(self._file, "r")
        devices_database = eval(database.read())["devices"]
        for device in devices_database:
            if device["_id"] == device_id:
                return device

    @staticmethod
    def __get_activator(data, activator_id):
        try:
            return data["activators"][activator_id]
        except KeyError as exception:
            message = "No activator with id [" + activator_id + "] found."
            raise NotFoundException(message)
