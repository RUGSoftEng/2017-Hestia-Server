from flask_restplus import Resource

from endpoints.devices import DAO, ns
from endpoints.devices.Device import device


@ns.route('/')
class Devices(Resource):
    '''Shows a list of all devices, and lets you POST to add new device'''
    @ns.doc('list_devices')
    @ns.marshal_list_with(device)
    def get(self):
        '''List all devices'''
        return DAO.getDevices()


