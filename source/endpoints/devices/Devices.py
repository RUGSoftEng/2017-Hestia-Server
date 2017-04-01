from flask_restplus import Resource

from endpoints.devices import device_database, namespace
from endpoints.devices.Device import device
from endpoints.util.ToString import ToString
from endpoints.devices import plugin_manager

format_post_device = namespace.model('Device', {
    'organization': ToString(readOnly=True, required=True, discription='The organization')
    ,'plugin_name': ToString(readOnly=True, required=True, description='The name of the plugin')
    , 'required_info': ToString(attribgute='requiredInfo', required=True, discription='The info needed to operate')
})

@namespace.route('/')
class Devices(Resource):
    """ Shows a list of all devices, and lets you POST to add new device"""

    @namespace.doc('list_devices')
    @namespace.marshal_list_with(device)
    def get(self):
        """ List all devices"""
        return device_database.get_devices()

    @namespace.doc('post_device')
    @namespace.expect(format_post_device)
    @namespace.response(201, 'new device')
    def post(self):
        ''' Post a new device '''
        organization = namespace.apis[0].payload["organization"]
        plugin_name = namespace.apis[0].payload["plugin_name"]
        required_info = namespace.apis[0].payload["required_info"]
        class_plugin = plugin_manager.get_implementation_of(organization, plugin_name, required_info)
        device_database.addDevice(class_plugin)