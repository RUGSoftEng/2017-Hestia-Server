from flask_restplus import Resource

from endpoints.devices import device_database, namespace
from endpoints.devices.Device import device
from endpoints.util.ToString import ToString
from endpoints.devices import plugin_manager

format_post_device = namespace.model('Device', {
    'required_info': ToString(attribute='required_info', required=True, discription='The info needed to operate')
})

@namespace.route('/')
class Devices(Resource):
    """ Shows a list of all devices, and lets you POST to add new device"""

    @namespace.doc('list_devices')
    @namespace.marshal_list_with(device)
    def get(self):
        """ List all devices """
        return device_database.get_devices()

    @namespace.doc('post_device')
    @namespace.expect(format_post_device)
    @namespace.response(201, 'new device')
    def post(self):
        """ Post a new device """
        info = namespace.apis[0].payload['required_info']
        required_info = eval(info)
        name = required_info.pop("name", None)
        class_plugin = plugin_manager.get_implementation_of(required_info)
        class_plugin.name = name
        device_database.add_device(class_plugin)
        class_plugin.setup()