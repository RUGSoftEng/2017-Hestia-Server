from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from endpoints.devices.Activator import activator
from endpoints.devices.Devices import device_database


device = namespace.model('Device', {
    'deviceId': fields.Integer(readOnly=True, required=True, description='The unique identifier of the device')
    ,'name': fields.String(required=True, description='The name of the device')
    ,'activators': fields.List(fields.Nested(activator))
})


@namespace.route('/<int:deviceId>')
@namespace.response(404, 'Device not found')
@namespace.param('deviceId', 'The device ID')
class Device(Resource):
    ''' Show a single device, update and delete a device'''
    @namespace.doc('get_device')
    @namespace.marshal_with(device)
    def get(self, deviceId):
        '''Fetch a given device'''
        return device_database.getDevice(deviceId)

    @namespace.doc('delete_device')
    @namespace.response(204, 'Device deleted')
    def delete(self, deviceId):
        '''Delete a device given its identifier'''
        device_database.deleteDevice(deviceId)
        return '', 204