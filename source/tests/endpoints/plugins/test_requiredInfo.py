import unittest

from endpoints.plugins.business_logic.RequiredInfo import BusinessLogicRequiredInfo
from model.PluginManager import PluginManager
from plugins.mock.lock.Lock import Lock


class TestEndpointBusinessLogicRequiredInfo(unittest.TestCase):
    """
    A test for the endpoint RequiredInfo.
    It uses a mock list of plugins.
    This means that it depends on the current implementation of the plugin
    manager. When the plugin manager changes this class should change as well.
    """

    def setUp(self):
        self._plugin_manager = PluginManager()
        self._logic = BusinessLogicRequiredInfo(self._plugin_manager)
        self._plugin_manager.plugins = {"Mock": {"Lock": Lock}}

    def test_get_organizations_from_plugin_manager(self):
        organizations = self._logic.get_organizations()
        self.assertEqual(organizations, ["Mock"])

    def test_get_plugins_from_plugin_manager_by_organization(self):
        plugins = self._logic.get_plugins_by_organization("Mock")
        self.assertEqual(plugins, ["Lock"])

    def test_get_required_info_from_plugin_manager_by_organization_and_plugin(self):
        required_info = self._logic.get_required_info("Mock", "Lock")
        default_info = Lock._get_default_required_info()
        default_info["name"] = "default"
        self.assertEqual(required_info, default_info)