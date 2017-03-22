import ipaddress

class IpAddressAndPort():

    def __init__(self):
        self._ipAddress = ipaddress.ip_address("127.0.0.1")
        self.port = 0

    @property
    def ipAddress(self):
        return self._ipAddress

    @ipAddress.setter
    def ipAddress(self, string):
        self._ipAddress = ipaddress.ip_address(string)
