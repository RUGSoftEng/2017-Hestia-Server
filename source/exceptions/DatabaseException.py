from exceptions.HestiaException import HestiaException


class DatabaseException(HestiaException):

    def __init__(self, type, message):
        HestiaException.__init__(self)
        self._type = type
        self._message = message

    def to_dict(self):
        return {"type":self._type, "message" : self._message}

    def get_http_code(self):
        return 404
