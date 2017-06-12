from flask_restplus import abort


def abort_with_error(message):
    abort(404, error=message)
