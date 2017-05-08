from bson import ObjectId
from flask import Flask
from pymongo import MongoClient
from werkzeug.contrib.fixers import ProxyFix

from PluginManager import PluginManager
from database.DeviceDatabase import DeviceDatabase
from endpoints.api import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


#db = DeviceDatabase()
#pm = PluginManager('deviceConfig', db)
#ri = {
#        "bridge_ip": "127.1.0.1",
#        "bridge_port": 7000
#      }
#pm.implement_plugin("mock", "Lock", "Slot", ri)

#devices = db.get_all_devices()
#device = db.get_device("591021a7edc9f0447516e20a")
#name = device.name
#device.name = 'test'
#new_name = device.name
#options = device.options
#activator = device.get_activator("591021a7edc9f0447516e209")
#name = activator.name
#activators["278521d2-33bb-11e7-9079-305a3ae07a6a"].perform(options)

api.init_app(app)

if __name__ == "__main__":
    """ Setting host to 0.0.0.0 makes it available within the network. """
    app.run(debug=True, host="0.0.0.0", port=8000)
