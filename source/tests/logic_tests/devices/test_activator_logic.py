import unittest

from logic import ActivatorLogic
from tests import test_util


class TestActivatorLogic(unittest.TestCase):
    def setUp(self):
        self._database = test_util.get_database()
        self._plugin_manager = test_util.get_plugin_manager(self._database)

        req = self._plugin_manager.get_required_info_of("mock", "Lock")
        plugin = self._plugin_manager.get_plugin("mock", "Lock", req)
        plugin["name"] = "TestDevice"
        self._database.add_device(plugin)

        devices = self._database.get_all_devices()

        self._device = devices[0]
        self._activator = self._device.activators[0]

        self._logic = ActivatorLogic(self._database)

    def tearDown(self):
        self._database.delete_device(self._device.identifier)

    def test_get_activator(self):
        retrieved_activator = self._logic.get_activator(self._device.identifier, self._activator.identifier)

        self.assertEqual(self._activator.name, retrieved_activator.name)
        self.assertEqual(self._activator.type, retrieved_activator.type)

    def test_boolean_change_activator_state(self):
        requested_state = True
        self._logic.change_activator_state(self._device.identifier, self._activator.identifier, requested_state)
        self.assertEqual(requested_state, self._activator.state)

        requested_state = False
        self._logic.change_activator_state(self._device.identifier, self._activator.identifier, requested_state)
        self.assertEqual(requested_state, self._activator.state)
