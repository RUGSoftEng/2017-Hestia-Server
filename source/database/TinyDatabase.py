from bson import ObjectId
from tinydb import TinyDB, Query

from database.Database import Database
from exceptions.DatabaseException import DatabaseException
from exceptions.NotFoundException import NotFoundException
from models.User import User
from util.BasePath import get_base_path


class TinyDatabase(Database):

    def __init__(self, database_name):
        database_path = get_base_path() + "/database/tinydbData/"
        self._devices = TinyDB(database_path + database_name + '.json')

    def get_all_devices(self):
        """Instantiates all devices in database"""
        devices = []
        for data in self._devices.all():
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
        self._devices.insert(plugin)

    def delete_all_devices(self):
        self._devices.purge_tables()

    def delete_device(self, device_id):
        query = Query()
        self._devices.remove(query._id == device_id)

    def update_field(self, device_id, field, new_value):
        query = Query()
        self._devices.update({field: new_value}, query._id == device_id)

    def get_field(self, device_id, field):
        data = self.__get_device_data(device_id)
        return data[field]

    def get_activator_field(self, device_id, activator_id, field):
        data = self.__get_device_data(device_id)
        activator = self.__get_activator(data, activator_id)
        return activator[field]

    def update_activator_field(self, device_id, activator_id, field, new_value):
        query = Query()
        data = self.__get_device_data(device_id)
        activators = data["activators"]
        activator = activators[activator_id]
        activator[field] = new_value
        self._devices.update({"activators": activators}, query._id == device_id)

    def __get_device_data(self, device_id):
        query = Query()
        devices = self._devices.search(query._id == device_id)
        if len(devices) > 1:
            message = "Inconsistent database, more then one device with the same id"
            raise DatabaseException("tiny", message)
        elif len(devices) == 0:
            raise NotFoundException("device")
        else:
            return devices[0]

    def get_user(self, user_name):
        query = Query()
        users = self._devices.search(query._id == user_name)
        if len(users) > 1:
            message = "Inconsistent database, more then one device with the same id"
            raise DatabaseException("tiny", message)
        elif len(users) == 0:
            raise NotFoundException("device")
        else:
            return User(users[0]["username"],users[0]["password"], users[0]["rights"], users[0]["devices"])

    @staticmethod
    def __get_activator(data, activator_id):
        try:
            return data["activators"][activator_id]
        except KeyError:
            raise NotFoundException("activator")

