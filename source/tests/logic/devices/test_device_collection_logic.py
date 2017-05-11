import unittest

from bson import ObjectId
from pymongo import MongoClient

from PluginManager import PluginManager
from database.DeviceDatabase import DeviceDatabase
from logic import DeviceCollectionLogic


class TestEndpointActivator(unittest.TestCase):
    def setUp(self):
        self._direct_database = MongoClient()["Hestia"]["testing"]
        self._database = DeviceDatabase("testing")
        self._plugin_manager = PluginManager("deviceConfig")

        self._logic = DeviceCollectionLogic(self._database, self._plugin_manager)

    def tearDown(self):
        self._direct_database.delete_many({})

    def test_get_all_devices(self):
        self._id_device_one = ObjectId()
        self._name_device_one = "device_one"
        self._add_device(self._id_device_one, self._name_device_one)

        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(1, len(retrieved_devices))

        self._id_device_two = ObjectId()
        self._name_device_two = "device_two"
        self._add_device(self._id_device_two, self._name_device_two)
        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(2, len(retrieved_devices))

    def test_create_new_device(self):
        organization = "mock"
        plugin_name = "Lock"
        device_name = "TestDevice"

        req = self._plugin_manager.get_required_info_of(organization, plugin_name)
        req["organization"] = organization
        req["plugin_name"] = plugin_name
        req["name"] = device_name

        self._logic.create_new_device(req)

        devices = self._database.get_all_devices()
        device = devices[0]
        self.assertEqual(device_name, device.name)

    def test_get_device(self):
        req = self._plugin_manager.get_required_info_of("mock", "Lock")
        self._plugin_manager.implement_plugin("mock", "Lock", "test", req)
        device = self._database.get_all_devices()[0]

        retrieved_device = self._logic.get_device(device.identifier)

        self.assertEqual(device.name, retrieved_device.name)

    def test_remove_device(self):
        req = self._plugin_manager.get_required_info_of("mock", "Lock")
        self._plugin_manager.implement_plugin("mock", "Lock", "test", req)
        device = self._database.get_all_devices()[0]

        count_before_delete = len(self._database.get_all_devices())

        self._logic.remove_device(device.identifier)

        self.assertEqual(count_before_delete - 1, len(self._database.get_all_devices()))

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
            _id = str(id)
            data["activators"][_id] = activator

        data["_id"] = _id
        self._database.insert_one(data)
