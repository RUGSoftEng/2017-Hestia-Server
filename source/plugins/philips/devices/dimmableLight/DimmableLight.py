from plugins.philips.PhilipsDevice import PhilipsDevice


class DimmableLight(PhilipsDevice):
    """
       Device that can be used for the following philips hue types:
       - Dimmable light
       - Color temperature light
       """

    @classmethod
    def setup(cls, required_info):
        options = required_info
        types = ["Color temperature light", "Dimmable light"]
        options["base_path"] = cls._get_base_path(required_info, types)
        return options
