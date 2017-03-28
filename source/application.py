from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from endpoints.api import api
from model.Database import Database
from plugins.hestia.dimmableLight.DimmableLight import DimmableLight
from plugins.hestia.simpleLock.simpleLock import SimpleLock

DAO = Database()
DAO.addDevice(SimpleLock())
DAO.addDevice(DimmableLight())

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)