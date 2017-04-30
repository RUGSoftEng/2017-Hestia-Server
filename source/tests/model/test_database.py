import unittest
from model.Database import Database
from plugins.mock.lock.Lock import Lock


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.database_instance = Database()

        self.mock_instance_lock = Lock()
        self.mock_instance_lock.id = 0

        self.database_instance.devices.append(self.mock_instance_lock)
        self.database_instance.get_new_counter()


    def test_get_device(self):
        device = self.database_instance.get_device(0)
        self.assertEqual(device, self.mock_instance_lock)

    def test_add_device(self):
        device_0 = self.database_instance.get_device(0)
        self.database_instance.add_device(self.mock_instance_lock)
        device_1 = self.database_instance.get_device(1)
        self.assertEqual(device_0, device_1)


    def test_delete_device(self):
        empty_list = list()
        self.database_instance.delete_device(0)
        self.assertEqual(self.database_instance.get_devices(), empty_list)


if __name__ == '__main__':
    unittest.main()