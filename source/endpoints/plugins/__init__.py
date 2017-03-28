from flask_restplus import Namespace

from model.PluginManager import PluginManager

plugin_manager = PluginManager()

namespace = Namespace('plugins', description='All plugins of the system')
