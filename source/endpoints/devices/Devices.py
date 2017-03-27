from flask_restplus import Resource

from endpoints.devices import device_database, namespace
from endpoints.devices.Device import device


@namespace.route('/')
class Devices(Resource):
    '''Shows a list of all devices, and lets you POST to add new device'''
    @namespace.doc('list_devices')
    @namespace.marshal_list_with(device)
    def get(self):
        '''List all devices'''
        return device_database.getDevices()


