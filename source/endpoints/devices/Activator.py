from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from logic import activator_logic

activator = namespace.model("Activator", {
    "activatorId": fields.String(attribute="identifier", readOnly=True, required=True,
                                  description="The unique identifier of the action")
    , "name": fields.String(readOnly=True, required=True, description="The name of the action")
    , "type": fields.String(attribute="type", readOnly=True, required=True,
                            description="The type of interaction you can have")
    , "state": fields.Raw(attribute="state", required=True, description="The state of an action")
})
state = namespace.model("State", {
    "state": fields.Raw(required=True, description="new state of activator")
})


@namespace.route("/<string:device_id>/activators/<string:activator_id>")
@namespace.response(404, "Device or action not found")
@namespace.param("device_id", "The device ID")
@namespace.param("activator_id", "The action ID")
class Activator(Resource):
    """ Show a single action and performs a single action """

    @namespace.doc("get_activator")
    @namespace.marshal_with(activator)
    def get(self, device_id, activator_id):
        """ Fetch a given activator of a device """
        return activator_logic.get_activator(device_id, activator_id)

    @namespace.doc("post_activator")
    @namespace.expect(state)
    @namespace.response(201, "state updated")
    def post(self, device_id, activator_id):
        """ Post a given activator of a device """
        value = namespace.apis[0].payload["state"]
        activator_logic.change_activator_state(device_id, activator_id, value)
        return "state updated", 201