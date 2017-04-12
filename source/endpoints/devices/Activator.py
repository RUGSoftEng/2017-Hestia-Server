from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace, device_database

activator = namespace.model('Activator', {
    'activatorId': fields.Integer(attribute='id', readOnly=True, required=True,
                                  description='The unique identifier of the action')
    , 'name': fields.String(readOnly=True, required=True, description='The name of the action')
    , 'type': fields.String(attribute='type', readOnly=True, required=True,
                            description='The type of interaction you can have')
    , 'state': fields.String(attribute='state', required=True, description='The state of an action')
})
state = namespace.model('State', {
    'state': fields.String(required=True, description='new state of activator')
})


@namespace.route('/<int:device_id>/activators/<int:activator_id>')
@namespace.response(404, 'Device or action not found')
@namespace.param('device_id', 'The device ID')
@namespace.param('activator_id', 'The action ID')
class Activator(Resource):
    """ Show a single action and performs a single action """

    @namespace.doc('get_activator')
    @namespace.marshal_with(activator)
    def get(self, device_id, activator_id):
        """ Fetch a given action of a device """
        device = device_database.get_device(device_id)
        return device.get_activator(activator_id)

    @namespace.doc('post_activator')
    @namespace.expect(state)
    @namespace.response(201, 'state updated')
    def post(self, device_id, activator_id):
        """ Post a given action of a device """
        device = device_database.get_device(device_id)
        action = device.get_activator(activator_id)
        value = namespace.apis[0].payload['state']
        action.set_state_with_string(value)
        action.perform(device.required_info)
        return 'state updated', 201