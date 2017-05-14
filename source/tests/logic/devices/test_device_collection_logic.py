import unittest

from bson import ObjectId
from pymongo import MongoClient

from logic import DeviceCollectionLogic
from tests import test_util


class TestDeviceCollectionLogic(unittest.TestCase):
    def setUp(self):
        self._direct_database = MongoClient()["Hestia"]["testing"]
        self._database = test_util.get_dabase()
        self._plugin_manager = test_util.get_plugin_manager(self._database)

        self._logic = DeviceCollectionLogic(self._database, self._plugin_manager)

    def tearDown(self):
        self._direct_database.delete_many({})

    def test_get_all_devices(self):
        flag_device_one_found = False
        flag_device_two_found = False

        id_device_one = str(ObjectId())
        name_device_one = "device_one"
        self._add_device(id_device_one, name_device_one)

        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(1, len(retrieved_devices))

        id_device_two = str(ObjectId())
        name_device_two = "device_two"
        self._add_device(id_device_two, name_device_two)

        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(2, len(retrieved_devices))

        for device in retrieved_devices:
            if device.name == name_device_one:
                flag_device_one_found = True
            if device.name == name_device_two:
                flag_device_two_found = True

        self.assertTrue(flag_device_one_found)
        self.assertTrue(flag_device_two_found)

    def test_create_new_device(self):
        organization = "mock"
        plugin_name = "Lock"
        device_name = "TestDevice"

        req = self._plugin_manager.get_required_info_of(organization, plugin_name)
        req["organization"] = organization
        req["plugin_name"] = plugin_name
        req["name"] = device_name

        self._logic.create_new_device(req)

        device = self._direct_database.find_one({"name" : device_name})

        self.assertEqual(device_name, device["name"])

    def test_get_device(self):
        id_device_one = str(ObjectId())
        name_device_one = "device_one"
        self._add_device(id_device_one, name_device_one)

        retrieved_device = self._logic.get_device(str(id_device_one))

        self.assertEqual(name_device_one, retrieved_device.name)

    def test_remove_device(self):
        id_device_one = str(ObjectId())
        name_device_one = "device_one"
        self._add_device(id_device_one, name_device_one)

        count_before_delete = self._direct_database.count()

        self._logic.remove_device(id_device_one)

        self.assertEqual(count_before_delete - 1, self._direct_database.count())

    def _add_device(self, _id, name):
        data = {
            "module": "plugins.mock.Lock",
            "class": "Lock",
            "type": "Lock",
            "name": name,
            "options": {
                "bridge_ip": "127.0.2.1",
                "bridge_port": 90
            },
            "activators": [
                {
                    "module": "plugins.mock.ActivateLock",
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
