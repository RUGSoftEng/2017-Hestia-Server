import unittest

from endpoints.devices.business_logic.Activator import BusinessLogicActivator
from model.Database import Database
from plugins.mock.lock.Lock import Lock


class TestEndpointActivator(unittest.TestCase):
    def setUp(self):
        self._database = Database()
        self._logic = BusinessLogicActivator(self._database)

    def test__get_activator(self):
        lock = Lock()
        self._database.add_device(lock)
        device_id = lock.id
        activator_id = 0
        activator = lock.get_activator(activator_id)

        retrieved_activator = self._logic.get_activator_from_database_by_device_and_activator_id(device_id, activator_id)

        self.assertEqual(activator, retrieved_activator)

    def test_change_activator_state(self):
        lock = Lock()
        self._database.add_device(lock)
        device_id = lock.id
        activator_id = 0
        activator = lock.get_activator(activator_id)

        requested_state = True
        self._logic.change_activator_state_with_string(device_id, activator_id, str(requested_state))
        self.assertEqual(requested_state, activator.state)

        requested_state = False
        self._logic.change_activator_state_with_string(device_id, activator_id, str(requested_state))
        self.assertEqual(requested_state, activator.state)