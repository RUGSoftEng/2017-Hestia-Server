from flask_restplus import abort

from logic.util import abort_with_error
from util.InvalidStateException import InvalidStateException
from util.NotFoundException import NotFoundException


class ActivatorLogic:
    """This class contain all logic needed to retrieve and interact with activators. 
    Currently this only involves interaction with the database. In later versions this
    could be extended to, for example, checking whether or not the user is allowed to
    access the requested activator."""

    def __init__(self, db):
        self._database = db

    def get_activator(self, device_id, activator_id):
        try:
            device = self._database.get_device(device_id)
            activator = device.get_activator(activator_id)
            return activator
        except NotFoundException as exception:
            abort_with_error(str(exception))

    def change_activator_state(self, device_id, activator_id, state):
        try:
            device = self._database.get_device(device_id)
            options = device.options
            activator = device.get_activator(activator_id)
            activator.state = state
            activator.perform(options)
        except InvalidStateException as exception:
            abort(400, str(exception))
        except NotFoundException as exception:
            abort(404, str(exception))

