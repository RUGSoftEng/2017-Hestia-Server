from models.Device import Device


class Light(Device):
    """"
        Mock light device. 
        """

    @classmethod
    def setup(cls, required_info):
        print("Mock light is being setup")
        return required_info