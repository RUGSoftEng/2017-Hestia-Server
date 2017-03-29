from flask_restplus import Namespace

from model.Database import Database
from model.PluginManager import PluginManager

plugin_manager = PluginManager()

device_database = Database()

namespace = Namespace('devices', description='All devices of the system')