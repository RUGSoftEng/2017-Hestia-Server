from model.Device import Device
from plugins.setup.git.PullDevelopment import PullDevelopment


class UpdateServer(Device):
    """
    This device is used as a demonstration of what the system can do.
    It is a basic continues integration system.
    Different activators reflect different branches to pull.
    """
    def __init__(self):
        super().__init__()
        super().add_activator(PullDevelopment())

    @classmethod
    def _get_plugin_type(cls):
        return "Setup"

    @classmethod
    def _get_organization(cls):
        return "Hestia"

    def setup(self):
        """
        There is no setup required for this device at the moment.
        Later versions should include a way of login in.
        """
        True

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {}

    @classmethod
    def _get_plugin_name(cls):
        return "UpdateServer"