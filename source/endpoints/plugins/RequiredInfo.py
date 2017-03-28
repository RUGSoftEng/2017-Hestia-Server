from flask_restplus import Resource

from endpoints.plugins import plugin_manager, namespace


@namespace.route('/<string:organization>/plugins/<string:plugin_name>')
@namespace.response(404, 'Organization or plugin not found')
@namespace.param('organization', 'The name of the organization of the plugin')
@namespace.param('plugin_name', 'The name of the plugin')
class RequiredInfo(Resource):
    ''' Show the required information of a plugin'''
    @namespace.doc('get_activator')
    def get(self, organization, plugin_name):
        ''' Fetch the required information of a plugin '''
        return plugin_manager.get_required_info_of(organization, plugin_name)


@namespace.route('/')
class Organizations(Resource):
    ''' Show the all the organizations that have plugins'''
    @namespace.doc('list_organizations')
    def get(self):
        ''' Fetch all the organizations that have plugins installed '''
        return plugin_manager.get_organizations()

@namespace.route('/<string:organization>/')
@namespace.response(404, 'Organization  not found')
@namespace.param('organization', 'The name of the organization of the plugin')
class Plugins(Resource):
    ''' Show the required information of a plugin'''
    @namespace.doc('get_activator')
    def get(self, organization):
        ''' Fetch the required information of a plugin '''
        return plugin_manager.get_plugins_of(organization)