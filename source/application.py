
import unittest

import sys
from coverage import coverage

from flask import Flask
from flask_script import Manager
from werkzeug.contrib.fixers import ProxyFix
from endpoints.api import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

manager = Manager(app)

@manager.command
def run():
    app.run(host="0.0.0.0", port=8000)

@manager.command
def dev():
    app.run(debug=True, host="0.0.0.0", port=8000)

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
    manager.run()
