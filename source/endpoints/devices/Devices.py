from flask_restplus import Resource
from flask_restplus import fields

from endpoints.devices import device_database, namespace
from endpoints.devices.Device import device
from endpoints.devices import plugin_manager

format_post_device = namespace.model('new_device', {
    'required_info': fields.String(attribute='required_info', required=True,
                              description='The organization and plugin_name of device and additional info')
})


@namespace.route('/')
class Devices(Resource):
    """ Shows a list of all devices and adds a new device with POST """

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
        required_info = namespace.apis[0].payload['required_info']
        new_device_info = eval(required_info)
        name = new_device_info.pop('name', None)
        class_plugin = plugin_manager.get_implementation_of(new_device_info)
        class_plugin.name = name
        device_database.add_device(class_plugin)
        class_plugin.setup()
        return 'new device', 201