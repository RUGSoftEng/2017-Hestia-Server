import unittest

from bson import ObjectId

from logic import DeviceCollectionLogic
from tests import tests_util


class TestDeviceCollectionLogic(unittest.TestCase):
    def setUp(self):
        self._database = tests_util.get_database()
        self._plugin_manager = tests_util.get_plugin_manager()


        self._logic = DeviceCollectionLogic(self._database, self._plugin_manager)

    def tearDown(self):
        self._database.delete_all_devices()

    def test_get_all_devices(self):
        flag_device_one_found = False
        flag_device_two_found = False

        self.__create_database_with_one_device()

        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(1, len(retrieved_devices))

        name_device_two = "device_two"
        self._add_device(name_device_two)

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

        devices = self._database.get_all_devices()
        self.assertEqual(1, len(devices))

    def test_get_device(self):
        self.__create_database_with_one_device()

        retrieved_device = self._logic.get_device(self.id_device_one)

        self.assertEqual(self.id_device_one, retrieved_device.identifier)

    def test_remove_device(self):
        self.__create_database_with_one_device()

        count_before_delete = len(self._database.get_all_devices())

        self._logic.remove_device(self.id_device_one)

        count_after_delete = len(self._database.get_all_devices())
        self.assertEqual(count_before_delete - 1, count_after_delete)

    def test_change_device_name(self):
        self.__create_database_with_one_device()
        new_name = "new_name"
        self._logic.change_device_name(self.id_device_one, new_name)
        device = self._logic.get_device(self.id_device_one)
        self.assertEqual(device.name, new_name)

    def __create_database_with_one_device(self):
        self.name_device_one = "device_one"
        self._add_device(self.name_device_one)

    def _add_device(self, name):
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

        self._database.add_device(data)
        devices = self._database.get_all_devices()
        self.id_device_one = devices[0].identifier

    def __get_plugin_information(self, name):
        return {'organization': "mock"
                , 'plugin_name': "lock"
                , 'required_info': {
                    'name': name
                    , 'bridge_ip': '127.0.0.1'
                    , 'bridge_port': '80'
                    }
                }
