from flask_restplus import fields


class StateTypeToString(fields.Raw):
    def format(self, value):
        return value.__name__
