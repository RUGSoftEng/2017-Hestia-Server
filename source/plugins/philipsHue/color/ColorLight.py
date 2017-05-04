from model.Device import Device
from plugins.philipsHue.activators.SliderBrightness import SliderBrightness
from plugins.philipsHue.activators.SliderColor import SliderColor
from plugins.philipsHue.activators.SwitchOnOff import SwitchOnOff
from plugins.philipsHue.utils import get_lamp_id_for_types, get_new_user_if_needed


class ColorLight(Device):
    """
    Device that can be used for the following philips hue types:
        - Color light
        - Extended color light
    """
    types = ["Extended color light", "Color light"]

    def __init__(self):
        super().__init__()
        super().add_activator(SwitchOnOff())
        super().add_activator(SliderBrightness())
        super().add_activator(SliderColor())
        self._baseUrl = None

    def setup(self):
        """
        By calling this method the system connects with the philips hue bridge
        to get all the information necessary to control the light.
        """
        get_new_user_if_needed(self.required_info)
        get_lamp_id_for_types(self.required_info, self.types)

    @classmethod
    def _get_organization(cls):
        return 'Philips'

    @classmethod
    def _get_plugin_name(cls):
        return "ColorLight"

    @classmethod
    def _get_plugin_type(cls):
        return "Light"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        """
        ip :            ip of philips hue bridge
        user :          string for identification
        search_method : method used to find the lamp ID
        """
        return {"ip": "127.0.0.1", "user": "unknown", "search_method": "last"}

