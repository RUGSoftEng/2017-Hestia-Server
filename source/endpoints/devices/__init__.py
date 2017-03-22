from flask_restplus import Namespace

from model.DeviceDAO import DeviceDAO

DAO = DeviceDAO()

ns = Namespace('devices', description='All devices of the system')