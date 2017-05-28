import unittest

from logic import PluginLogic
from tests.tests_util import get_plugin_manager

class TestPluginLogic(unittest.TestCase):
    """
    A test for the endpoint RequiredInfo.
    It uses a mock list of plugins.
    This means that it depends on the current implementation of the plugin
    manager. When the plugin manager changes this class should change as well.
    """

    def setUp(self):
        plugin_manager = get_plugin_manager()
        self._plugin_logic = PluginLogic(plugin_manager)

    def test_get_organizations(self):
        organizations = self._plugin_logic.get_organizations()
        self.assertEqual(organizations, ["mock"])

    def test_get_plugins_from_plugin_manager_by_organization(self):
        plugins = self._plugin_logic.get_plugins("mock")
        self.assertEqual(plugins, ["lock"])

    def test_get_required_info_from_plugin_manager_by_organization_and_plugin(
            self):
        required_info = self._plugin_logic.get_required_info("mock", "lock")
        expected = self.get_expected_plugin_information()
        self.assertEqual(required_info, expected)

    def get_expected_plugin_information(self):
        return {'collection': "mock"
                , 'plugin_name': "lock"
                , 'required_info': {
                    'name': 'default_name'
                    , 'bridge_ip': '127.0.0.1'
                    , 'bridge_port': '80'
                    }
                 }