from flask_restplus import fields


class ToString(fields.Raw):
    def format(self, value):
        return str(value)
