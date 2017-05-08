import importlib

from bson import ObjectId
from pymongo import MongoClient


class DeviceDatabase:
    def __init__(self):
        self._devices = MongoClient()["Hestia"]["devices"]

    def get_all_devices(self):
        devices = []
        for data in self._devices.find():
            _id = str(data["_id"])
            device = self._get_class(data["module"], data["class"])(self, _id)
            devices.append(device)

        return devices

    def get_device(self, device_id):
        """Instantiates the device with the given device_id"""
        data = self._devices.find_one(ObjectId(device_id))
        device = self._get_class(data["module"], data["class"])
        return device(self, device_id)

    def add_device(self, plugin):
        """Adds the given plugin info as a new device"""
        data = plugin
        data["_id"] = ObjectId()
        self._devices.insert(data)

    def delete_device(self, device_id):
        self._devices.delete_one({"_id" : ObjectId(device_id)})

    def update_field(self, device_id, field, new_value):
        self._devices.find_one_and_update({"_id" : ObjectId(device_id)}, {"$set": {field: new_value}})

    def get_field(self, device_id, field):
        data = self._devices.find_one(ObjectId(device_id))
        return data[field]

    def get_activator_field(self, device_id, activator_id, field):
        data = self._devices.find_one(ObjectId(device_id))
        return data["activators"][activator_id][field]

    def update_activator_field(self, device_id, activator_id, field, new_value):
        self._devices.find_one_and_update({"_id": ObjectId(device_id)}
                                          , {"$set": {"activators."+activator_id+"."+field: new_value}})

    def _get_class(self, module, class_name):
        module = importlib.import_module(module)
        return getattr(module, class_name)


