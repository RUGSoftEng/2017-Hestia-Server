from exceptions.HestiaException import HestiaException


class InvalidStateException(HestiaException):
    def __init__(self, new_value, expected_type):
        HestiaException.__init__(self)
        self.new_value = new_value
        self.expected_type = expected_type

    def to_dict(self):
        response = dict()
        response["expected_type"] = str(self.expected_type)
        response["value_type"] = str(type(self.new_value))
        return response