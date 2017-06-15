from plugins.philips.PhilipsDevice import PhilipsDevice


class ColorLight(PhilipsDevice):
    """
       Device that can be used for the following philips hue types:
       - Color light
       - Extended color light
       """

    @classmethod
    def setup(cls, required_info):
        options = required_info
        types = ["Color light", "Extended color light"]
        options["base_path"] = cls._get_base_path(required_info, types)
        return options
