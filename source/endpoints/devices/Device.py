from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from endpoints.devices.Activator import activator
from logic import device_logic

device = namespace.model("Device", {
    "deviceId": fields.String(attribute="identifier", readOnly=True, required=True,
                               description="The unique identifier of the device")
    , "name": fields.String(required=True, description="The name of the device")
    , "type": fields.String(attribute="type",required=True)
    , "activators": fields.List(fields.Nested(activator))
})


@namespace.route("/<string:device_id>")
@namespace.response(404, "Device not found")
@namespace.param("device_id", "The device ID")
class Device(Resource):
    """ Show a single device and delete a device """

    @namespace.doc("get_device")
    @namespace.marshal_with(device)
    def get(self, device_id):
        """ Fetch a device given its identifier """
        return device_logic.get_device(device_id)

    @namespace.doc("delete_device")
    @namespace.response(204, "Device deleted")
    def delete(self, device_id):
        """ Delete a device given its identifier """
        device_logic.remove_device(device_id)
        return "", 204
