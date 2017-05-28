from flask_restplus import Resource

from endpoints.plugins import namespace
from logic import plugin_logic


@namespace.route("/")
class Collections(Resource):
    """ Show all the collections that have plugins """

    @namespace.doc("list_collections")
    def get(self):
        """ Fetch all the collections that have plugins installed """
        return plugin_logic.get_collections()


@namespace.route("/<string:collection>/")
@namespace.response(404, "Collection  not found")
@namespace.param("collection", "The name of the collection of the plugin")
class Plugins(Resource):
    """ Show all plugins of an collection """

    @namespace.doc("get_activator")
    def get(self, collection):
        """ Fetch all plugins of an collection """
        return plugin_logic.get_plugins(collection)


@namespace.route("/<string:collection>/plugins/<string:plugin_name>")
@namespace.response(404, "Collection or plugin not found")
@namespace.param("collection", "The name of the collection of the plugin")
@namespace.param("plugin_name", "The name of the plugin")
class RequiredInfo(Resource):
    """ Show the required information of a plugin """

    @namespace.doc("get_activator")
    def get(self, collection, plugin_name):
        """ Fetch the required information of a plugin based on its collection and name """
        return plugin_logic.get_required_info(collection, plugin_name)
