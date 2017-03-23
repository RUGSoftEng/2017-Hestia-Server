from flask_restplus import Namespace

from model.Database import Database

DAO = Database()

ns = Namespace('devices', description='All devices of the system')