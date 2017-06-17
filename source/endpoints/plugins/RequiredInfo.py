from flask_restplus import Resource

from endpoints.error_handling import handle_hestia_exception, handle_standard_exception
from endpoints.plugins import namespace
from exceptions.HestiaException import HestiaException
from logic import plugin_logic


@namespace.route("/")
class Collections(Resource):
    """ Show all the collections that have plugins """

    @namespace.doc("list_collections")
    def get(self):
        """ Fetch all the collections that have plugins installed """
        try:
            return_collection = plugin_logic.get_collections()
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return return_collection


@namespace.route("/<string:collection>/")
@namespace.response(404, "Collection  not found")
@namespace.param("collection", "The name of the collection of the plugin")
class Plugins(Resource):
    """ Show all plugins of an collection """

    @namespace.doc("get_activator")
    def get(self, collection):
        """ Fetch all plugins of an collection """
        try:
            return_plugins = plugin_logic.get_plugins(collection)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return return_plugins


@namespace.route("/<string:collection>/plugins/<string:plugin_name>")
@namespace.response(404, "Collection or plugin not found")
@namespace.param("collection", "The name of the collection of the plugin")
@namespace.param("plugin_name", "The name of the plugin")
class RequiredInfo(Resource):
    """ Show the required information of a plugin """

    @namespace.doc("get_activator")
    def get(self, collection, plugin_name):
        """ Fetch the required information of a plugin based on its collection and name """
        try:
            return_required_info = plugin_logic.get_required_info(collection, plugin_name)
        except HestiaException as error:
            return handle_hestia_exception(error)
        except Exception as error:
            return handle_standard_exception(error)
        return return_required_info
