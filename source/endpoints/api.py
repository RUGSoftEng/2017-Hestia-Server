from flask_restplus import Api

from .devices.Devices import namespace as devices_namespace
from .plugins.RequiredInfo import namespace as plugin_namespace

api = Api(
    version='0.4'
    , title='Hestia Home Automation app'
    , description='A home automation hub for all your IOT devices'
)


api.add_namespace(devices_namespace)
api.add_namespace(plugin_namespace)
