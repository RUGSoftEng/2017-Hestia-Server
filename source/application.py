import unittest

import sys
from coverage import coverage
from flask_sslify import SSLify

from flask import Flask
from flask_script import Manager
from werkzeug.contrib.fixers import ProxyFix
from endpoints.api import api

from zeroconf import *
import socket

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
sslify = SSLify(app)

api.init_app(app)

manager = Manager(app)


@manager.command
def run():
    app.run(host="0.0.0.0", port=8000, ssl_context='adhoc')


@manager.command
def dev():
    app.run(debug=True, host="0.0.0.0", port=8000, ssl_context='adhoc')


@manager.command
def test():
    sys.exit(__run_test())


@manager.command
def cov():
    cov = coverage(source = "./")
    cov.start()
    succes = __run_test()
    cov.stop()
    cov.save()
    print("Coverage summary")
    cov.report()
    sys.exit(succes)


def __run_test():
    test = unittest.TestLoader().discover("tests")
    success = unittest.TextTestRunner().run(test).wasSuccessful()
    return not success


def _publish_server():
    """This method publishes the server using the zero conf protocol.
    This makes it possible for the client application to find the ip
    of the server easily."""
    zero_conf = Zeroconf()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))   # Prepares a socket for connecting to google
                                # without actually sending something
    local_ip_address = s.getsockname()[0]   # Gets the ip of the socket that
                                            # would be used
    bytes = socket.inet_aton(local_ip_address)
    info = ServiceInfo("_hestia._tcp.local.",
                       "HestiaServer._hestia._tcp.local.",
                       port=8000, properties={'api_level': api.version},
                       address=bytes, weight=0, priority=0)

    zero_conf.unregister_all_services()
    zero_conf.register_service(info)

if __name__ == "__main__":
    _publish_server()
    manager.run()
