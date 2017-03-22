from flask_restplus import fields

from endpoints.devices import ns
from endpoints.util.ToString import ToString
from model.IpAddressAndPort import IpAddressAndPort

ipAddress = ns.model('ipAddressAndPort', {
                             'ipaddress': ToString(attribute='ipAddress')
                             ,'port': fields.Integer(required=True)
})


class RequiredInfo(fields.Raw):
    def format(self, value):
        # TODO: Implement correct method to parse a ipAddress
        print(str(value))
        if value.__name__ == "IpAddressAndPort":
            return "here"
        else:
            return "there"
