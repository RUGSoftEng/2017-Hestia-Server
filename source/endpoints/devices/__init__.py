from flask_restplus import Namespace

from model.Database import Database

device_database = Database()

namespace = Namespace('devices', description='All devices of the system')