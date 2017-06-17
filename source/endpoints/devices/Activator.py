from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from endpoints.error_handling import handle_standard_exception, handle_hestia_exception
from exceptions.HestiaException import HestiaException
from logic import activator_logic

activator = namespace.model("Activator", {
    "activatorId": fields.String(attribute="identifier", readOnly=True, required=True,
                                  description="The unique identifier of the action")
    , "rank": fields.Integer(attribute="rank", readOnly=True, required=True,
                                  description="The rank of the activator")
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
        try:
            return_activator = activator_logic.get_activator(device_id, activator_id)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return return_activator

    @namespace.doc("post_activator")
    @namespace.expect(state)
    @namespace.response(201, "state updated")
    def post(self, device_id, activator_id):
        """ Post a given activator of a device """
        try:
            value = namespace.apis[0].payload["state"]
            activator_logic.change_activator_state(device_id, activator_id, value)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return "state updated", 201