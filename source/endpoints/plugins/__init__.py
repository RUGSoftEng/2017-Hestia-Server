from flask_restplus import Namespace
from pymongo.database import Database

from PluginManager import PluginManager
from database.DeviceDatabase import DeviceDatabase
from endpoints.plugins.business_logic.RequiredInfo import BusinessLogicRequiredInfo

device_database = DeviceDatabase()
plugin_manager = PluginManager('deviceConfig', device_database)
business_logic_required_info = BusinessLogicRequiredInfo(plugin_manager)

namespace = Namespace('plugins', description='All plugins of the system')


