import unittest

from bson import ObjectId
from pymongo import MongoClient

from models.Device import Device
from tests import test_util


class TestDeviceDatabaseMongoDB(unittest.TestCase):
    def setUp(self):
        self._database = test_util.get_mongo_database()
        self._direct_database = MongoClient()["Hestia"]["testing"]

    def tearDown(self):
        self._direct_database.delete_many({})

    def test_get_all_devices(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)

        retrieved_devices = self._database.get_all_devices()

        self.assertEqual(1, len(retrieved_devices))

        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)

        retrieved_devices = self._database.get_all_devices()

        self.assertEqual(2, len(retrieved_devices))

    def test_get_device(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)

        device = self._database.get_device(device_data["_id"])

        self.assertEqual(device_data["name"], device.name)
        self.assertIsInstance(device, Device)

    def test_add_device(self):
        device_data = self._get_device_data()
        initial_count = self._direct_database.count()

        self._database.add_device(device_data)

        self.assertEqual(initial_count+1, self._direct_database.count())

    def test_delete_device(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)
        initial_count = self._direct_database.count()

        self._database.delete_device(device_data["_id"])

        self.assertEqual(initial_count - 1, self._direct_database.count())


    def test_update_field(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)
        new_name = "Hestia"

        self._database.update_field(device_data["_id"], "name", new_name)

        device = self._direct_database.find_one({"_id": device_data["_id"]})
        self.assertEqual(device["name"], new_name)

    def test_get_field(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)

        name = self._database.get_field(device_data["_id"], "name")

        self.assertEqual(device_data["name"], name)

    def test_get_activator_field(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)

        activators = self._direct_database.find_one({"_id": device_data["_id"]})["activators"]
        act_id = list(activators.keys())[0]

        activator_name = self._database.get_activator_field(device_data["_id"], act_id, "name")

        real_name = device_data["activators"][act_id]["name"]

        self.assertEqual(real_name, activator_name)

    def test_update_activator_field(self):
        device_data = self._get_device_data()
        device_data["_id"] = str(ObjectId())
        self._direct_database.insert_one(device_data)

        activators = self._direct_database.find_one({"_id": device_data["_id"]})["activators"]
        act_id = list(activators.keys())[0]

        new_name = "new_name"
        self._database.update_activator_field(device_data["_id"], act_id, "name", new_name)

        device_in_db = self._direct_database.find_one({"_id": device_data["_id"]})
        activator_name_in_db = device_in_db["activators"][act_id]["name"]

        self.assertEqual(activator_name_in_db, new_name)

    def _get_device_data(self):
        device_data = {
            "module": "plugins.mock.lock.Lock",
            "class": "Lock",
            "type": "Lock",
            "name": "TestDevice",
            "options": {
                "bridge_ip": "127.0.2.1",
                "bridge_port": 90
            },
            "activators": [
                {
                    "module": "plugins.mock.ActivateLock",
                    "rank": 0,
                    "class": "ActivateLock",
                    "name": "Activate",
                    "type": "bool",
                    "state": True
                }
            ]
        }
        activators = device_data.pop("activators", None)
        device_data["activators"] = {}
        for activator in activators:
            _id = str(ObjectId())
            device_data["activators"][_id] = activator
        return device_data
