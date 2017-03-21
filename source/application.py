from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

from model.Action import Action
from model.Device import Device
from model.DeviceDAO import DeviceDAO

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='0.2', title='Hestia Home Automation app'
          ,description='A home automation hub for all your IOT devices'
)

ns = api.namespace('devices', description='All devices of the system')

light = Device("Light")
light.addAction(Action("On/Off", 'Boolean'))
light.addAction(Action("Color", 'Interval0-1'))

lock = Device("Lock")
lock.addAction(Action("Open/Close", 'Boolean'))

DAO = DeviceDAO()
DAO.addDevice(light)
DAO.addDevice(lock)

action = api.model('Action', {
    'actionId': fields.Integer(readOnly=True, required=True, discription='The unique identifier of the action'),
    'name': fields.String(readOnly=True, required=True, description='The name of the action'),
    'actionType': fields.String(readOnly=True, required=True, description='The type of interaction you can have'),
    'state': fields.Float(required=True, dicription='The state of an action')
})

device = api.model('Device', {
    'deviceId': fields.Integer(readOnly=True, required=True, description='The unique identifier of the device'),
    'name': fields.String(required=True, description='The name of the device'),
    'actions': fields.List(fields.Nested(action))
})


@ns.route('/')
class Devices(Resource):
    '''Shows a list of all devices, and lets you POST to add new device'''
    @ns.doc('list_devices')
    @ns.marshal_list_with(device)
    def get(self):
        '''List all devices'''
        return DAO.get()

    @ns.doc('create_device')
    @ns.expect(device)
    @ns.marshal_with(device, code=201)
    def post(self):
        '''Create a new device'''
        return DAO.addDevice(api.payload), 201


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


@ns.route('/<int:deviceId>/action/<int:actionId>')
@ns.response(404, 'Device or action not found')
@ns.param('deviceId', 'The device ID')
@ns.param('actionId', 'The action ID')
class Action(Resource):
    ''' Show a single action, and put a new value'''
    @ns.doc('get_action')
    @ns.marshal_with(action)
    def get(self, deviceId, actionId):
        ''' Fetch a given action of a device '''
        device = DAO.getDevice(deviceId)
        return device.get(actionId)

    @ns.doc('put_action')
    @ns.expect(action)
    @ns.marshal_with(action)
    def put(self, deviceId, actionId):
        ''' Put a given action of a device '''
        device = DAO.getDevice(deviceId)
        action = device.get(actionId)
        action.setState(api.payload['state'])
        return action, 201

if __name__ == '__main__':
    app.run(debug=True)