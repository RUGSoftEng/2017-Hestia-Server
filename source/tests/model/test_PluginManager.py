import unittest

from model.PluginManager import PluginManager
from model.util.NotFoundException import NotFoundException
from plugins.mock.lock.Lock import Lock


class TestPluginManager(unittest.TestCase):
    """
    A test for the plugin manager.

    It uses a mock list of plugins.
    This means that it depends on the current implementation of the plugin
    manager. When the plugin manager changes this class should change as well.
    """

    @classmethod
    def setUpClass(cls):
        mock_plugin_manager = PluginManager()
        mock_plugin_manager.plugins = {"Mock": {"Lock": Lock}}
        cls.mock_plugin_manager = mock_plugin_manager

    def test_get_organizations(self):
        organizations = self.mock_plugin_manager.get_organizations()
        self.assertEqual(organizations, ["Mock"])

    def test_get_plugins_of(self):
        plugins = self.mock_plugin_manager.get_plugins_of("Mock")
        self.assertEqual(plugins, ["Lock"])

    def test_get_required_info_of(self):
        plugin_manager = self.mock_plugin_manager
        required_info = plugin_manager.get_required_info_of("Mock", "Lock")
        default_info = Lock._get_default_required_info()
        self.assertEqual(required_info, default_info)

    def test_get_implementation_of(self):
        plugin_manager = self.mock_plugin_manager
        default_info = Lock._get_default_required_info()
        lock = plugin_manager.get_implementation_of(default_info)
        self.assertEqual(type(lock), type(Lock()))

    def test_invalid_organization_in_get_plugins(self):
        with self.assertRaises(NotFoundException):
            self.mock_plugin_manager.get_plugins_of("Invalid")

    def test_invalid_organization_in_get_required_info(self):
        with self.assertRaises(NotFoundException):
            self.mock_plugin_manager.get_required_info_of("Invalid", "Lock")

    def test_invalid_plugin_in_get_required_info(self):
        with self.assertRaises(NotFoundException):
            self.mock_plugin_manager.get_required_info_of("Mock", "Invalid")

    def test_invalid_required_info_in_get_implementation_of(self):
        with self.assertRaises(NotFoundException):
            self.mock_plugin_manager.get_implementation_of("")

    def test_no_organization_in_get_implementation_of(self):
        self.missing_key_in_get_implementation_of("organization")

    def test_no_plugin_in_get_implementation_of(self):
        self.missing_key_in_get_implementation_of("plugin")

    def missing_key_in_get_implementation_of(self, key):
        required_info = Lock._get_default_required_info()
        required_info.pop(key)
        with self.assertRaises(NotFoundException):
            self.mock_plugin_manager.get_implementation_of(required_info)

    def test_invalid_organization_in_get_implementation_of(self):
        self.invalid_value_of_key_in_get_implementation_of("organization")

    def test_invalid_plugin_in_get_implementation_of(self):
        self.invalid_value_of_key_in_get_implementation_of("plugin")

    def invalid_value_of_key_in_get_implementation_of(self, key):
        required_info = Lock._get_default_required_info()
        required_info[key] = "Invalid"
        with self.assertRaises(NotFoundException):
            self.mock_plugin_manager.get_implementation_of(required_info)


if __name__ == '__main__':
    unittest.main()