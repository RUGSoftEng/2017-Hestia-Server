import unittest

from bson import ObjectId
from pymongo import MongoClient

from database.DeviceDatabase import DeviceDatabase
from models.Device import Device
from tests import test_util


class TestDeviceDatabaseMongoDB(unittest.TestCase):
    def setUp(self):
        self._database = test_util.get_dabase()
        self._direct_database = MongoClient()["Hestia"]["testing"]

        self._device_data = {
                              "module": "plugins.mock.Lock",
                              "class": "Lock",
                              "type" : "Lock",
                              "name" : "TestDevice",
                              "options": {
                                "bridge_ip": "127.0.2.1",
                                "bridge_port": 90
                              },
                              "activators": [
                                {
                                  "module" : "plugins.mock.ActivateLock",
                                  "class": "ActivateLock",
                                  "name": "Activate",
                                  "type": "bool",
                                  "state" : True
                                }
                              ]
                            }
        activators = self._device_data.pop("activators", None)
        self._device_data["activators"] = {}
        for activator in activators:
            _id = str(ObjectId())
            self._device_data["activators"][_id] = activator

    def tearDown(self):
        self._device_data = {}
        self._direct_database.delete_many({})

    def test_get_all_devices(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)

        retrieved_devices = self._database.get_all_devices()

        self.assertEqual(1, len(retrieved_devices))

        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)

        retrieved_devices = self._database.get_all_devices()

        self.assertEqual(2, len(retrieved_devices))


    def test_get_device(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)

        device = self._database.get_device(_id)

        self.assertEqual(_id, device.identifier)
        self.assertIsInstance(device, Device)

    def test_add_device(self):
        initial_count = self._direct_database.count()

        self._database.add_device(self._device_data)

        self.assertEqual(initial_count+1, self._direct_database.count())

    def test_delete_device(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)
        initial_count = self._direct_database.count()

        self._database.delete_device(_id)

        self.assertEqual(initial_count - 1, self._direct_database.count())


    def test_update_field(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)
        new_name = "Hestia"

        self._database.update_field(_id, "name", new_name)

        device = self._direct_database.find_one({"_id": _id})
        self.assertEqual(device["name"], new_name)

    def test_get_field(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)

        name = self._database.get_field(_id, "name")

        self.assertEqual(self._device_data["name"], name)

    def test_get_activator_field(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)

        activators = self._direct_database.find_one({"_id": _id})["activators"]
        act_id = list(activators.keys())[0]

        activator_name = self._database.get_activator_field(_id, act_id, "name")

        real_name = self._device_data["activators"][act_id]["name"]

        self.assertEqual(real_name, activator_name)

    def test_update_activator_field(self):
        _id = ObjectId()
        self._device_data["_id"] = _id
        self._direct_database.insert_one(self._device_data)

        activators = self._direct_database.find_one({"_id": _id})["activators"]
        act_id = list(activators.keys())[0]

        new_name = "new_name"
        self._database.update_activator_field(_id, act_id, "name", new_name)

        name_in_database = self._direct_database.find_one({"_id": _id})["activators"][act_id]["name"]

        self.assertEqual(name_in_database, new_name)
