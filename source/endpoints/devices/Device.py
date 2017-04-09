from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from endpoints.devices.Activator import activator
from endpoints.devices.Devices import device_database

device = namespace.model('Device', {
    'deviceId': fields.Integer(attribute="id", readOnly=True, required=True, description='The unique identifier of the device')
    , 'name': fields.String(required=True, description='The name of the device')
    , 'type': fields.String(attribute='plugin_type',required=True)
    , 'required_info': fields.String(required=True, description='Required info of device')
    , 'activators': fields.List(fields.Nested(activator))
})


@namespace.route('/<int:device_id>')
@namespace.response(404, 'Device not found')
@namespace.param('device_id', 'The device ID')
class Device(Resource):
    """ Show a single device, update and delete a device"""

    @namespace.doc('get_device')
    @namespace.marshal_with(device)
    def get(self, device_id):
        """ Fetch a given device"""
        return device_database.get_device(device_id)

    @namespace.doc('delete_device')
    @namespace.response(204, 'Device deleted')
    def delete(self, device_id):
        """ Delete a device given its identifier"""
        device_database.delete_device(device_id)
        return '', 204
