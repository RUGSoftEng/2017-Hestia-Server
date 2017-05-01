import unittest
from plugins.mock.lock.Lock import Lock


class TestDevice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        mock_instance = Lock()
        mock_instance.id = 1
        mock_instance.name = "Name"
        cls.mock_Instance = mock_instance
        cls.mock_Class = Lock
        cls.default_required_info = {'ip': ''
                                     , 'maximum spin speed': ''
                                     , 'organization': 'Mock'
                                     , 'plugin': 'Lock'
                                     , 'port': ''}

    def test_class_plugin_name(self):
        self.assertEqual(self.mock_Class._get_plugin_name(), "Lock")

    def test_class_organization(self):
        self.assertEqual(self.mock_Class._get_organization(), "Mock")

    def test_class_default_required_info(self):
        self.assertEqual(self.mock_Class._get_default_required_info()
                         , self.default_required_info)

    def test_class_plugin_typ(self):
        self.assertEqual(self.mock_Class._get_plugin_type(), "Lock")

    def test_instance_name(self):
        self.assertEqual(self.mock_Instance.name, "Name")

    def test_instance_plugin_name(self):
        self.assertEqual(self.mock_Instance.plugin_name, "Lock")

    def test_instance_organization(self):
        self.assertEqual(self.mock_Instance.organization, "Mock")

    def test_instance_required_info(self):
        self.assertEqual(self.mock_Instance.required_info
                         , self.default_required_info)

    def test_instance_plugin_typ(self):
        self.assertEqual(self.mock_Instance.plugin_type, "Lock")

    def test_instance_id(self):
        self.assertEqual(self.mock_Instance.id, 1)


if __name__ == '__main__':
    unittest.main()