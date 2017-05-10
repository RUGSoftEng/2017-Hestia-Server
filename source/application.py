import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from endpoints.api import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

if __name__ == "__main__":
    """ Setting host to 0.0.0.0 makes it available within the network. """
    app.run(debug=True, host="0.0.0.0", port=8000)
