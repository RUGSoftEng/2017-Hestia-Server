import unittest

from PluginManager import PluginManager
from database.DeviceDatabase import DeviceDatabase
from logic import DeviceCollectionLogic


class TestEndpointActivator(unittest.TestCase):
    def setUp(self):
        self._database = DeviceDatabase("testing")
        self._plugin_manager = PluginManager('source/tests/testing_deviceConfig', self._database)

        self._logic = DeviceCollectionLogic(self._database, self._plugin_manager)

    def tearDown(self):
        devices = self._database.get_all_devices()
        for device in devices:
            self._database.delete_device(device.identifier)

    def test_get_all_devices(self):
        device1_req = self._plugin_manager.get_required_info_of("mock", "Lock")
        self._plugin_manager.implement_plugin("mock", "Lock", "test1", device1_req)
        retrieved_devices = self._logic.get_all_devices()
        self.assertEqual(1, len(retrieved_devices))

        device2_req = self._plugin_manager.get_required_info_of("mock", "Lock")
        self._plugin_manager.implement_plugin("mock", "Lock", "test2", device2_req)
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

        self.assertEqual(count_before_delete-1, len(self._database.get_all_devices()))

