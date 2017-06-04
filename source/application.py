import unittest

import sys
from coverage import coverage
from flask_sslify import SSLify

from flask import Flask
from flask_script import Manager
from werkzeug.contrib.fixers import ProxyFix

from MyListener import MyListener
from endpoints.api import api

from zeroconf import *

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
    type = "_http._tcp.local."
    listener = MyListener()
    browser = ServiceBrowser(r, type, listener)
    manager.run()
