import unittest

from bson import ObjectId
from pymongo import MongoClient

from database.DeviceDatabase import DeviceDatabase
from logic import DeviceCollectionLogic
from pluginmanager.PluginManager import PluginManager


class TestDeviceCollectionLogic(unittest.TestCase):
    def setUp(self):
        self._direct_database = MongoClient()["Hestia"]["testing"]
        self._database = DeviceDatabase("testing")
        self._plugin_manager = PluginManager()

        self._logic = DeviceCollectionLogic(self._database, self._plugin_manager)

    def tearDown(self):
        self._direct_database.delete_many({})

    def test_get_all_devices(self):
        flag_device_one_found = False
        flag_device_two_found = False

        self.__create_database_with_one_device()

        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(1, len(retrieved_devices))

        id_device_two = str(ObjectId())
        name_device_two = "device_two"
        self._add_device(id_device_two, name_device_two)

        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(2, len(retrieved_devices))

        for device in retrieved_devices:
            if device.name == self.name_device_one:
                flag_device_one_found = True
            if device.name == name_device_two:
                flag_device_two_found = True

        self.assertTrue(flag_device_one_found)
        self.assertTrue(flag_device_two_found)

    def test_create_new_device(self):
        device_name = "TestDevice"
        required_info = self.__get_plugin_information(device_name)
        self._logic.create_new_device(required_info)

        device = self._direct_database.find_one({"name": device_name})
        self.assertEqual(device_name, device["name"])

    def test_get_device(self):
        self.__create_database_with_one_device()

        retrieved_device = self._logic.get_device(str(self.id_device_one))

        self.assertEqual(self.name_device_one, retrieved_device.name)

    def test_remove_device(self):
        self.__create_database_with_one_device()

        count_before_delete = self._direct_database.count()

        self._logic.remove_device(self.id_device_one)

        self.assertEqual(count_before_delete - 1, self._direct_database.count())

    def test_change_device_name(self):
        self.__create_database_with_one_device()
        new_name = "new_name"
        self._logic.change_device_name(self.id_device_one, new_name)
        device = self._logic.get_device(self.id_device_one)
        self.assertEqual(device.name, new_name)

    def __create_database_with_one_device(self):
        self.id_device_one = str(ObjectId())
        self.name_device_one = "device_one"
        self._add_device(self.id_device_one, self.name_device_one)

    def _add_device(self, _id, name):
        data = {
            "module": "plugins.mock.devices.lock.Lock",
            "class": "Lock",
            "type": "Lock",
            "name": name,
            "options": {
                "bridge_ip": "127.0.2.1",
                "bridge_port": 90
            },
            "activators": [
                {
                    "module": "plugins.mock.activators.ActivateLock",
                    "rank": 0,
                    "class": "ActivateLock",
                    "name": "Activate",
                    "type": "bool",
                    "state": True
                }
            ]
        }
        activators = data.pop("activators", None)
        data["activators"] = {}
        for activator in activators:
            act_id = str(ObjectId())
            data["activators"][act_id] = activator

        data["_id"] = _id
        self._direct_database.insert_one(data)

    def __get_plugin_information(self, name):
        return {'organization': "Mock"
                , 'plugin_name': "Lock"
                , 'required_info': {
                    'name': name
                    , 'bridge_ip': '127.0.0.1'
                    , 'bridge_port': '80'
                    }
                }
