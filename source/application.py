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
from util.LanIp import get_lan_ip

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
    succes = unittest.TextTestRunner().run(test).wasSuccessful()
    return not succes

if __name__ == "__main__":
    r = Zeroconf()
    addr = get_lan_ip()
    info = ServiceInfo("_hestia._tcp.local.",
                       "HestiaServer._hestia._tcp.local.",
                       server = "HestiaServer", port=8000, properties = {'api_level': api.version},
                               address = socket.inet_aton(addr), weight = 0, priority = 0)

    r.unregister_all_services()
    r.register_service(info)
    manager.run()
