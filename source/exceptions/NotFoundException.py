from exceptions.HestiaException import HestiaException


class NotFoundException(HestiaException):
    def __init__(self, type):
        HestiaException.__init__(self)
        self._type = type

    def to_dict(self):
        return {"type" : self._type}
