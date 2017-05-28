from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import namespace
from endpoints.devices.Device import device
from logic import device_logic

format_post_device = namespace.model("new_device", {
    "required_info": fields.Raw(attribute="required_info", required=True,
                                   description="The collection and plugin_name of device and additional info")
})


@namespace.route("/")
class Devices(Resource):
    """ Shows a list of all devices and adds a new device with POST """

    @namespace.doc("list_devices")
    @namespace.marshal_list_with(device)
    def get(self):
        """ List all devices """
        devices = device_logic.get_all_devices()
        return devices

    @namespace.doc("post_device")
    @namespace.expect(format_post_device)
    @namespace.response(201, "new device")
    def post(self):
        """ Post a new device """
        json_required_info = namespace.apis[0].payload["required_info"]
        device_logic.create_new_device(json_required_info)
        return "new device", 201