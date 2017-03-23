from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import ns
from endpoints.devices.Activator import activator
from endpoints.devices.Devices import DAO


device = ns.model('Device', {
    'deviceId': fields.Integer(readOnly=True, required=True, description='The unique identifier of the device')
    ,'name': fields.String(required=True, description='The name of the device')
    ,'activators': fields.List(fields.Nested(activator))
})


@ns.route('/<int:deviceId>')
@ns.response(404, 'Device not found')
@ns.param('deviceId', 'The device ID')
class Device(Resource):
    ''' Show a single device, update and delete a device'''
    @ns.doc('get_device')
    @ns.marshal_with(device)
    def get(self, deviceId):
        '''Fetch a given device'''
        return DAO.getDevice(deviceId)

    @ns.doc('delete_device')
    @ns.response(204, 'Device deleted')
    def delete(self, deviceId):
        '''Delete a device given its identifier'''
        DAO.deleteDevice(deviceId)
        return '', 204