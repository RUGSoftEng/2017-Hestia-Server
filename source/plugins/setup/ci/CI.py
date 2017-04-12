from model.Device import Device


class CI(Device):
    @classmethod
    def _get_plugin_type(cls):
        pass

    @classmethod
    def _get_organization(cls):
        return "Setup"

    def setup(self):
        pass

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {}

    @classmethod
    def _get_plugin_name(cls):
        return "HestiaCI"