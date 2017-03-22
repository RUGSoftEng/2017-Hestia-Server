from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import ns, DAO
from endpoints.util.ToString import ToString

activator = ns.model('Activator', {
    'activatorId': fields.Integer(readOnly=True, required=True, discription='The unique identifier of the action')
    ,'name': fields.String(readOnly=True, required=True, description='The name of the action')
    ,'stateType': ToString(attribute="stateType", readOnly=True, required=True, description='The type of interaction you can have')
    ,'state': ToString(attribute="state", required=True, dicription='The state of an action')
})

@ns.route('/<int:deviceId>/activator/<int:activatorId>')
@ns.response(404, 'Device or action not found')
@ns.param('deviceId', 'The device ID')
@ns.param('activatorId', 'The action ID')
class Activator(Resource):
    ''' Show a single action, and put a new value'''
    @ns.doc('get_activator')
    @ns.marshal_with(activator)
    def get(self, deviceId, activatorId):
        ''' Fetch a given action of a device '''
        device = DAO.getDevice(deviceId)
        return device.getActivator(activatorId)

    @ns.doc('put_activator')
    @ns.expect(activator)
    @ns.marshal_with(activator)
    def put(self, deviceId, activatorID):
        ''' Put a given action of a device '''
        device = DAO.getDevice(deviceId)
        action = device.getActivator(activatorID)
        action.perform(ns.payload['state'])
        return action, 201