from flask_restplus import Resource

from endpoints.plugins import namespace, business_logic_required_info


@namespace.route("/")
class Organizations(Resource):
    """ Show all the organizations that have plugins """

    @namespace.doc("list_organizations")
    def get(self):
        """ Fetch all the organizations that have plugins installed """
        return business_logic_required_info.get_organizations()


@namespace.route("/<string:organization>/")
@namespace.response(404, "Organization  not found")
@namespace.param("organization", "The name of the organization of the plugin")
class Plugins(Resource):
    """ Show all plugins of an organization """

    @namespace.doc("get_activator")
    def get(self, organization):
        """ Fetch the plugin of an organization """
        return business_logic_required_info.get_plugins_by_organization(organization)


@namespace.route("/<string:organization>/plugins/<string:plugin_name>")
@namespace.response(404, "Organization or plugin not found")
@namespace.param("organization", "The name of the organization of the plugin")
@namespace.param("plugin_name", "The name of the plugin")
class RequiredInfo(Resource):
    """ Show the required information of a plugin """

    @namespace.doc("get_activator")
    def get(self, organization, plugin_name):
        """ Fetch the required information of a plugin based on its organization and name """
        return business_logic_required_info.get_required_info_by_organization_and_plugin_name(organization, plugin_name)