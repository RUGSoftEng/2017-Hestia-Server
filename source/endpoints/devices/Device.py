from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from endpoints.devices.Activator import activator
from endpoints.error_handling import handle_hestia_exception, handle_standard_exception
from exceptions.HestiaException import HestiaException
from logic import device_logic

device = namespace.model("Device", {
    "deviceId": fields.String(attribute="identifier", readOnly=True, required=True,
                               description="The unique identifier of the device")
    , "name": fields.String(required=True, description="The name of the device")
    , "type": fields.String(attribute="type",required=True)
    , "activators": fields.List(fields.Nested(activator))
})

name = namespace.model("Name", {
    "name": fields.String(required=True, description="The new name of the device")
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
        try:
            return_device = device_logic.get_device(device_id)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return return_device

    @namespace.doc("delete_device")
    @namespace.response(204, "Device deleted")
    def delete(self, device_id):
        """ Delete a device given its identifier """
        try:
            device_logic.remove_device(device_id)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return "", 204

    @namespace.doc("put_name")
    @namespace.expect(name)
    @namespace.response(201, "name changed")
    def put(self, device_id):
        """ Put a new name for device given its identifier """
        try:
            new_name = namespace.apis[0].payload["name"]
            device_logic.change_device_name(device_id, new_name)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return "name changed", 201
