import unittest

from endpoints.devices.business_logic.Device import BusinessLogicDevice
from model.Database import Database
from plugins.mock.lock.Lock import Lock


class TestEndpointDevice(unittest.TestCase):

    def setUp(self):
        self._database = Database()
        self._logic = BusinessLogicDevice(self._database)

    def tearDown(self):
        self._database.devices.clear()

    def test_database_set_correctly(self):
        self.assertEqual(self._database, self._logic._database)

    def test_get_device_from_database_by_id(self):
        device_id = 0
        mock_device = Lock()
        self._database.add_device(mock_device)

        retrieved_device = self._logic.get_device_from_database_by_id(device_id)
        self.assertEqual(mock_device, retrieved_device)

    def test_remove_device_from_database_by_id(self):
        device_id = 0
        mock_device = Lock()
        self._database.add_device(mock_device)

        database_size_before_delete = len(self._database.devices)
        self._logic.remove_device_from_database_by_id(device_id)
        database_size_after_delete = len(self._database.devices)
        self.assertEqual(database_size_before_delete-1, database_size_after_delete)

