from exceptions.HestiaException import HestiaException


class SetupFailedException(HestiaException):
    def __init__(self, field, hint):
        self._field = field
        self._hint = hint

    def to_dict(self):
        response = dict()
        response["field"] = self._field
        response["hint"] = self._hint
