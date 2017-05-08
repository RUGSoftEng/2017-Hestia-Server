from flask_restplus import Namespace

from PluginManager import PluginManager
from database.DeviceDatabase import DeviceDatabase
from endpoints.devices.business_logic.Activator import BusinessLogicActivator
from endpoints.devices.business_logic.Device import BusinessLogicDevice
from endpoints.devices.business_logic.Devices import BusinessLogicDevices

device_database = DeviceDatabase()
plugin_manager = PluginManager('deviceConfig', device_database)
business_logic_device = BusinessLogicDevice(device_database)
business_logic_devices = BusinessLogicDevices(device_database, plugin_manager)
business_logic_activator = BusinessLogicActivator(device_database)

namespace = Namespace('devices', description='All devices of the system')
