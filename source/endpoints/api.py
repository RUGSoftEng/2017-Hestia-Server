from flask_restplus import Api
from .devices.Devices import namespace as devicesNamespace
from .plugins.Organizations import namespace as pluginNamespace

api = Api(
    version='0.2'
    ,title='Hestia Home Automation app'
    ,description='A home automation hub for all your IOT devices'
)

api.add_namespace(devicesNamespace)
api.add_namespace(pluginNamespace)
