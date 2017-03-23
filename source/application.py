from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from endpoints.api import api
from model.DeviceDAO import DeviceDAO
from plugins.simpleLock.simpleLock import simpleLock
from plugins.dimmableLight.DimmableLight import DimmableLight

DAO = DeviceDAO()
DAO.addDevice(simpleLock())
#DAO.addDevice(DimmableLight())

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)