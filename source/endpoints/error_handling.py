import traceback

import sys

from flask_restplus import abort


def handle_hestia_exception(error):
    traceback.print_exc(file=sys.stdout)
    return handle_exception(error.__class__.__name__
                            , error.to_dict()
                            , error.get_http_code())


def handle_standard_exception(error):
    traceback.print_exc(file=sys.stdout)
    return handle_exception("ServerException"
                            , {"exception": error.__class__.__name__}
                            , 500)


def handle_exception(error, details, http_code):
    response = dict()
    response["exception"] = error
    response["details"] = details
    abort(http_code, error=response)