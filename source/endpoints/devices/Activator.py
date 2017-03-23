from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import ns, DAO
from endpoints.devices.RequiredInfo import RequiredInfo
from endpoints.util.ToString import ToString
from endpoints.util.StateTypeToString import StateTypeToString


activator = ns.model('Activator', {
    'activatorId': fields.Integer(readOnly=True, required=True, discription='The unique identifier of the action')
    ,'name': fields.String(readOnly=True, required=True, description='The name of the action')
    ,'stateType': StateTypeToString(attribute="stateType", readOnly=True, required=True, description='The type of interaction you can have')
    ,'state': ToString(attribute="state", required=True, discription='The state of an action')
    , "requiredInfo": RequiredInfo(attribute="requiredInfo", required=True, discription="The info needed to operate")
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

    @ns.doc('post_activator')
    #@ns.expect(bool)
    @ns.marshal_with(activator)
    def post(self, deviceId, activatorId):
        ''' Post a given action of a device '''
        device = DAO.getDevice(deviceId)
        action = device.getActivator(activatorId)
        #action.perform(ns.payload['state'])
        #action.state("False")
        return 201