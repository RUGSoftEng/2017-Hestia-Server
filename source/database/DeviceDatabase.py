import importlib

from bson.objectid import ObjectId
from pymongo import MongoClient

from util.NotFoundException import NotFoundException


class DeviceDatabase:
    """
    This class communicates with the MongoDB database. 
    It has several methods for this communication.
    """
    def __init__(self, collection):
        self._devices = MongoClient()["Hestia"][collection]

    def get_all_devices(self):
        """Instantiates all devices in database"""
        devices = []
        for data in self._devices.find():
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
        """Adds the given plugin info as a new device"""
        plugin["_id"] = str(ObjectId())
        self._devices.insert_one(plugin)

    def delete_device(self, device_id):
        self._devices.delete_one({"_id" : device_id})

    def update_field(self, device_id, field, new_value):
        self._devices.find_one_and_update({"_id" : device_id}, {"$set": {field: new_value}})

    def get_field(self, device_id, field):
        data = self.__get_device_data(device_id)
        return data[field]

    def get_activator_field(self, device_id, activator_id, field):
        data = self.__get_device_data(device_id)
        activator = self.__get_activator(data, activator_id)
        return activator[field]

    def update_activator_field(self, device_id, activator_id, field, new_value):
        self._devices.find_one_and_update({"_id": device_id}
                                          , {"$set": {"activators."
                                                      + activator_id
                                                      + "."
                                                      + field: new_value}})

    def __get_device_data(self, device_id):
        """Get data of device based on its id"""
        data = self._devices.find_one(device_id)
        if data is None:
            message = "No device with id [" + device_id + "] found."
            raise NotFoundException(message)
        else:
            return data

    @staticmethod
    def __get_activator(data, activator_id):
        try:
            return data["activators"][activator_id]
        except KeyError as exception:
            message = "No activator with id [" + activator_id + "] found."
            raise NotFoundException(message)

    @staticmethod
    def _get_class(module, class_name):
        module = importlib.import_module(module)
        return getattr(module, class_name)
