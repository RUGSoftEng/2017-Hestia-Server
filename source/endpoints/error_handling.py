import traceback

import sys


def handle_hestia_exception(error):
    traceback.print_exc(file=sys.stdout)
    return handle_exception(error.__class__.__name__, error.to_dict())


def handle_standard_exception(error):
    traceback.print_exc(file=sys.stdout)
    return handle_exception("ServerException", {"exception": error.__class__.__name__})


def handle_exception(error, details):
    response = dict()
    response["error"] = error
    response["details"] = details
    return response, 500
