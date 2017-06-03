def handle_hestia_exception(error):
    return handle_exception(error.__class__.__name__, error.to_dict())


def handle_standard_exception(error):
    response = dict()
    return handle_exception("ServerException", error.message)


def handle_exception(error, message):
    response = dict()
    response["error"] = error
    response["message"] = message
    return response, 500
