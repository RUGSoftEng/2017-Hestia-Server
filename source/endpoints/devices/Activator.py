from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace, device_database
from endpoints.util.StateTypeToString import StateTypeToString
from endpoints.util.ToString import ToString

activator = namespace.model('Activator', {
    'activatorId': fields.Integer(readOnly=True, required=True, discription='The unique identifier of the action')
    ,'name': fields.String(readOnly=True, required=True, description='The name of the action')
    ,'stateType': StateTypeToString(attribute="stateType", readOnly=True, required=True, description='The type of interaction you can have')
    ,'stateString': ToString(attribute="state", required=True, discription='The state of an action')
    , "requiredInfo": ToString(attribgute="requiredInfo", required=True, discription="The info needed to operate")
})
state = namespace.model('State', {
    'state': fields.String(required = True, discription = 'new state of activator')
})

@namespace.route('/<int:deviceId>/activators/<int:activatorId>')
@namespace.response(404, 'Device or action not found')
@namespace.param('deviceId', 'The device ID')
@namespace.param('activatorId', 'The action ID')
class Activator(Resource):
    ''' Show a single action, and put a new value'''
    @namespace.doc('get_activator')
    @namespace.marshal_with(activator)
    def get(self, deviceId, activatorId):
        ''' Fetch a given action of a device '''
        device = device_database.getDevice(deviceId)
        return device.getActivator(activatorId)

    @namespace.doc('post_activator')
    @namespace.expect(state)
    @namespace.response(201, 'state changed')
    def post(self, deviceId, activatorId):
        ''' Post a given action of a device '''
        device = device_database.getDevice(deviceId)
        action = device.getActivator(activatorId)
        value = namespace.apis[0].payload["state"]
        action.setStateWithString(value)
        action.perform()