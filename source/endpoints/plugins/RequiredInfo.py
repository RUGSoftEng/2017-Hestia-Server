from flask_restplus import Resource

from endpoints.plugins import namespace
from logic import plugin_logic


@namespace.route("/")
class Organizations(Resource):
    """ Show all the organizations that have plugins """

    @namespace.doc("list_organizations")
    def get(self):
        """ Fetch all the organizations that have plugins installed """
        return plugin_logic.get_organizations()


@namespace.route("/<string:organization>/")
@namespace.response(404, "Organization  not found")
@namespace.param("organization", "The name of the organization of the plugin")
class Plugins(Resource):
    """ Show all plugins of an organization """

    @namespace.doc("get_activator")
    def get(self, organization):
        """ Fetch all plugins of an organization """
        return plugin_logic.get_plugins(organization)


@namespace.route("/<string:organization>/plugins/<string:plugin_name>")
@namespace.response(404, "Organization or plugin not found")
@namespace.param("organization", "The name of the organization of the plugin")
@namespace.param("plugin_name", "The name of the plugin")
class RequiredInfo(Resource):
    """ Show the required information of a plugin """

    @namespace.doc("get_activator")
    def get(self, organization, plugin_name):
        """ Fetch the required information of a plugin based on its organization and name """
        return plugin_logic.get_required_info(organization, plugin_name)
