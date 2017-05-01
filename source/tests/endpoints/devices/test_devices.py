import unittest
import json

from endpoints.devices.business_logic.Devices import BusinessLogicDevices
from model.Database import Database
from model.PluginManager import PluginManager
from plugins.mock.light.Light import Light
from plugins.mock.lock.Lock import Lock


class TestDevices(unittest.TestCase):

    def setUp(self):
        self._database = Database()
        self._plugin_manager = PluginManager()
        self._logic = BusinessLogicDevices(self._database, self._plugin_manager)

    def test_database_set_correctly(self):
        self.assertEqual(self._database, self._logic._database)

    def test_plugin_manager_set_correctly(self):
        self.assertEqual(self._plugin_manager, self._logic._plugin_manager)

    @unittest.skip("Currently not working because of singleton")
    def test_get_all_devices_from_database(self):
        lock = Lock()
        light = Light()
        self._database.add_device(lock)
        self._database.add_device(light)

        devices = self._logic.get_all_devices_from_database()

        self.assertIn(lock, devices)
        self.assertIn(light, devices)

    @unittest.skip("Currently not working because of singleton")
    def test_get_all_devices_from_database_not_containing_other_devices(self):
        lock = Lock()
        light = Light()
        self._database.add_device(lock)
        self._database.add_device(light)

        devices = self._logic.get_all_devices_from_database()
        devices_length = len(devices)

        self.assertEqual(devices_length, 2)

    def test_create_new_device_from_json(self):
        test_name = "test_name"
        test_organization = "Mock"
        test_plugin_name = "Light"
        test_ip = "127.0.0.1"
        test_port = "0"
        json_data = self.create_json(test_name, test_organization, test_plugin_name, test_ip, test_port)

        plugin = self._logic.create_new_device_from_json_input(json_data)

        self.assertIsNotNone(plugin)

    def test_create_new_device_from_json_name_is_correct(self):
        test_name = "test_name"
        test_organization = "Mock"
        test_plugin_name = "Light"
        test_ip = "127.0.0.1"
        test_port = "0"
        json_data = self.create_json(test_name, test_organization, test_plugin_name, test_ip, test_port)

        plugin = self._logic.create_new_device_from_json_input(json_data)

        self.assertEqual(plugin.name, test_name)

    def test_install_new_device_setup_done(self):
        light = Light()

        self._logic.install_new_device(light)

        self.assertTrue(light._is_setup_done)

    def create_json(self, test_name, test_organization, test_plugin_name, test_ip,test_port):
        json_data = {}
        json_data["name"] = str(test_name)
        json_data["organization"] = str(test_organization)
        json_data["plugin"] = str(test_plugin_name)
        json_data["ip"] = str(test_ip)
        json_data["test_port"] = str(test_port)

        return json.dumps(json_data)

