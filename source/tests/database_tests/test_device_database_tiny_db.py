import unittest

from bson import ObjectId

from tests import test_util


class TestDeviceDatabaseTinyDB(unittest.TestCase):
    def setUp(self):
        self.database = test_util.get_tiny_database()
        self.direct = self.database._devices
        self.empty_data = []

    def tearDown(self):
        self.direct.purge_tables()

    def test_get_all_devices(self):
        self._insert_one_device_and_get_id()
        retieved_devices = self.database.get_all_devices()
        self.assertEqual(1, len(retieved_devices))

        self._insert_one_device_and_get_id()
        retieved_devices = self.database.get_all_devices()
        self.assertEqual(2, len(retieved_devices))


    def test_add_device(self):
        self.database.add_device(self._get_device_data())
        database_data = self.direct.all()
        self.assertNotEqual(database_data, self.empty_data)

    def test_get_device(self):
        device_id = self._insert_one_device_and_get_id()
        database_data = self.database.get_device(device_id)
        self.assertNotEqual(database_data, self.empty_data)

    def test_delete_device(self):
        device_id = self._insert_one_device_and_get_id()
        self.database.delete_device(device_id)
        database_data = self.direct.all()
        self.assertEqual(database_data, self.empty_data)

    def test_get_field(self):
        device_id = self._insert_one_device_and_get_id()
        database_data = self.database.get_field(device_id, "name")
        self.assertEqual(database_data, "TestDevice")

    def test_get_activator_field(self):
        device_id = self._insert_one_device_and_get_id()
        direct_data = self.direct.all()
        activators = direct_data[0]["activators"]
        activator_id = next(iter(activators.keys()))
        field = "class"
        expected_data = activators[activator_id][field]
        database_data = self.database.get_activator_field(device_id
                                                          , activator_id
                                                          , field)
        self.assertEqual(expected_data, database_data)

    def test_update_field(self):
        device_id = self._insert_one_device_and_get_id()
        expected_value = "Changed"
        field = "name"
        self.database.update_field(device_id, field, expected_value)
        changed_value = self.direct.all()[0][field]
        self.assertEqual(expected_value, changed_value)

    def test_update_activator_field(self):
        device_id = self._insert_one_device_and_get_id()
        direct_data = self.direct.all()
        activators = direct_data[0]["activators"]
        activator_id = next(iter(activators.keys()))
        field = "name"
        expected_value = "Changed"
        self.database.update_activator_field(device_id, activator_id
                                             , field, expected_value)
        activators = self.direct.all()[0]["activators"]
        changed_value = activators[activator_id][field]
        self.assertEqual(expected_value, changed_value)

    def _insert_one_device_and_get_id(self):
        device_id = str(ObjectId())
        device_data = self._get_device_data()
        device_data['_id'] = device_id
        self.direct.insert(device_data)
        return device_id

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
                },
                {
                    "module": "plugins.mock.ActivateLock",
                    "rank": 0,
                    "class": "ActivateLock",
                    "name": "Activate#2",
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
