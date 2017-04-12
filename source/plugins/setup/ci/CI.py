from model.Device import Device
from plugins.setup.ci.PullDevelopment import PullDevelopment


class CI(Device):
    def __init__(self):
        super().__init__()
        super().add_activator(PullDevelopment())

    @classmethod
    def _get_plugin_type(cls):
        return "Setup"

    @classmethod
    def _get_organization(cls):
        return "Setup"

    def setup(self):
        True

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {}

    @classmethod
    def _get_plugin_name(cls):
        return "HestiaCI"