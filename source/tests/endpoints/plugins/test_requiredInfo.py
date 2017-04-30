import unittest

from endpoints.plugins.business_logic.RequiredInfo import BusinessLogicRequiredInfo
from model.PluginManager import PluginManager
from plugins.mock.lock.Lock import Lock


class TestEndpointDevice(unittest.TestCase):

    def setUp(self):
        self._plugin_manager = PluginManager()
        self._logic = BusinessLogicRequiredInfo(self._plugin_manager)
        self._plugin_manager.plugins = {"Mock": {"Lock": Lock}}

    def test_get_organizations_from_plugin_manager(self):
        organization = self._plugin_manager.get_organizations()
        self.assertEqual(organization, "Mock")

    def test_get_plugins_from_plugin_manager_by_organization(self):
        plugins = self._plugin_manager.get_plugins_of("Mock")
        self.assertEqual(plugins, "Lock")

    def test_get_required_info_from_plugin_manager_by_organization_and_plugin(self):
        #plugin_manager = self._plugin_manager
        required_info = self.plugin_manager.get_required_info_of("Mock", "Lock")
        default_info = Lock._get_default_required_info()
        self.assertEqual(required_info, default_info)