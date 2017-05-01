import unittest

from model.PluginManager import PluginManager
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
        organization = self.mock_plugin_manager.get_organizations()
        self.assertEqual(organization, "Mock")

    def test_get_plugins_of(self):
        plugins = self.mock_plugin_manager.get_plugins_of("Mock")
        self.assertEqual(plugins, "Lock")

    def test_get_required_info_of(self):
        plugin_manager = self.mock_plugin_manager
        required_info = plugin_manager.get_required_info_of("Mock", "Lock")
        default_info = Lock._get_default_required_info()
        self.assertEqual(required_info, default_info)

    def test_implementation_of(self):
        plugin_manager = self.mock_plugin_manager
        default_info = Lock._get_default_required_info()
        lock = plugin_manager.get_implementation_of(default_info)
        self.assertEqual(type(lock), type(Lock()))


if __name__ == '__main__':
    unittest.main()