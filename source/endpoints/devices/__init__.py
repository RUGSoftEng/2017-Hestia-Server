from flask_restplus import Namespace

from endpoints.devices.business_logic.Device import BusinessLogicDevice
from endpoints.devices.business_logic.Devices import BusinessLogicDevices
from model.Database import Database
from model.PluginManager import PluginManager

plugin_manager = PluginManager()

device_database = Database()
business_logic_device = BusinessLogicDevice(device_database)
business_logic_devices = BusinessLogicDevices(device_database, PluginManager)

namespace = Namespace('devices', description='All devices of the system')
