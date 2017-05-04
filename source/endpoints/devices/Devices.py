from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import business_logic_devices, namespace
from endpoints.devices import plugin_manager
from endpoints.devices.Device import device

format_post_device = namespace.model("new_device", {
    "required_info": fields.String(attribute="required_info", required=True,
                                   description="The organization and plugin_name of device and additional info")
})


@namespace.route("/")
class Devices(Resource):
    """ Shows a list of all devices and adds a new device with POST """

    @namespace.doc("list_devices")
    @namespace.marshal_list_with(device)
    def get(self):
        """ List all devices """
        return business_logic_devices.get_all_devices_from_database()

    @namespace.doc("post_device")
    @namespace.expect(format_post_device)
    @namespace.response(201, "new device")
    def post(self):
        """ Post a new device """
        json_required_info = namespace.apis[0].payload["required_info"]
        plugin = business_logic_devices.create_new_device_from_json_input(json_required_info)
        business_logic_devices.install_new_device(plugin)
        return "new device", 201