from flask import jsonify

from endpoints.api import api
from exceptions import SetupFailedException, HestiaException


@api.errorhandler(HestiaException)
def handle_hestia_exception(error):
    response = dict()
    response["error"] = error.__class__.__name__
    response["message"] = error.to_dict()
    return jsonify(response), 500
