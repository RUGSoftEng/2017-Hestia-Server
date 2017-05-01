from flask_restplus import Namespace

from model.PluginManager import PluginManager
from endpoints.plugins.business_logic.RequiredInfo import BusinessLogicRequiredInfo

plugin_manager = PluginManager()
business_logic_required_info = BusinessLogicRequiredInfo(plugin_manager)

namespace = Namespace('plugins', description='All plugins of the system')


